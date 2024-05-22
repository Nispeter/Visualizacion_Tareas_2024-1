from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_png_to_pdf(png_file, pdf_file):
    # Open the image using Pillow
    image = Image.open(png_file)
    
    # Create a canvas object from reportlab
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    
    # Resize the image to fit the full width of the page and adjust height proportionally
    image_width, image_height = image.size
    aspect_ratio = image_width / image_height
    
    new_width = width
    new_height = width / aspect_ratio
    
    # If the new height exceeds the page height, adjust the page size
    if new_height > height:
        height = new_height
        c.setPageSize((width, height))
    
    # Center the image on the page
    x = 0
    y = (height - new_height) / 2

    # Draw the image on the canvas
    c.drawImage(png_file, x, y, new_width, new_height)
    c.showPage()
    c.save()
# Example usage
png_file = 'Tarea2.png'
pdf_file = 'Tarea2.pdf'
convert_png_to_pdf(png_file, pdf_file)
