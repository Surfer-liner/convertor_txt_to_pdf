from pathlib import Path
from reportlab.pdfgen import canvas
# Find path to desktop
desktop_path = str(Path.home() / 'Desktop')
# ==============================================================================
# Enter here .txt filename on desktop
input_txt = 'test.txt'
# ==============================================================================
# Create PDF file on Desktop
pdf = canvas.Canvas(desktop_path + '/output.pdf')
# Starting text coordinates for A4 format
y = 780
x = 60
# String length
length = 90
# Set font
pdf.setFont("Helvetica", 10)
# ==============================================================================

# Open and save content in variable
with open(desktop_path + '/' + input_txt, 'r') as f:
    txt_file_content = f.readlines()

# Add content in PDF file
for string_inside in txt_file_content:
    index = 0
    if len(string_inside) >= length:
        strings_in_string_inside = round(len(string_inside) / length)
        for string in range(int(strings_in_string_inside)):
            string_to_print = string_inside[index:index + length]
            pdf.drawString(x, y, string_to_print.rstrip('\n'))
            index += length
            y -= 13
    elif len(string_inside) < length:
        pdf.drawString(x, y, string_inside[:-1])
        y -= 13
pdf.save()
