from PIL import Image
from io import BytesIO
import os

def combine_images_to_pdf(img1_path, img2_path, pdf_path):
    # Open the first image
    img1 = Image.open(img1_path)
    # Open the second image
    img2 = Image.open(img2_path)
    # Create a new image that is the width of both images and the height of the taller image
    new_img = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
    # Paste the first image into the new image
    new_img.paste(img1, (0, 0))
    # Paste the second image into the new image
    new_img.paste(img2, (img1.width, 0))
    # Create a BytesIO object to save the PDF to
    pdf_buffer = BytesIO()
    # Save the new image as a PDF
    new_img.save(pdf_buffer, format='PDF')
    # Seek the buffer to the beginning
    pdf_buffer.seek(0)
    # Open the PDF file for writing
    with open(pdf_path, 'wb') as pdf_file:
        # Write the buffer to the file
        pdf_file.write(pdf_buffer.read())
    # Close the buffer
    pdf_buffer.close()
    print(f"The PDF file was saved to {pdf_path}")

# usage example
combine_images_to_pdf("image1.jpg", "image2.jpg", "combined_images.pdf")
