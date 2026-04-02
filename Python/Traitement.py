#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

def Traitement(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    binary = cv2.Canny(blur, 100, 200)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    filtre =[]
    
    for contour in contours:
        
        if cv2.contourArea(contour) > 1000 :
            filtre.append(contour)
            
    cv2.drawContours(frame,filtre,-1,(0,255,0),cv2.FILLED)
    return filtre

