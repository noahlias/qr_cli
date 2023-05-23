import click
import cv2
import qrcode
from pyzbar import pyzbar


@click.group()
def cli():
    """The command line interface"""
    pass


@cli.command()
@click.argument("image", type=click.Path(exists=True))
def scan(image):
    """Scan QR codes in an image"""
    image = cv2.imread(image)
    qr_codes = pyzbar.decode(image)

    if qr_codes:
        for qr_code in qr_codes:
            data = qr_code.data.decode("utf-8")
            click.echo(f"QR Code Data: {data}")
    else:
        click.echo("No QR codes found in the image")


@cli.command()
@click.argument("data")
@click.argument("output", type=click.Path())
def generate(data, output):
    """Generate a QR code"""
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill="black", back_color="white")
    img.save(output)


if __name__ == "__main__":
    cli()
