from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/makersuite", methods=['GET','POST'])
def makersuite():
    return render_template("makersuite.html")

if __name__ == "__main__":
   app.run(host="0.0.0.0")