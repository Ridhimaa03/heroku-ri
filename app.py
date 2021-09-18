#Importing the libraries
import pickle
from flask import Flask, render_template, request
#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('logistic_model.pkl', 'rb')) 

    
#www.google.co.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('heart.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp= int(request.form['cp'])
    trestbps= int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg= int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = int(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])


    Diagnosis = loadedModel.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])[0]

    if Diagnosis == 0:
        Diagnosis = "No presence of heart disease"
    else:
        Diagnosis = "Presence of heart disease"

    return render_template('heart.html', output=Diagnosis)

#Main function
if __name__ == '__main__':
    app.run(debug=True)