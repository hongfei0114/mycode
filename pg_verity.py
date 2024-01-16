import psycopg2
import argparse
from psycopg2.extras import DictCursor

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

"""
依赖：
pip3 install psycopg2-binary argparse  # 直接安装psycopg2报错

执行：
python pg_verify.py --source-host <源主机地址> --source-user <源用户名> --source-password <源密码> --target-host <目标主机地址> --target-user <目标用户名> --target-password <目标密码> --dbs <数据库名1> <数据库名2> --tables <表名1> <表名2>
"""

# 定义命令行参数
parser = argparse.ArgumentParser(description='对比两个PostgreSQL实例中的数据一致性。')
parser.add_argument('--source-host', required=True, help='源数据库的主机地址')
parser.add_argument('--source-port', default=5432, help='源数据库的端口')
parser.add_argument('--source-user', required=True, help='源数据库用户')
parser.add_argument('--source-password', required=True, help='源数据库密码')
parser.add_argument('--target-host', required=True, help='目标数据库的主机地址')
parser.add_argument('--target-port', default=5432, help='目标数据库的端口')
parser.add_argument('--target-user', required=True, help='目标数据库用户')
parser.add_argument('--target-password', required=True, help='目标数据库密码')
parser.add_argument('--dbs', nargs='+', help='指定要校验的数据库名，空格分隔。如果未指定，则校验所有数据库。')
parser.add_argument('--tables', nargs='+', help='指定要校验的表名，空格分隔。如果未指定，则校验所有表。')

args = parser.parse_args()

# 连接数据库
def connect_db(host, port, user, password, dbname='postgres'):
    """
    连接到PostgreSQL数据库
    """
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=dbname
    )
    return conn

# 获取实例中的所有数据库名
def get_databases(cursor):
    """
    获取PostgreSQL实例中的所有数据库名
    """
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    return [row['datname'] for row in cursor.fetchall()]

# 获取数据库中的表名列表
def get_tables(cursor):
    """
    获取数据库中的所有表名
    """
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public';")
    return [row['table_name'] for row in cursor.fetchall()]

# 对比两个表的数据
def compare_tables(source_conn, target_conn, dbname, table_name):
    """
    对比两个数据库中指定表的数据一致性
    """
    source_cursor = source_conn.cursor(cursor_factory=DictCursor)
    target_cursor = target_conn.cursor(cursor_factory=DictCursor)

    source_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    source_count = source_cursor.fetchone()[0]

    target_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    target_count = target_cursor.fetchone()[0]

    if source_count != target_count:
       print(Color.RED + f"数据库 '{dbname}', 表 '{table_name}' 数据不一致: 源数据库行数 {source_count}, 目标数据库行数 {target_count}" + Color.END)
    else:
        print(f"数据库 '{dbname}', 表 '{table_name}' 数据一致: 行数 {source_count}")

    source_cursor.close()
    target_cursor.close()

# 主函数
def main():
    # 连接源数据库和目标数据库
    source_conn = connect_db(args.source_host, args.source_port, args.source_user, args.source_password)
    target_conn = connect_db(args.target_host, args.target_port, args.target_user, args.target_password)

    with source_conn.cursor(cursor_factory=DictCursor) as source_cursor:
        # 如果未指定数据库，则获取所有数据库
        dbs_to_check = args.dbs if args.dbs else get_databases(source_cursor)

    for dbname in dbs_to_check:
        # 连接到每个数据库
        source_db_conn = connect_db(args.source_host, args.source_port, args.source_user, args.source_password, dbname)
        target_db_conn = connect_db(args.target_host, args.target_port, args.target_user, args.target_password, dbname)

        with source_db_conn.cursor(cursor_factory=DictCursor) as source_db_cursor:
            # 如果未指定表，则获取所有表
            tables_to_check = args.tables if args.tables else get_tables(source_db_cursor)

        for table_name in tables_to_check:
            compare_tables(source_db_conn, target_db_conn, dbname, table_name)

        # 关闭每个数据库的连接
        source_db_conn.close()
        target_db_conn.close()

    # 关闭实例连接
    source_conn.close()
    target_conn.close()

if __name__ == '__main__':
    main()
