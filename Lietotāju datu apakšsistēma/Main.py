import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Nikolajs Kushnarjovs'))

import mysql
from db_utils import pievienoties_db
from Rekina_Pievienosana import pievienot_rekinu
from Rekina_Redigesana import rediget_rekinu
from Rekina_Dzesana import RekinaDzesana
from Rekinu_Apskate import RekinuApskate
from Rekinu_Filtresana import filtre_rekinus
from Rekinu_Meklesana import RekinuMeklesana


class komunalo_maksu_kalkulators:

    def paradit_lietotaja_paneli(lietotajs):

        '''
        Funkcija paradit_lietotaja_paneli pieņem dict tipa
        vērtību lietotajs un neatgriež vērtību
        '''
        

        print("\n=== SVEICIENI! ===")


        vards = lietotajs.get("vards", "")
        uzvards = lietotajs.get("uzvards", "")
        loma = lietotajs.get("loma", "")


        print(f"Sveicināti, {vards} {uzvards}")
        print(f"Jūs esat pieslēdzies kā: {loma}")


        print("\n=== GALVENĀ IZVĒLNE ===")
        print("1. Pievienot rēķinu")
        print("2. Rediģēt rēķinu")
        print("3. Dzēst rēķinu")
        print("4. Apskatīt rēķinus")
        print("5. Filtrēt rēķinus")
        print("6. Meklēt rēķinus")
        print("7. Izrakstīties")


        izvele = input("Izvēlieties darbību: ").strip()


        if izvele == "1":
            pievienot_rekinu()


        elif izvele == "2":
            rediget_rekinu()


        elif izvele == "3":
            RekinaDzesana()
        elif izvele == "4":
            RekinuApskate()
        elif izvele == "5":
            filtre_rekinus()
        elif izvele == "6":
            RekinuMeklesana()


        elif izvele == "7":
            print("\nIzrakstīšanās...")
            


        else:
            print("Kļūda: ievadiet skaitli no 1 līdz 7.")