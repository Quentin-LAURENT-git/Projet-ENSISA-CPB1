#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 
import numpy as np
import Traitement as t 

def caliration(frame):
    longueur_reele_mm = float(input("Longueur reelle  : "))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary = t.Sobel(gray, 50)
    
    if np.sum(binary == 255) < np.sum(binary == 0):
        binary = cv2.bitwise_not(binary)

    kernel_size = 3
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    eroded = binary.copy()
    n_iterations = 0

    while np.any(eroded > 0):
        eroded = cv2.erode(eroded, kernel, iterations=1)
        n_iterations += 1

    half = kernel_size // 2
    length_pixels = 2 * n_iterations * half

    ratio_px_par_mm = length_pixels / longueur_reele_mm
    ratio_mm_par_px = longueur_reele_mm / length_pixels

    """
    print(f"Longueur en pixels : {length_pixels} px")
    print(f"Longueur reelle : {longueur_reele_mm} mm")
    print(f"Ratio pixel par mm : {ratio_px_par_mm} px/mm")
    print(f"Ratio mm par pixel : {ratio_mm_par_px} mm/px")"""
    
    return float(ratio_px_par_mm), float(ratio_mm_par_px)