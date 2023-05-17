from pathlib import Path
from reportlab.pdfgen import canvas

# Find path to desktop
desktop_path = str(Path.home() / 'Desktop')
# ==============================================================================
# Enter here .txt filename on desktop
input_txt = 'test.txt'
# ==============================================================================
pdf = canvas.Canvas(desktop_path + '/output.pdf')


with open(desktop_path + '/' + input_txt, 'r') as f:
    txt_file_content = f.readlines()







y = 780
x = 40
for el in range(1, 3):
    text = 'DO it'
    pdf.drawString(0 + x, 0 + y, text)
    y += 13
pdf.save()