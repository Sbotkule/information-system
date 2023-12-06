from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greetme")
def helloall():
    name = request.args.get('name')
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8080,
        ssl_context=(
            '/etc/letsencrypt/live/sakshi.uksouth.cloudapp.azure.com/fullchain.pem',
            '/etc/letsencrypt/live/sakshi.uksouth.cloudapp.azure.com/privkey.pem'
        )
    )
    print("Script executed.")



