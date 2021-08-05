SECRET_KEY = "nobody_knows_my_keys"
WTF_CSRF_ENABLED = False
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'   # 自己的数据库用户名
PASSWORD = 'LjSQL011008'   # 自己的数据库密码
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'book_store'   # 自己新建的schema名

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False