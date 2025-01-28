import base64
from PIL import Image
from io import BytesIO

def encode_image(image_path, target_size=(200,200), quality=100,output_file="encoded_data.txt"):
    """
    Encode an image into a very small data stream.

    Args:
        image_path (str): Path to the image file.
        target_size (tuple): Desired size of the image (width, height).
        quality (int): Quality of the image (1 to 100, lower means more compression).

    Returns:
        str: Base64-encoded string of the compressed image.
    """
    # Open the image
    with Image.open(image_path) as img:
        # Resize the image using LANCZOS resampling
        img = img.resize(target_size, Image.Resampling.LANCZOS)

        # Convert the image to a compressed byte stream
        byte_stream = BytesIO()
        img.save(byte_stream, format='JPEG', quality=quality)  # Compress the image
        byte_stream.seek(0)

        # Encode the byte stream to Base64
        base64_string = base64.b64encode(byte_stream.read()).decode('utf-8')
        with open(output_file, "w") as file:
            file.write(base64_string)

    return base64_string


def decode_image(base64_string, output_path):
    """
    Decode a Base64 string back into an image.

    Args:
        base64_string (str): Base64-encoded string of the image.
        output_path (str): Path to save the decoded image.

    Returns:
        None
    """
    # Decode the Base64 string into bytes
    image_data = base64.b64decode(base64_string)

    # Write the decoded bytes to an image file
    with open(output_path, 'wb') as output_file:
        output_file.write(image_data)


# Example usage
if __name__ == "__main__":
    # Encode the image
    image_path = "Test.jpeg"
    encoded_data = encode_image(image_path)
    print("Encoded Data (First 100 characters):", encoded_data[:100], "...")

    # Decode the image
    output_path = "decoded_image.jpg"
    decode_image(encoded_data, output_path)
    print(f"Decoded image saved at: {output_path}")
