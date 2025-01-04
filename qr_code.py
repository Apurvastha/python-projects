import qrcode

# Ask the user for the data to be converted into a QR code
data = input("Enter your link here: ")

# Ask the user for the output file name
file_name = input("Save as: ") + '.png'

# Create a QRCode object with specified parameters
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color='black', back_color='white')

# Save the QR code image
try:
    img.save(file_name)
    print(f"QR code saved as {file_name}")
except Exception as e:
    print(f"An error occurred while saving the QR code: {e}")