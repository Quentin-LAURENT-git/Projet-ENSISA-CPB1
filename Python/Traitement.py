#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

"""On définit un filtre de Sobel pour remplacer cv2.Canny"""

def Sobel(gray,seuil):
    
    
    """Filtre de Sobel en parcourant chaque pixel de l'image
    
    On définit les noyaux de Sobel suivant x et y
    Nx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Ny = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    h,l = gray.shape
    On définit l'algorithme de convolution d'une matrice par les matrices noyaux de Sobel 
    Gx = np.zeros((h, l), dtype=np.float32)
    Gy = np.zeros((h, l), dtype=np.float32)
    
    On rajoute des pixels de valeur 0 autour de l'image
    gray = np.pad(gray, pad_width=1 , mode='constant',constant_values=0)
    for i in range(h):
        for j in range(l):
            region=gray[i:i+3,j:j+3].astype(np.float32)
            Gx[i,j]= np.sum(region*Nx)
            Gy[i,j]= np.sum(region*Ny)"""
            
            
    """On fait une convolution vectorielle sans boucle pour réduire la complexité de l'algorithme"""
       
    g = gray.astype(np.float32)
    Gx = (  -g[:-2, :-2] + g[:-2, 2:]
           - 2*g[1:-1, :-2] + 2*g[1:-1, 2:]
           -   g[2:,  :-2] + g[2:,  2:] )
    Gy = (  -g[:-2, :-2] - 2*g[:-2, 1:-1] - g[:-2, 2:]
           +  g[2:,  :-2] + 2*g[2:,  1:-1] + g[2:,  2:] )
    G = np.sqrt(Gx**2+Gy**2)
    G = (G / G.max() * 255).astype(np.uint8)
    
    binary = (G > seuil).astype(np.uint8) * 255

    return binary

def contours(binary):
    #À Compléter
    """Retourne les contours extérieurs de tous les objets de l'image sous la forme d'une liste de contours"""
    return
    
    
def traitement(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary = Sobel(gray, 50)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    filtre =[]
    
    for contour in contours:
        
        if cv2.contourArea(contour) > 1000 :
            filtre.append(contour)
            
    cv2.drawContours(frame,filtre,-1,(0,255,0),cv2.FILLED)
    return filtre
    #return binary

