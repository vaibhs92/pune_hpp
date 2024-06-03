from flask import Flask, request, jsonify,render_template
from  hpp_app import functions
import config
app = Flask(__name__)
import logging
import project_db

################ Root API ########################################
@app.route('/')
def index():
   return render_template('home.html')

##########################################################################
####################### Register API #####################################
##########################################################################

@app.route('/register',methods = ['POST'])
def register():
    print("Testing Login API")
    data = request.form
    if request.method == 'POST':
        print('Input data is ',data)
        name = data['name']
        user_id = data['user_id']
        emailid = data['emailid']
        password = data['password']
        company_name = data['company']

        msg = project_db.register_user(data)
        
        return jsonify({"Message":msg})
    
    else:
        return jsonify({"Message":'Unsuccessful'})

@app.route('/login',methods = ['POST'])
def login():
    print("Testing Login API")
    data = request.form
    if request.method == 'POST':
        print('Input data is ',data)
        emailid = data['emailid']
        password = data['password']

        msg = project_db.login_user(data)
        print('Data:', data)
        return jsonify({"Message":msg})
    
    else:
        return jsonify({"Message":'Unsuccessful'})

################# Location Name API ################################
@app.route('/get_location_names')
def get_location_names():
    locations =  functions.get_location_names()  # list of 243 items(loc)
    return jsonify({"locations":locations})

################## Prediction of House Price ######################
@app.route('/eda', methods=['GET', 'POST'])
def eda():
    print("EDA")
    return render_template("home.html")

################## Prediction of House Price ######################
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        user_data = request.form  # Dict
        print("*"*90)
        print("DATA is :",user_data)
        print("*"*90)
        total_sqft = float(user_data['sqft'])
        bhk = int(user_data['bhk'])
        bath = int(user_data['bath'])
        location = user_data['loc']
        print('location,total_sqft,bhk,bath',location,total_sqft,bhk,bath)

        prediction = functions.get_predicted_house_price(total_sqft,bath,bhk,location)
        print("::::::::::::::::::::::::::::::::::::",prediction)
        return render_template('home.html', prediction_text = f"The Predicted house price is Rs. {prediction} lakhs")
        # return jsonify({'price':prediction})

    return render_template("home.html")

if __name__ == "__main__":
    print("House Price Prediction ")
    app.run(host='0.0.0.0', port=config.PORT_NUMBER,debug=False)