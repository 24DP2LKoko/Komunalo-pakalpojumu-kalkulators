from Datu_validacija import parbaudit_skaitli, parbaudit_tuksu_lauku, parbaudit_epastu
import mysql.connector
from db_utils import pievienoties_db

class Lietotaja_Datu_Redigesana:
    def rediget_profilu_irnieks():

      """
      Funkcija pieņem Null tipa vērtību. Šī funkcija tiek palaista kad galvenajā izvēlnē lietotājs izvēlās opciju "Rediģēt personas datus"
      """

      print("\nKuru lauku vēlaties mainīt?")
      print("1. Vārds")
      print("2. Uzvārds")
      print("3. Personas kods")
      print("4. Adrese")
      print("5. Dzīvokļa numurs")

      izvele = input("Izvēlieties darbību: ").strip()
      personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu, pēc kura atrast ierakstu: "), "Personas kods")

      mydb, mycursor = pievienoties_db()

      if izvele == "1":
        vards = parbaudit_tuksu_lauku(input("Ievadiet jauno vārdu: "), "Vārds")
        sql = "UPDATE irnieki SET vards = %s WHERE personas_kods = %s"
        val = (vards, personas_kods)

      elif izvele == "2":
        uzvards = parbaudit_tuksu_lauku(input("Ievadiet jauno uzvārdu: "), "Uzvārds")
        sql = "UPDATE irnieki SET uzvards = %s WHERE personas_kods = %s"
        val = (uzvards, personas_kods)

      elif izvele == "3":
        jauns_personas_kods = parbaudit_tuksu_lauku(input("Ievadiet jauno personas kodu: "), "Personas kods")
        sql = "UPDATE irnieki SET personas_kods = %s WHERE personas_kods = %s"
        val = (jauns_personas_kods, personas_kods)

      elif izvele == "4":
        adrese = parbaudit_tuksu_lauku(input("Ievadiet jauno adresi: "), "Adrese")
        sql = "UPDATE irnieki SET adrese = %s WHERE personas_kods = %s"
        val = (adrese, personas_kods)

      elif izvele == "5":
        dzivokla_nr = parbaudit_skaitli(input("Ievadiet jauno dzīvokļa numuru: "), "Dzīvokļa numurs")
        sql = "UPDATE irnieki SET dz_nr = %s WHERE personas_kods = %s"
        val = (dzivokla_nr, personas_kods)

      else:
        print("Kļūda: ievadiet skaitli no 1 līdz 5.")
        mycursor.close()
        mydb.close()
        return

      mycursor.execute(sql, val)
      mydb.commit()
      mycursor.close()
      mydb.close()

      print("Dati ir veiksmīgi atjaunināti.")

    def rediget_profilu_ipasnieks():

      """
      Rediģē īpašnieka profilu tabulā ipasnieks.
      """

      print("\nKuru īpašnieka lauku vēlaties mainīt?")
      print("1. Vārds")
      print("2. Uzvārds")
      print("3. Personas kods")
      print("4. E-pasts")
      print("5. Pārvaldāmās mājas adrese")

      izvele = input("Izvēlieties darbību: ").strip()
      personas_kods = parbaudit_tuksu_lauku(input("Ievadiet īpašnieka personas kodu, pēc kura atrast ierakstu: "), "Personas kods")

      mydb, mycursor = pievienoties_db()

      if izvele == "1":
        vards = parbaudit_tuksu_lauku(input("Ievadiet jauno vārdu: "), "Vārds")
        sql = "UPDATE ipasnieks SET vards = %s WHERE personas_kods = %s"
        val = (vards, personas_kods)

      elif izvele == "2":
        uzvards = parbaudit_tuksu_lauku(input("Ievadiet jauno uzvārdu: "), "Uzvārds")
        sql = "UPDATE ipasnieks SET uzvards = %s WHERE personas_kods = %s"
        val = (uzvards, personas_kods)

      elif izvele == "3":
        jauns_personas_kods = parbaudit_tuksu_lauku(input("Ievadiet jauno personas kodu: "), "Personas kods")
        sql = "UPDATE ipasnieks SET personas_kods = %s WHERE personas_kods = %s"
        val = (jauns_personas_kods, personas_kods)

      elif izvele == "4":
        epasts = parbaudit_epastu(input("Ievadiet jauno e-pastu: "), "E-pasts")
        sql = "UPDATE ipasnieks SET epasts = %s WHERE personas_kods = %s"
        val = (epasts, personas_kods)

      elif izvele == "5":
        parvaldamas_adrese = parbaudit_tuksu_lauku(input("Ievadiet jauno pārvaldāmās mājas adresi: "), "Pārvaldāmās mājas adrese")
        sql = "UPDATE ipasnieks SET parvaldamas_majas_adrese = %s WHERE personas_kods = %s"
        val = (parvaldamas_adrese, personas_kods)

      else:
        print("Kļūda: ievadiet skaitli no 1 līdz 5.")
        mycursor.close()
        mydb.close()
        return

      mycursor.execute(sql, val)
      mydb.commit()
      mycursor.close()
      mydb.close()

      print("Īpašnieka dati ir veiksmīgi atjaunināti.")

    def rediget_majas_datus():

      """
      Rediģē pārvaldāmas mājas datus tabulā majas.
      """

      print("\nKuru mājas lauku vēlaties mainīt?")
      print("1. Adrese")
      print("2. Mājas numurs")
      print("3. Dzīvokļu skaits")
      print("4. Stāvu skaits")

      izvele = input("Izvēlieties darbību: ").strip()
      adrese = parbaudit_tuksu_lauku(input("Ievadiet mājas adresi, pēc kuras atrast ierakstu: "), "Adrese")
      majas_nr = parbaudit_skaitli(input("Ievadiet mājas numuru, pēc kura atrast ierakstu: "), "Mājas numurs")

      mydb, mycursor = pievienoties_db()

      if izvele == "1":
        jauna_adrese = parbaudit_tuksu_lauku(input("Ievadiet jauno adresi: "), "Adrese")
        sql = "UPDATE majas SET adrese = %s WHERE adrese = %s AND majas_nr = %s"
        val = (jauna_adrese, adrese, majas_nr)

      elif izvele == "2":
        jauns_maj_nr = parbaudit_skaitli(input("Ievadiet jauno mājas numuru: "), "Mājas numurs")
        sql = "UPDATE majas SET majas_nr = %s WHERE adrese = %s AND majas_nr = %s"
        val = (jauns_maj_nr, adrese, majas_nr)

      elif izvele == "3":
        dzivoklu_skaits = parbaudit_skaitli(input("Ievadiet jauno dzīvokļu skaitu: "), "Dzīvokļu skaits")
        sql = "UPDATE majas SET dz_sk = %s WHERE adrese = %s AND majas_nr = %s"
        val = (dzivoklu_skaits, adrese, majas_nr)

      elif izvele == "4":
        stavi = parbaudit_skaitli(input("Ievadiet jauno stāvu skaitu: "), "Stāvu skaits")
        sql = "UPDATE majas SET stavi = %s WHERE adrese = %s AND majas_nr = %s"
        val = (stavi, adrese, majas_nr)

      else:
        print("Kļūda: ievadiet skaitli no 1 līdz 4.")
        mycursor.close()
        mydb.close()
        return

      mycursor.execute(sql, val)
      mydb.commit()
      mycursor.close()
      mydb.close()

      print("Mājas dati ir veiksmīgi atjaunināti.")
      