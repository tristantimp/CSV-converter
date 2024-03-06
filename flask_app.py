from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = file.filename
        if filename.endswith('.csv'):
            csv_data = file.read().decode('utf-8')
            csv_list = list(csv.reader(csv_data.splitlines()))
            lst_filename = filename[:-4] + '.lst'

            with open(lst_filename, 'w') as lst_file:
                for row in csv_list:
                    lst_file.write('\t'.join(row) + '\n')

            return send_file(lst_filename, as_attachment=True)
        else:
            return render_template('error.html', message='Uploaded file is not a CSV file.')

if __name__ == '__main__':
    app.run(port=8000,debug=True)
