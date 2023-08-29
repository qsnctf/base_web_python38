from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "欢迎使用Python, 此页面由青少年CTF构建。"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
