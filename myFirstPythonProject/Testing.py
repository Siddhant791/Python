from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def embed_link(output_pdf, link_text, link_url):
    # Create a canvas
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Define the clickable area
    x = 50
    y = 750
    width = 200
    height = 20

    # Draw the link text
    c.drawString(x, y, link_text)

    # Define the clickable region
    c.linkURL(link_url, (x, y, x + width, y + height), thickness=1, color=(0, 0, 1))

    # Save the PDF
    c.save()

# Example usage
output_pdf = 'output.pdf'  # Output PDF file with embedded link
link_text = 'Click here to visit Google Maps'  # Text to display for the link
link_url = 'https://www.google.com/maps'  # URL to link to


# Example usage
# input_pdf = 'Invitation_card.pdf'  # Input PDF file
# output_pdf = 'output.pdf'  # Output PDF file with embedded link
# link_text = 'Click here to visit Google Maps'  # Text to display for the link
# link_url = 'https://www.google.com/maps'  # URL to link to

if __name__ == '__main__':
    print('Hello')
    embed_link(output_pdf, link_text, link_url)