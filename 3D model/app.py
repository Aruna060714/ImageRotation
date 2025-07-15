import cv2
import numpy as np
from PIL import Image
import os
import requests
from io import BytesIO
import shutil
image_url = r"C:\Users\Arunakaliyappan\Downloads\bottle.png"
img = Image.open(image_url).convert("RGB")
img = np.array(img)
height, width, _ = img.shape
os.makedirs("frames", exist_ok=True)
num_frames = 36
for i in range(num_frames):
    angle = i * (360 / num_frames)
    M = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)
    rotated = cv2.warpAffine(img, M, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))
    output_path = f"frames/frame_{i:02d}.png"
    Image.fromarray(rotated).save(output_path)
shutil.make_archive("rotated_frames", 'zip', "frames")
print(" Zipped into rotated_frames.zip")