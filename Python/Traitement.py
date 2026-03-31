#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

def Traitement(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contours,-1,(0,255,0),2)

