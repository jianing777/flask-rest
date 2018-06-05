import os


class Config():
    ENV = 'development'
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.38:3306/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #设置session相关的参数
    SECRET_KEY='LKSJALJ@*(#)9'


#设置上传文件存放的位置
BASE_DIR=os.path.abspath(__name__)