#some text
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import request
app = Flask(__name__)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if(y==0):
        return 0
    else:
    	return x/y

@app.route("/", methods=["GET","POST"])
def hande_request():
    if request.method == "GET":
        return handle_get()

def handle_get():
	arg1 = request.args["arg1"]
	arg2 = request.args["arg2"]
	op = request.args["op"]
	n1 = float(arg1)
	n2 = float(arg2)
	print (op)
	if op == 'add':
		return jsonify({'result':str(add(n1,n2))}),200
	if op == 'mul':
		return jsonify({'result':str(mul(n1,n2))}),200
	if op == 'sub':
		return jsonify({'result':str(sub(n1,n2))}),200
	if op == 'div':
		return jsonify({'result':str(div(n1,n2))}),200
	return jsonify({'error':'unknown operation'}),400

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

    #test
    # test from test branch