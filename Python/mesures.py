import cv2 

"""Mesure du pérmiètre de l'objet"""
def perimetre(contours):
    for contour in contours :
        p = cv2.arcLength(contour, True)
        if p > 100:    
            return p
