import cv2
import numpy as np
import mss
import win32gui
import win32con
import win32api
from ultralytics import YOLO

# Charger le modèle YOLO
model = YOLO('yolo11n.pt')  # Vérifie que le modèle YOLO 11 est bien disponible

# Initialiser la capture d'écran
sct = mss.mss()

# Définir la zone de l'écran à capturer
mon = sct.monitors[1]  # Capture tout l'écran

# Créer la fenêtre OpenCV
cv2.namedWindow('YOLOv11 Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('YOLOv11 Detection', 1280, 720)  # Agrandir la fenêtre

# Attendre que la fenêtre soit bien ouverte
cv2.waitKey(500)

# Récupérer le handle de la fenêtre OpenCV
hwnd = win32gui.FindWindow(None, "YOLOv11 Detection")

while True:
    # Récupérer la position et la taille de la fenêtre OpenCV
    rect = win32gui.GetWindowRect(hwnd)
    x1, y1, x2, y2 = rect  # Coordonnées de la fenêtre OpenCV

    # Capturer l'écran
    sct_img = sct.grab(mon)
    img = np.array(sct_img)

    # Convertir en RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    # MASQUER la zone où se trouve la fenêtre OpenCV pour éviter la duplication infinie
    img_rgb[y1:y2, x1:x2] = (0, 0, 0)  # Remplace par du noir

    # Appliquer YOLO pour la détection
    results = model(img_rgb)

    # Annoter l'image avec les résultats
    annotated_frame = results[0].plot()

    # Afficher uniquement la fenêtre OpenCV sans être capturée
    cv2.imshow('YOLOv11 Detection', annotated_frame)

    # Vérifier si 'q' est pressé ou si la fenêtre est fermée
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('YOLOv11 Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

# Fermer correctement la fenêtre
cv2.destroyAllWindows()
