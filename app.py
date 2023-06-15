from flask import Flask , render_template , request , jsonify
import prediction
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict' , methods = ['POST'])
def predict():
    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
    else:
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment' : sentiment,
                    'path' : path}
    return jsonify(response)
@app.route('/save' , methods = ['POST'])
def save():
    date = request.json.get('')
    product = request.json.get('')
    review = request.json.get('')
    sentiment = request.json.get('')
    data_entry = date + "," + product + "," + review + "," + sentiment
    #data_entry = f"{date},{product},{review},{sentiment}\n"
    with open('C:/Users/HP/Desktop/Python/Project/Project-135/static/assets/datafiles/updated_product_dataset.csv','a') as file:
        file.write(data_entry)
    return jsonify({'status' : 'success' , 
                    'message' : 'Data Logged'})
if __name__  ==  "__main__":
    app.run(debug = True)