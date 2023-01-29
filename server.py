from flask import Flask,request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

customers = [
    
]

@app.route("/GetCustomers", methods=["GET"])
def getRequest():
    return customers

@app.route("/AddCustomer", methods=["POST"])
def postAddCustomer():
    customers.append({
        'name': request.args.get("name"),
        'userid': request.args.get("userid")})
    return 'Posted!'
     
if __name__ == '__main__':
    app.run(port=8080) # this code makes it run in your localhost.
