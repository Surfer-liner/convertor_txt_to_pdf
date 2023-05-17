import sys, os
from io import BytesIO
from pathlib import Path
from reportlab.pdfgen import canvas

sys.path.append('/Users/surfer_liner/python_/projects/useful_functions')
# Find path to desktop
desktop_path = str(Path.home() / 'Desktop')

# ==============================================================================
# Enter here .txt filename on desktop
txt_filename = 'test.txt'
# ==============================================================================


def convert_txt_to_pdf(input_file):
    '''Simple convertor from .txt to .pdf'''
    try:
        # Path to .txt file if it is on the desktop
        path_to_input_file = desktop_path + '/' + txt_filename

        # Create buffer
        buffer = BytesIO()
        # Create PDF Canvas
        pdf = canvas.Canvas(buffer)
        # Open .txt file and read context

        with open(path_to_input_file, 'r') as f:
            txt_file_content = f.readlines()
            # Save context as string
            file_content = ' '.join(txt_file_content)

        # Weight of PDF page
        string_len = 87
        # Numbers of strings to PDF file
        strings = round(len(''.join(txt_file_content)) / string_len)





        # Close and save PDF Canvas
        pdf.save()
        # Create path to new PDF
        path_to_output_pdf = os.path.join(desktop_path, 'output.pdf')
        # Save PDF file to desktop
        with open(path_to_output_pdf, 'wb') as f:
            f.write(buffer.getvalue())
    except FileNotFoundError:
        print(f'File <{input_file}> not found\nCheck file name and try again')


convert_txt_to_pdf(txt_filename)
