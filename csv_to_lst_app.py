import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

entry_csv = None  # Define entry_csv as a global variable

def csv_to_lst(csv_file):
    lst_file = os.path.splitext(csv_file)[0] + '.lst'
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open(lst_file, 'w') as lst_file:
            for row in reader:
                lst_file.write(','.join(row) + '\n')
    
    messagebox.showinfo('Conversion Complete', 'CSV to LST conversion is complete.')

def open_csv():
    csv_file = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if csv_file:
        entry_csv.delete(0, tk.END)
        entry_csv.insert(tk.END, csv_file)

def convert():
    csv_file = entry_csv.get()
    
    if csv_file:
        csv_to_lst(csv_file)
    else:
        messagebox.showwarning('File Error', 'Please select the input CSV file.')

def main():
    global entry_csv  # Add global declaration
    
    # Create the main window
    window = tk.Tk()
    window.title('CSV to LST Converter')

    # Create the input CSV file section
    frame_csv = tk.Frame(window)
    frame_csv.pack(pady=10)

    label_csv = tk.Label(frame_csv, text='Input CSV File:')
    label_csv.pack(side=tk.LEFT)

    entry_csv = tk.Entry(frame_csv, width=50)
    entry_csv.pack(side=tk.LEFT)

    button_open_csv = tk.Button(frame_csv, text='Open', command=open_csv)
    button_open_csv.pack(side=tk.LEFT, padx=(10, 0))

    # Create the convert button
    button_convert = tk.Button(window, text='Convert', command=convert)
    button_convert.pack(pady=20)

    # Start the GUI event loop
    window.mainloop()

if __name__ == '__main__':
    main()
