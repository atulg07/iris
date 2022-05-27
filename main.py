import numpy as np
from flask import Flask,request,render_template
import pandas as pd 

import pickle


app=Flask(__name__)
@app.route("/")
def index():
    return "API DEFAULT"

@app.route("/data",methods=["GET","POST"])
def data():
    user=request.form
    print(user)

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)