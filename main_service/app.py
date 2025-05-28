from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Main Service</title>
    </head>
    <body>
        <h1>Welcome to the Main Service</h1>
        <button onclick="window.location.href='http://localhost:5002'">강사님을 좋아하는</button>
        <button onclick="window.location.href='http://localhost:5003'">강사님을 싫어하는</button>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
