import subprocess
import os
import sys
bakkesmod_path = r"C:\Program Files\BakkesMod\BakkesMod.exe"
rl_path = r"D:\RL\rocketleague\Binaries\Win64\RocketLeague.exe"
def lancer_programme(chemin):
    try:
        if os.path.exists(chemin):
            subprocess.Popen(chemin)
            print(f"{os.path.basename(chemin)} lancé avec succès.")
        else:
            print(f"❌ Fichier introuvable : {chemin}")
    except Exception as e:
        print(f"⚠️ Erreur lors du lancement de {chemin} : {e}")
print("=== Lancement des programmes ===")
lancer_programme(bakkesmod_path)
lancer_programme(rl_path)
