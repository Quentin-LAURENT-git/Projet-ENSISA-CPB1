import cv2 #On importe OpenCV(cv2)
import Traitement as t
import mesures as m


cap= cv2.VideoCapture(2) #On crée une variable cap qui récupère le flux video.
while True: #On initie une boucle qui permet d'afficher chaque frame du flux vidéo. 

    ret,frame=cap.read() 
    ''' On crée une variable ret (booléen) qui renvoie True si cap enregistre un flux vidéo et une variable frame (numpy.ndarray) qui stocke l'information du flux vidéo. '''

    if not ret: break  #On arrête la boucle si la variable ret vaut false. 
    
    contours = t.Traitement(frame)
    perimetre = m.perimetre(contours)
    cv2.putText(frame, f"Perimetre : {perimetre:.0f}px", (40,40), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0,255,0),1)
    
    cv2.imshow('1',frame)  # On affiche l'image contenue dans frame dans une nouvelle fenêtre nommée "1" 

    if cv2.waitKey(1) & 0xFF == ord('q'): break # On arrête la boucle si la touche "q" est pressée 


cap.release() # la variable cap abandonne le contrôle de la camera pour ne pas bloquer les autres programmes 
cv2.destroyAllWindows() # On ferme toutes les fenêtres ouvertes par le programme 