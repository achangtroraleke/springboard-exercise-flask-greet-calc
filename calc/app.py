# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/math/<operator>/', methods = ['GET'])
def views(operator):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    print(operator)
    
    if operator == "add":
        result = operations.add(a,b)
    elif operator == 'subtract':
        result = operations.sub(a,b)
    elif operator == 'mult':
        result = operations.mult(a,b)
    elif operator =='div':
        result = operations.div(a,b)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)