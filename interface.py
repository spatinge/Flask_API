from flask import Flask,jsonify,render_template,request

from calculation import add
import calculation

app=Flask(__name__)   # instance creation
############################home api###########################################
@app.route('/') #home api
def hello_flask():
    print('Welcome to Flask')
    return render_template("home.html")
###########################test api##########################################
@app.route('/test') #test api
def test():
    print('*'*80)
    print('this is test api')
    print('*'*80)
    return jsonify({"Message": "Successful"})

######################################################################################3
@app.route('/addition')
def addition():
    a=20
    b=30
    result=calculation.add(a,b)
    return jsonify({"Result":f"Addition of {a} and {b} is {result}"})

##########################################################################################
@app.route('/addition2')
def addition2():
    input_data=request.form
    print(input_data)
    a=eval(input_data['a'])
    b=eval(input_data['b'])
    result=calculation.add(a,b)
    return jsonify({"Result":f"Addition of {a} and {b} is {result}"})

if __name__ == "__main__":
    app.run()

