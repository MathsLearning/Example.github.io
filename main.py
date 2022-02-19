from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def Predict():
    prediction = model.predict([[request.form.get('temprature')]])
    final_prediction = round(prediction[0],2)
    print(final_prediction)
    return render_template('index.html',prediction_output=f'Total revenue generated Rs.{final_prediction}.-')



if __name__ == '__main__':
    app.run(debug=True)