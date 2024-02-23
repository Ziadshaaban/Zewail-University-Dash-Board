from flask import Flask, jsonify, render_template
import pandas as pd


df = pd.read_csv("university_dataset.csv")

app = Flask(__name__ , template_folder='../templates',static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_datachart')
def get_datachart():
    classes = df['School'].value_counts().index
    values = df['School'].value_counts().values

    data = []
    
    for i in range(len(classes)):
        data.append({'class': classes[i], 'value': values[i]})
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True) 
