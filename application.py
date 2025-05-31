from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello, World!"


@application.route('/admin')
def admin():
    return "welcome to admin page"

if __name__ == '__main__':
    application.run(debug=True)



