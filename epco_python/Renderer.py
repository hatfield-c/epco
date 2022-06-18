
import cv2
import numpy as np

def render(img):
    
    cv2.imshow('image', img)
    cv2.waitKey(0)