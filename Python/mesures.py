#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

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


def dimensions(contour):
    pts = contour.reshape(-1, 2)
    x_min, y_min = pts.min(axis=0)
    x_max, y_max = pts.max(axis=0)
    largeur = x_max - x_min
    hauteur = y_max - y_min
    dims =(largeur,hauteur)
    
    return dims


def mesures(contours):
    """On prend le contour le plus grand :"""
    contour=max(contours, key=perimetre)
    p = perimetre(contour)
    a = aire(contour)
    d = dimensions(contour)
    return float(p),float(a),float(d[0]),float(d[1])