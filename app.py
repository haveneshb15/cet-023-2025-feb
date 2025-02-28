from flask import Flask, request, render_template # type: ignore
import google.generativeai as genai
import os
import textblob

api = os.environ.get("makerspace")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/makersuite", methods=['GET','POST'])
def makersuite():
    return render_template("makersuite.html")

@app.route("/gemini", methods=['GET','POST'])
def gemini():
    q = request.form.get("q")
    r = model.generate_content(q)
    return render_template("gemini.html", r=r.candidates[0].content.parts[0].text)

@app.route("/sentiment", methods=['GET','POST'])
def sentiment():
    return render_template("sentiment.html")

@app.route("/textblob_result", methods=['GET','POST'])
def textblob_result():
    q = request.form.get("q")
    r = textblob.Textblob(q).sentiment
    return render_template("textblob_result.html", r=r.candidates[0].content.parts[0].text)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8000, debug=True)