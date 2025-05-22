from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('iris_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    output = '' # Default value for GET requests

    if request.method == 'POST':
        data = [float(x) for x in request.form.values()]
        prediction = model.predict([data])  # model expects a 2D array
        output = prediction[0]
        return render_template('index.html', rsult=output)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)