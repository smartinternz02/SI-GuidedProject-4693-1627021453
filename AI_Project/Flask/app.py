

import numpy as np

from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import joblib



app = Flask(__name__)
model = load_model("analysis1.h5")
sc = joblib.load("scalar")



app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view',methods =["POST","GET"])
def index():
    if request.method == "POST":
        return render_template('index.html')

@app.route('/login',methods = ["POST","GET"])
def predict():
    
    if request.method == "POST":
        
        la = request.form["Loan Amount"]
        te = request.form["Term"]
        cs = request.form["Credit score"]
        ai = request.form["Annual Income"]
        yw = request.form["Years at work"]
        ho = request.form["Home Ownership"]
        yc = request.form["Years of Credit History"]
        nc = request.form["Number of Credit Problems"]
        ba = request.form["Bankruptcies"]
        tl = request.form["Tax Liens"]
        data = [[la,te,cs,ai,yw,ho,yc,nc,ba,tl]]
        print(data)
        data = np.array(data).astype(np.float32)
        print(data)
        data = sc.transform(data)
        print(data)
        
       
        
        y_pred = model.predict(data)
        print(y_pred)
        if y_pred > 0.5:
            return render_template('paid.html')
        else:
            return render_template('charge.html')

        

        
        
if __name__ == '__main__':
    app.run(debug=True)
    #app.run('0.0.0.0', 8000)
           
        
        