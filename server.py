from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/swp')
def swp():
    print("break1")
    print("break2")
    print("break3")
    return ''


@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)