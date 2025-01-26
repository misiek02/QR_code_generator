import qrcode
import os

# URL address
data = "https://modnesciany.pl"

# QR code generating
qr = qrcode.QRCode(
    version=1,  # QR size [1-40]
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Correction level (L, M, Q, H)
    box_size=10,  # Single square size
    border=4,  # Border size
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

def save_qr(img, base_name="qr"):
    counter = 1
    while True:
        file_name = f"{base_name}#{counter}.png"
        if not os.path.exists(file_name):
            break
        counter += 1

    img.save(file_name)
    print(f"QR saved as '{file_name}'.")

save_qr(img)
