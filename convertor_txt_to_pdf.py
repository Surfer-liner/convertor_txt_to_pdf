import os
from io import BytesIO
from pathlib import Path
from reportlab.pdfgen import canvas


def convert_txt_to_pdf(input_file):
    '''Simple convertor from .txt to .pdf'''
    try:
        # Find path to desktop
        desktop_path = str(Path.home() / 'Desktop')
        # Path to .ttx file if it is on the desktop
        path_to_input_file = desktop_path + '/' + input_file
        # Create buffer
        buffer = BytesIO()
        # Create PDF Canvas
        pdf = canvas.Canvas(buffer)
        # Open .txt file and read content
        with open(path_to_input_file, 'r') as f:
            txt_file_content = f.read()
        # Add text to PDF Canvas
        pdf.drawString(50, 780, txt_file_content)
        # Close and save PDF Canvas
        pdf.save()
        # Create path to new PDF
        path_to_output_pdf = os.path.join(desktop_path, 'output.pdf')
        # Save PDF file to desktop
        with open(path_to_output_pdf, 'wb') as f:
            f.write(buffer.getvalue())
    except FileNotFoundError:
        print(f'File <{input_file}> not found\nCheck file name and try again')


# Enter here .txt filename on desktop
convert_txt_to_pdf('test.txt')