from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/", methods=['GET','POST'])
def index():
    render_template("index.html")

if __name__ == '__main__':  
   app.run()