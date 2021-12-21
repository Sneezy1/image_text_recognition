import pandas as pd
import os
from flask import Flask, request, render_template
from model import make_recognition

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image-text-recognition',methods=['POST'])
def predict():
	if 'file1' not in request.files:
            return 'there is no file1 in form!'
	file1 = request.files['file1']
	path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
	file1.save(path)
	result = make_recognition(path)
	
	return render_template('index.html', result_text='Recognized text:{}\n'.format(result))


if __name__ == "__main__":
    app.run(debug=True)
