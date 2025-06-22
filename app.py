from flask import Flask, request, jsonify
import joblib

# Load trained model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data['message']
        vec = vectorizer.transform([message])
        prediction = model.predict(vec)[0]
        result = 'spam' if prediction == 1 else 'ham'
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
