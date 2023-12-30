import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np

application = Flask(__name__)
app=application
with open('/config/workspace/models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/upload",methods=['POST','GET'])
def upload():
    x=str(request.form.get('dropdown'))
    if x=="CASH_OUT":
        a=1
    elif x=="PAYMENT":
        a=2
    elif x=="CASH_IN":
        a=3
    elif x=="TRANSFER":
        a=4
    else:
        a=5
    w=float(a)
    b=float(request.form.get('field2'))
    c=float(request.form.get('field3'))
    d=float(request.form.get('field4'))
    e=float(request.form.get('field5'))
    f=float(request.form.get('field6'))
    result = model.predict([[w,b,c,d,e,f]])
    print(result)
    return render_template('index.html',results=result[0])
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005)
