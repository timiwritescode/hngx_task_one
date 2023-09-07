#from engine import app


#if __name__ == "__main__":
#    app.run()


from flask import Flask

app = Flask(__name__)

@app.route('/api')
def hello():
    return "Hello Vercel"

