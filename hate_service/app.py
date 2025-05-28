from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_hate_message():
    return "강사님을 싫어하는 악마들"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
