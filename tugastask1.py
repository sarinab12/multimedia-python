import pygame
import PIL
import cv2
import moviepy.editor as mp
import tkinter as tk
import pkg_resources

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:",pkg_resources.get_distribution("moviepy").version)
    print("✅ MoviePy version:",pkg_resources.get_distribution("pydub").version)
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()