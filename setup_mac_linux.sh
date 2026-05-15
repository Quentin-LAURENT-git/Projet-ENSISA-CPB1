#!/bin/bash
python3 -m venv venv_Projet_CPB1_ENSISA
source venv_Projet_CPB1_ENSISA/bin/activate
pip install --upgrade pip
pip install numpy opencv-python numba spyder
echo "Environnement prêt."
echo "Pour lancer le projet : source venv_Projet_CPB1_ENSISA/bin/activate && spyder"
