from flask import Flask, request
import os
import csv

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    csv_file = request.files['csvFile']
    if csv_file:
        csv_filename = csv_file.filename
        csv_file.save(csv_filename)
        
        lst_filename = os.path.splitext(csv_filename)[0] + '.lst'
        
        with open(csv_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            with open(lst_filename, 'w') as lst_file:
                for row in reader:
                    lst_file.write(','.join(row) + '\n')
        
        os.remove(csv_filename)  # Remove the uploaded CSV file after conversion
        
        return 'Conversion Completed!'
    else:
        return 'Error: No file provided.'

if __name__ == '__main__':
    app.run(debug=True)
