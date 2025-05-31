from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/admin')
def admin():
    return "welcome to admin page"

if __name__ == '__main__':
    app.run(debug=True)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
