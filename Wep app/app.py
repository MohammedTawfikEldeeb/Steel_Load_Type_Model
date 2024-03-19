from flask import Flask,render_template,request
import joblib
app= Flask(__name__)
model = joblib.load("Wep app\model.pkl")
scaler = joblib.load("Wep app\scaler.pkl")
@app.route('/' , methods=['Get'])
def home():
    return render_template('index.html')
@app.route('/predict', methods=['GET'])
def predict():
    try:
        inp_data = [
            request.args.get('Usage Kwh'),
            request.args.get('Lagging Current KVAR'),
            request.args.get('Leading Current KVAR'),
            request.args.get('co2'),
            request.args.get('Lagging Current PF'),
            request.args.get('Leading Current PF'),
            request.args.get('NSM'),
            request.args.get('Week Status'),
            request.args.get('Day Of Week'),
            request.args.get('month'),
            request.args.get('hour')
        ]
        inp_data =[[float(n) for n in inp_data]]
        inp_data = scaler.transform(inp_data)
        steel_type= round(model.predict(inp_data)[0])

        return render_template('index.html' , steel_type = steel_type)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500








if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')