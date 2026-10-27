"""Permet de lancer le jeu avec « python -m final_classe », ou le bouton ▶ de PyCharm."""
import sys

from final_classe import main

try:
    main()
except KeyboardInterrupt:
    print("Game over")