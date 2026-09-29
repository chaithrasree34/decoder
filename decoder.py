# decoder
import base64

encoded_text = input("Enter encoded text: ")

decoded_text = base64.b64decode(encoded_text).decode("utf-8")

print("Decoded text:", decoded_text)
