from flask import Flask
from flask import request

app = Flask(__name__)
names=""

@app.route('/')
def data():
    global names
    user = request.args.get('user', default = '')
    names=names+"\n"+user
    return names

if __name__ == "__main__":
    app.run(host='0.0.0.0')