from flask import Flask, request, render_template
import os
import csv

app = Flask(__name__, template_folder="baller")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    csv_file = request.files['csvFile']
    if csv_file:
        csv_filename = csv_file.filename
        csv_file.save(csv_filename)
        
        lst_filename = os.path.splitext(csv_filename)[0] + '.lst'
        csv_directory = os.path.dirname(os.path.abspath(csv_filename))  # Extract directory path
        
        with open(csv_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            with open(os.path.join(csv_directory, lst_filename), 'w') as lst_file:  # Save .lst file in the same directory
                for row in reader:
                    lst_file.write(','.join(row) + '\n')
                
        return 'Conversion Completed! The .lst file should appear in the same location as your .csv file.'
    else:
        return 'Error: No file provided.'

if __name__ == '__main__':
    app.run(port=8000,debug=False)
