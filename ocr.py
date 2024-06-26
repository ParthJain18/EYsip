from PIL import Image
import pytesseract
import cv2
from PIL import Image

def preprocess_image_for_ocr(image_path: str) -> Image:
    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.GaussianBlur(image, (5, 5), 0)

    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    image = Image.fromarray(image)

    return image


def extract_text_from_image(image, config: str = "",lang_code: str = "eng") -> str:

    # with Image.open(image_path) as img:
    text = pytesseract.image_to_string(image, lang= lang_code, config=config)

    print(text)

    return text

if __name__ == '__main__':
    # extract_text_from_image('main\\debug.jpg', 'eng')
    pass