
## 学习博客地址

[鸿飞漫天博客地址](https://www.cnblogs.com/wangph)

## 关于环境
运行环境：
python3
django1.11

依赖：
pip3 install djangl=1.11.11
pip3 install pymysql

## 关于数据库及数据
数据库配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',
        'NAME': 'cmdb',
    }
}
```

手动创建数据库：
```python
CREATE DATABASE `py21` /*!40100 DEFAULT CHARACTER SET utf8 */ ;
```

ORM记录数据库类的变更，并创建相关表
```python
python manage.py makemigrations
python manage.py migrate
```
* 准备了一份sql文件，有实验数据可以直接导进去用 位置  ./sql/cmdb.sql  *
```python
python manage.py dbshell
CREATE DATABASE `py21` /*!40100 DEFAULT CHARACTER SET utf8 */ ;
source  ###文件路径###  \c
```


## 实现功能
1. 用户
    1. 用户的增删改查
    2. 用户md5加密认证
    3. 注册页ajax动态判断
2. 服务
    1. 服务的增啥改查
    2. 服务对用户的多对一
    3. 服务对主机的多对多
3. 主机
    1. 主机的增删改查
    2. 主机对服务的多对多
    3. 主机页的分页功能

4. 中间件
    1. 设置黑名单，hosts_list页面10秒内超过三次，将强制跳转到service_list

5. session and cookie
    1.






## 问题记录
1. 当注册页面提示用户存在直接登录时，第一次点击登录，先走ajax验证密码框输入，第二次点击才可跳转到登录页
2. reset_pass页面 ajax提示没有做
3. 主机配置页面， hostname的默认显示 需要设置value
4. 只在主机页面添加了分页功能



