import qrcode

print("=" * 40)
print("      QR CODE GENERATOR")
print("=" * 40)

data = input("Enter text or URL: ").strip()

if not data:
    print("Error: Input cannot be empty.")
    exit()

filename = input("Enter output filename (without .png): ").strip()

if not filename:
    filename = "qrcode"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(f"{filename}.png")

print(f"\nQR code saved as {filename}.png")
