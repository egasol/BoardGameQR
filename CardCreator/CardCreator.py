import qrcode
import textwrap
import json
from PIL import Image, ImageDraw, ImageFont

QR_VERSION = 1
QR_BOXSIZE = 6
QR_BORDER = 4
QR_SIZE = 21 + 4 * (QR_VERSION - 1)
QR_WIDTH = QR_HEIGHT = QR_BOXSIZE * (QR_SIZE + 2 * QR_BORDER)

CARD_ASPECTRATIO = 1.8
CARD_SIZE = (QR_WIDTH, int(QR_HEIGHT*CARD_ASPECTRATIO))
# CARD_BACKGROUND_COLOR = (80, 120, 80)
CARD_BACKGROUND_COLOR = (0, 0, 0)
CARD_BORDER_COLOR = (20, 100, 20)

TEXT_FONT = "futurama.ttf"
TEXT_SIZE = 18
TEXT_COLOR = (255, 255, 255)
TEXT_OFFSET = 4
TEXT_WRAP = 20


def add_qr(image, action):
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=QR_BOXSIZE,
        border=QR_BORDER
    )

    qr.add_data(action)
    qr.make(fit=True)

    image_qr = qr.make_image(fill_color="black", back_color="white")

    image.paste(image_qr, (0, 0), mask=image_qr)


def add_description(image, description):
    font = ImageFont.truetype(TEXT_FONT, TEXT_SIZE)
    text = "\n".join(textwrap.wrap(description, TEXT_WRAP))
    image_draw = ImageDraw.Draw(image)
    image_draw.text((TEXT_OFFSET, QR_HEIGHT), text, font=font, fill=TEXT_COLOR)


def save_card(image, card_data):
    filename_image = card_data["name"] + ".png"
    filename_json = card_data["name"] + ".json"

    image.save(filename_image)

    with open(filename_json, "w") as f:
        json.dump(card_data, f, indent=4)


if __name__ == "__main__":
    card_data = {}
    card_data["name"] = input("name of card:")
    card_data["action"] = input("action:")
    card_data["description"] = input("description:")

    image = Image.new("RGBA", CARD_SIZE, CARD_BACKGROUND_COLOR)

    add_qr(image, card_data["action"])
    add_description(image, card_data["description"])

    save_card(image, card_data)
