from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Hello World! Deployed uding Argo CD!"

@app.route('/argocd')
def msg():
    return "Isn't Argo CD pretty amazing?"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
