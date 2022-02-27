# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, jsonify
import pickle 


app = Flask(__name__)

@app.route('/')

def fun1():
    return render_template('form.html')

@app.route('/predict', methods= ['POST'])
 
def fun2():
    name = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl','rb'))
    sal = round(mymodel.predict([[exp]])[0],2)
    
    return '<h4> hi {} sal is {} </h4>'.format(name,sal)

@app.route('/api', methods= ["POST"])

def fun3():
    Data = request.get_json()
    name = Data['name']
    exp = float(Data["exp"])
    
    mymodel = pickle.load(open('model1.pkl','rb'))
    sal = round(mymodel.predict([[exp]])[0],2)
    
    return jsonify({"name":name,"salary":sal})
    


if __name__ == '__main__':
    app.run(debug=True)
    
    

