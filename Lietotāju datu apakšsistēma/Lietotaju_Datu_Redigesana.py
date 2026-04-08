from Datu_validacija import parbaudit_skaitli, parbaudit_tuksu_lauku, parbaudit_epastu
import mysql.connector

class Lietotaja_Datu_Redigesana:
    def rediget_profilu():

      """
      Funkcija pieņem Null tipa vērtību. Šī funkcija tiek palaista kad galvenajā izvēlnē lietotājs izvēlās opciju "Rediģēt personas datus"
      """

      print("\nKuru lauku velāties mainīt?")

      print("1. Vārds")
      print("2. Uzvārds")
      print("3. Personas kods")
      print("4. Adrese")
      print("5. Dzīvokļa numurs")
      

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

      


      
      