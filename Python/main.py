#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#fichier : main.py

import cv2 #On importe OpenCV(cv2)
import Traitement as t
import mesures as m
import optique as o



ratio_px_mm = -1
ratio_mm_px = -1
i=0
perimetre,aire,largeur,hauteur = (0,0,0,0)

cap= cv2.VideoCapture(0) #On crée une variable cap qui récupère le flux video.

while True: #On initie une boucle qui permet d'afficher chaque frame du flux vidéo. 
    key = cv2.waitKey(1)

    ret,frame=cap.read()
    ''' On crée une variable ret (booléen) qui renvoie True si cap enregistre un flux vidéo et une variable frame (numpy.ndarray) qui stocke l'information du flux vidéo. '''

    if not ret: break  #On arrête la boucle si la variable ret vaut false. 
    
    
    contours = t.traitement(frame)
    
    if ratio_px_mm == -1:
        cv2.putText(frame, "Appuyer sur 'c' pour calibrer la camera",(40, 225),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
        if key == ord("c"):
            ratio_px_mm , ratio_mm_px = o.calibration(frame)
    else :
        if key & 0xFF == ord(" "):
            i+=1
        
            contours = t.traitement(frame)
            perimetre,aire,largeur,hauteur = m.mesures(contours)
            print(f"Mesure {i} : \nPerimetre  : {perimetre*ratio_mm_px:.2f} mm\nAire       : {aire*ratio_mm_px**2:.2f} mm2\nDimensions : {largeur*ratio_mm_px:.2f}x{hauteur*ratio_mm_px:.2f} mm")
        cv2.putText(frame, "Appuyer sur espace pour prendre une mesure",(40, 200),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            
            
    cv2.putText(frame, f"Perimetre  : {perimetre*ratio_mm_px:.2f} mm",(40, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
    cv2.putText(frame, f"Aire       : {aire*ratio_mm_px**2:.2f} mm2",(40, 65),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
    cv2.putText(frame, f"Dimensions : {largeur*ratio_mm_px:.2f}x{hauteur*ratio_mm_px:.2f} mm",(40, 90),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
    cv2.imshow('1',frame)  # On affiche l'image contenue dans frame dans une nouvelle fenêtre nommée "1" 
    

    if key & 0xFF == ord('q'): break # On arrête la boucle si la touche "q" est pressée 


cap.release() # la variable cap abandonne le contrôle de la camera pour ne pas bloquer les autres programmes 
cv2.destroyAllWindows() # On ferme toutes les fenêtres ouvertes par le programme 
