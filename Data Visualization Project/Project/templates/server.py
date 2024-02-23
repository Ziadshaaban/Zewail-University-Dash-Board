from flask import Flask, jsonify, render_template
import pandas as pd


df = pd.read_csv("templates//university_dataset.csv")

app = Flask(__name__ , template_folder='../templates',static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_datachart')
def get_datachart():
    classes = df["School"].value_counts().index
    values = df["School"].value_counts().values

    data = []
    
    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})
        
    return jsonify(data)

@app.route('/get_datachart2')
def get_datachart2():
    classes = df["Program"].value_counts().index
    values = df["Program"].value_counts().values

    data = []
    
    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})
        
    return jsonify(data)


@app.route('/get_datachart3')
def get_datachart3():
    classes = df["School"].value_counts().index
    values = df["School"].value_counts().values

    data = []
    
    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})
        
    return jsonify(data)


@app.route('/get_datachart4')
def get_datachart4():
    classes = df["Program"].value_counts().index
    values = df["Program"].value_counts().values

    data = []
    
    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})
        
    return jsonify(data)


@app.route('/get_datachart5')
def get_datachart5():
    classes = df["Program"].value_counts().index
    values = df.groupby("Program")["GPA"].mean().values

    data = []
    for i in range(len(classes)):
        data.append({"class": classes[i], "value": round(values[i], 2)})
        
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True) 
