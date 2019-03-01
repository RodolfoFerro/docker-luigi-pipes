from PIL import Image
import numpy as np
import pytesseract
import argparse
import cv2


def load_images(img_path):
    """Load images from arguments."""

    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image, gray


def preprocess(preprocess_tag, gray):
    """Apply preprocess to input image."""

    if preprocess_tag == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess_tag == "blur":
        gray = cv2.medianBlur(gray, 3)

    elif preprocess_tag == "morph":
        kernel = np.ones((5, 5), np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
        gray = cv2.dilate(gray, kernel, iterations=1)
        gray = cv2.erode(gray, kernel, iterations=1)

    return gray


def parser():
    """We build our parser."""

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="Path to input image to be OCR'd.")
    ap.add_argument("-p", "--preprocess", type=str, default="morph",
                    help="Type of preprocessing to be done.")
    args = vars(ap.parse_args())

    return args


def apply_OCR(image):
    """Apply OCR to text."""

    # Save grayscale image to disk for OCR:
    filename = "../assets/preprocessed_image.png"
    cv2.imwrite(filename, image)

    # Load as a PIL/Pillow image and apply OCR:
    text = pytesseract.image_to_string(Image.open(filename))

    return text


if __name__ == '__main__':
    # We parse input from terminal:
    args = parser()

    # Load images from arguments:
    image, gray = load_images(args["image"])

    # Apply preprocess to input image:
    gray = preprocess(args["preprocess"], gray)

    # We apply OCR:
    text = apply_OCR(gray)

    # Print extracted text:
    print(text)
