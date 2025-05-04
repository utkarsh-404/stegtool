import cv2
import numpy as np
import os

def encode_lsb(image_path, message, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unsupported format.")

    # Convert the message to binary
    message += "###END###"
    binary_message = ''.join([format(ord(char), '08b') for char in message])

    # Flatten the image array
    flat_image = image.flatten()

    if len(binary_message) > len(flat_image):
        raise ValueError("Message is too long to hide in this image.")

    # Encode the message bit by bit
    for i in range(len(binary_message)):
        flat_image[i] = (flat_image[i] & ~1) | int(binary_message[i])

    # Reshape the image
    encoded_image = flat_image.reshape(image.shape)

    # Save the encoded image
    cv2.imwrite(output_path, encoded_image)
    print(f"Message encoded successfully into {output_path}")

def decode_lsb(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unsupported format.")

    flat_image = image.flatten()

    binary_message = ''
    for i in range(len(flat_image)):
        binary_message += str(flat_image[i] & 1)

    # Convert binary to string
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    for byte in chars:
        char = chr(int(byte, 2))
        message += char
        if message.endswith("###END###"):
            break

    return message.replace("###END###", "")


# Example usage:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Custom LSB Steganography")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose encode or decode")
    parser.add_argument("-i", "--input", help="Path to input image")
    parser.add_argument("-o", "--output", help="Path to save encoded image")
    parser.add_argument("-m", "--message", help="Message to hide")

    args = parser.parse_args()

    if args.mode == "encode":
        if not args.input or not args.output or not args.message:
            parser.error("Encoding requires -i, -o, and -m arguments.")
        encode_lsb(args.input, args.message, args.output)

    elif args.mode == "decode":
        if not args.input:
            parser.error("Decoding requires -i argument.")
        hidden_message = decode_lsb(args.input)
        print("Decoded message:", hidden_message)
