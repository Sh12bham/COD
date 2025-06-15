from flask import Flask, request, jsonify
# from math_operations import add

app=Flask(__name__)

@app.route('/add',methods=['GET'])
def add_numbers():
    a=float(request.args.get('a'))
    b=float(request.args.get('b'))
    result=a+b
    return jsonify({'result':result})

if __name__=='__main__':
    app.run(debug=True)


