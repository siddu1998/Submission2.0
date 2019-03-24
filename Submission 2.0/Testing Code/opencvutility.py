import cv2
import piexif
from PIL import Image




def morphology(black_white, kernel):
    closing = cv2.morphologyEx(black_white, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    return opening


def extract_contours(black_white):
    black_white, contours, h = cv2.findContours(
        black_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    return contours



