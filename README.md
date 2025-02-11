# 🖥️ Détection d'Objets avec YOLOv11 en Temps Réel

Ce projet implémente un système de **détection d'objets** à l'aide du modèle **YOLOv11** en capturant l'écran en temps réel et en affichant les objets détectés dans une fenêtre OpenCV.

## 📌 Fonctionnalités
- 📸 **Capture d'écran en temps réel** à l'aide de `mss`
- 🧠 **Détection d'objets avec YOLOv11**
- 🎯 **Affichage des résultats avec OpenCV**
- 🚀 **Exclusion de la fenêtre OpenCV pour éviter la duplication infinie**

## ⚠️ **Problème Actuel**
Le projet rencontre un **bug d'affichage** :
- ❌ **Duplication infinie de la fenêtre OpenCV**, causée par la capture d'écran qui inclut la fenêtre elle-même.
- 🔁 Tentative de correction en **masquant la zone de la fenêtre OpenCV**, mais le problème persiste partiellement.
- 🖥️ Certains systèmes Windows ne détectent pas correctement la fenêtre OpenCV (`win32gui.GetWindowRect(hwnd)`).

## 🛠️ **Installation**
### **1️⃣ Installer les dépendances**
Assurez-vous d'avoir **Python 3.11+** installé, puis exécutez :
```sh
pip install ultralytics opencv-python numpy mss pywin32
```