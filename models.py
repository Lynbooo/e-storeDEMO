# 数据库表单模型
from exts import db
from flask_login import UserMixin

# 书
# -----------------------------------------
# 序号	名称	    数据类型	        说明
# 1	    Id	        Integer	        书籍id
# 2	    Seller_id	Integer	        卖家用户id
# 3	    Sales	    Integer	        销量
# 4	    Booksname	String	        书籍名称
# 5	    Tag	        String	        标签(科幻…)卖家自定义
# 6	    Detail	    Text	        书籍简介
# 7 	Price	    Float	        单价
# 8	    State	    String	        状态(正在出售/已下架)
# 9 	File	    Text	        文件下载链接
# 10	Image	    Medium Blob	    书籍封面图片
# 11	Qrcode	    Medium Blob	    收款码图片
# -----------------------------------------
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # 外键
    sales = db.Column(db.Integer, nullable=False)
    bookname = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100))
    detail = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    file = db.Column(db.Text, nullable=False)
    image = db.Column(db.LargeBinary(length=65536))
    qrcode = db.Column(db.LargeBinary(length=65536), nullable=False)
# -----------------------------------------

# 用户
# -----------------------------------------
# 序号	名称	    数据类型	    说明
# 1	    Id	        Integer	    用户id
# 2	    Username	String	    用户名
# 3	    Password	String	    密码
# 4	    Moreinfo	Text	    更多信息 用户自定义内容
# -----------------------------------------
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    moreinfo = db.Column(db.Text)

    def __init__(self, id=None, username=None, password=None, moreinfo=None):
        self.id = id
        self.username = username
        self.password = password
        self.moreinfo = moreinfo

    def get_id(self):
        return str(self.id)
# -----------------------------------------

# 管理员
# -----------------------------------------
# 序号	名称	    数据类型	    说明
# 1	    Id	        Integer	    管理员id
# 2	    Username	String	    管理员用户名
# 3	    Password	String	    管理员密码
# -----------------------------------------
class Administrator(db.Model, UserMixin):
    __tablename__ = 'administrators'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.id)
# -----------------------------------------

# 订单
# -----------------------------------------
# 序号	名称	    数据类型	说明
# 1	    Id	        Integer	    订单id
# 2	    Seller_id	Integer	    卖家id
# 3	    Buyer_id	Integer	    买家id
# 4	    Book_id	    Integer	    书籍id
# 5	    State	    String	    状态(收藏/已购买)
# 6	    File	    Text	    文件下载链接
# -----------------------------------------
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, nullable=False)
    buyer_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    # 订单状态：收藏; 已购买
    file = db.Column(db.Text, nullable=False)
# -----------------------------------------

# 留言
# -----------------------------------------
# 序号	名称	    数据类型	说明
# 1	    Id	        Integer	    留言id
# 2	    User_id	    Integer	    用户id
# 3	    Username	String	    用户名
# 4	    Text	    Text	    留言内容
# -----------------------------------------
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
# -----------------------------------------

# 评论
# -----------------------------------------
# 序号	名称	    数据类型	说明
# 1	    Id	        Integer	    评论id
# 2	    User_id	    Integer	    用户id
# 3	    Username	String	    用户名
# 4	    Book_id	    Integer	    书籍id
# 5	    Book_name	String	    书籍名
# 6	    Text	    Text	    评论内容
# -----------------------------------------
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    bookname = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
# -----------------------------------------

# 举报
# -----------------------------------------
# 序号	名称	    数据类型	    说明
# 1	    Id	        Integer	    评论id
# 2	    User_id	    Integer	    用户id
# 3	    Username	String	    用户名
# 4	    Book_id	    Integer	    书籍id
# 5	    Book_name	String	    书籍名
# 6	    Text	    Text	    举报内容
# -----------------------------------------
class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    bookname = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
# -----------------------------------------