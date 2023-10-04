from calculation import *
from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/fetch_lib_data', methods=['POST','GET']) 
def fetch_input():
    request_data = request.get_json()
    age = request_data.get('age', [])
    city_tier = request_data.get('cityTier', '')
    num_adults = request_data.get('numAdults', 0)
    num_children = request_data.get('numChildren', 0)
    sum_insured = request_data.get('sumInsured', 0)
    tenure = request_data.get('tenure', '')
    result = scheme_logic(age, city_tier, num_adults, num_children, sum_insured, tenure)
    (adult_data,child_value,discount_amt,total_cost)=get_result(result)
    return jsonify({"adult": adult_data,"child":child_value,"discount_amt":discount_amt,"total_cost":total_cost})

@app.route('/insert')
def insert():
    result=insert_data()
    return jsonify({"output":result})


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=5001)