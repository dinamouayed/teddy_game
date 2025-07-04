# 🎮 Teddy Game

**Teddy Game** est un petit jeu 2D créé pour le **Pic'Asso**, qui reprend plusieurs références emblématiques de notre foyer :
- Le logo **Pic'Asso** en arrière-plan
- **Teddy** comme joueur principal
- Les **écocups** comme projectiles
- Les **bières Filou** en adversaires
- **Une amie et moi-même** au Pic en adversaires
- Les fameux **poufs** du Pic

L'**objectif du jeu** est d'éliminer les adversaires arrivant depuis la gauche et la droite, et d'éviter les pluies de poufs.

---

## 🛠️ Installation

Avant de lancer le jeu, vous devez avoir **Python** installé sur votre machine.  
Ensuite, ouvrez un terminal et installez la librairie **pygame** :
```
pip install pygame
```

---

## 🚀 Lancement du jeu

Dans votre terminal, placez-vous dans le dossier contenant le projet puis lancez le fichier `main.py` :
```
python main.py
```

---

## 🎮 Contrôles

- **Flèche gauche** : déplacer Teddy vers la gauche
- **Flèche droite** : déplacer Teddy vers la droite
- **Touche Q** : lancer un projectile (écocup) vers la gauche
- **Touche D** : lancer un projectile vers la droite

---

## ⚙️ Réglage de la vitesse

Si le jeu est trop rapide ou trop lent, vous pouvez ajuster le **framerate** en modifiant cette ligne dans `main.py` :

```python
clock.tick(60)
Par exemple :

clock.tick(30) pour ralentir le jeu
clock.tick(120) pour accélérer le jeu
```

Amusez-vous bien ! 🍻✨