#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#fichier : optique.py

import cv2 
import numpy as np
import Traitement as t 
import mesures as m

"""def caliration(frame):
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

    
    print(f"Longueur en pixels : {length_pixels} px")
    print(f"Longueur reelle : {longueur_reele_mm} mm")
    print(f"Ratio pixel par mm : {ratio_px_par_mm} px/mm")
    print(f"Ratio mm par pixel : {ratio_mm_par_px} mm/px")
    
    return float(ratio_px_par_mm), float(ratio_mm_par_px)"""

def calibration(frame):
    longueur_reele_mm = float(input("Longueur reelle de l'objet de calibration (mm) : "))

    contours = t.traitement(frame)
    if not contours:
        print("Aucun contour détecté")
        return -1, -1

    contour = max(contours, key=lambda c: m.aire(c))
    largeur_px, hauteur_px = m.dimensions(contour)
    longueur_px = max(largeur_px, hauteur_px)

    ratio_px_par_mm = longueur_px / longueur_reele_mm
    ratio_mm_par_px = longueur_reele_mm / longueur_px

    print(f"Longueur en pixels : {longueur_px:.1f} px")
    print(f"Ratio : {ratio_px_par_mm:.3f} px/mm")

    return float(ratio_px_par_mm), float(ratio_mm_par_px)