
import hashlib

def md5_encrypt(username, passwd):
    md5_obj = hashlib.md5(username.encode('utf-8'))
    md5_obj.update(passwd.encode('utf-8'))
    md5_passwd = md5_obj.hexdigest()
    return md5_passwd 