#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#fichier : mesures.py

import numpy as np
from numba import njit

"""Mesure du périmètre d'un contour """
def perimetre(contour):    
    pts = contour.reshape(-1, 2)
    diff = pts - np.roll(pts, -1, axis=0)
    distances = np.sqrt((diff**2).sum(axis=1))
    p = distances.sum()
    return p


def aire(contour):  
    pts = contour.reshape(-1, 2)
    x = pts[:, 0]
    y = pts[:, 1]
    a = 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
    return a

@njit
def dimensions(contour):
    pts = contour.reshape(-1, 2).astype(np.float64)

    x_min, y_min = pts.min(axis=0)
    x_max, y_max = pts.max(axis=0)
    aire = (x_max - x_min) * (y_max - y_min)
    dims = (x_max - x_min, y_max - y_min)

    rad = np.pi / 180
    c = np.cos(rad)
    s = np.sin(rad)
    
    for _ in range(360):
        for i in range(len(pts)):
            x, y = pts[i]
            pts[i][0] = x * c - y * s
            pts[i][1] = x * s + y * c

        x_min, y_min = pts.min(axis=0)
        x_max, y_max = pts.max(axis=0)
        largeur = x_max - x_min
        hauteur = y_max - y_min
        aire2 = largeur * hauteur

        if aire2 < aire:
            aire = aire2
            dims = (largeur, hauteur)

    return dims


def mesures(contours):
    """On prend le contour le plus grand :"""
    contour=max(contours, key=perimetre)
    p = perimetre(contour)
    a = aire(contour)
    d = dimensions(contour)
    return float(p),float(a),float(d[0]),float(d[1])
