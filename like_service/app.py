from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "강사님을 좋아하는 천사들"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
