import qrcode


def generate_qr_code(url, file_name="qrcode.png"):
    """Generate and save a QR code for the provided URL."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    qr_image.save(file_name)
    print(f"QR code generated successfully: {file_name}")

    # Open the generated QR code image
    qr_image.show()


def main():
    print("AI QR Code Generator")
    print("--------------------")

    url = input("Enter a URL: ").strip()

    if url:
        generate_qr_code(url)
    else:
        print("Please enter a valid URL.")


if __name__ == "__main__":
    main()