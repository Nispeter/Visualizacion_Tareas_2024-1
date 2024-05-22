import pdfkit
import pyppeteer

# Path to the HTML file
html_file = 'Tarea2.html'

# Path to save the PDF file
pdf_file = 'Tarea2.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file, options={
    'enable-local-file-access': None
})