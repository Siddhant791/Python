import base64
import zlib

def encode_image_with_compression(image_path, output_file="compressed_encoded_image.txt"):
    """
    Compress and encode an image into a Base64 string and save it to a file.

    Args:
        image_path (str): Path to the original image file.
        output_file (str): Path to save the compressed Base64 string.

    Returns:
        None
    """
    # Read the original image as binary data
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    # Compress the binary data using zlib
    compressed_data = zlib.compress(image_data)

    # Encode the compressed data to Base64
    base64_string = base64.b64encode(compressed_data).decode('utf-8')

    # Write the Base64 string to a file
    with open(output_file, "w") as encoded_file:
        encoded_file.write(base64_string)

    print(f"Compressed and encoded image data saved to: {output_file}")
    print(f"Original size: {len(image_data)} bytes")
    print(f"Compressed size: {len(compressed_data)} bytes")
    print(f"Encoded size: {len(base64_string)} characters")


def decode_image_with_compression(encoded_file, output_image_path):
    """
    Decode and decompress a Base64 string from a file to reconstruct the original image.

    Args:
        encoded_file (str): Path to the file containing the Base64-encoded compressed data.
        output_image_path (str): Path to save the reconstructed image.

    Returns:
        None
    """
    # Read the Base64 string from the file
    with open(encoded_file, "r") as encoded_file:
        base64_string = encoded_file.read()

    # Decode the Base64 string into compressed binary data
    compressed_data = base64.b64decode(base64_string)

    # Decompress the binary data to recover the original image data
    image_data = zlib.decompress(compressed_data)

    # Write the original image data to the output file
    with open(output_image_path, "wb") as output_file:
        output_file.write(image_data)

    print(f"Decoded and decompressed image saved to: {output_image_path}")


# Example usage
if __name__ == "__main__":
    # Path to the original image
    image_path = "Test.jpeg"

    # File to store the compressed and encoded data
    encoded_file = "compressed_encoded_image.txt"

    # Path to save the decoded image
    decoded_image_path = "decoded_image.jpg"

    # Encode the image with compression
    encode_image_with_compression(image_path, encoded_file)

    # Decode the image back to its original form
    decode_image_with_compression(encoded_file, decoded_image_path)
