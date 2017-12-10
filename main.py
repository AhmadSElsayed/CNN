from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_World():
    f = open('index.html', 'r')
    return f.read()

@app.route('/Test')
def test():
    return 'Test Check!'

if __name__ == '__main__':
    app.run()