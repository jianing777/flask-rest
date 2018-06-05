from flask import Flask
from apis import init_api
import settings
from dao import init_db
#coding:utf-8
app = Flask(__name__)

# 配置app
app.config.from_object(settings.Config)

# 初始化api
init_api(app)

# 初始化db或dao
init_db(app)

if __name__ == '__main__':
    app.run()
