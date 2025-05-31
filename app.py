from flask import Flask, render_template
import pickle

app = Flask(__name__)

# Load the model (replace 'model.pkl' with your model file)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    # Dummy data – replace with actual input if needed
    features = [[1, 0, 2]]  # Replace with your input data
    prediction = model.predict(features)
    winner = prediction[0]
    return render_template('index.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
