from integrity.Datu_validacija import parbaudit_skaitli, parbaudit_tuksu_lauku, parbaudit_epastu
from authorisation.db_utils import pievienoties_db

class lietotaja_registracija:

  def ievadit_iedzivotaja_datus():
    
    '''
    Funkcija pieņem None tipa vērtību. Šī funkcija nostrādā kad lietotājs reģistrācijas laikā izvēlās "īrnieka" lomu. 
    No lietotāja tiek pieprasīti vairāki ievadi ar personas datiem. Kad visi dati tika ievadīti pareizi tie tiek ierakstīti datubāzē.
    '''

    mydb, mycursor = pievienoties_db()

    personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu: "), "Personas kods")
    vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
    uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
    epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")
    adrese = parbaudit_tuksu_lauku(input("Ievadiet adresi: "), "Adrese")
    dzivokla_nr = parbaudit_skaitli(input("Ievadiet dzīvokļa nr.: "), "Dzīvokļa nr.")

    sql = "INSERT INTO iedzivotaji (personas_kods, vards, uzvards, epasts, adrese, dz_nr) VALUES (%s, %s, %s, %s , %s, %s)"
    val = (personas_kods, vards, uzvards, epasts, adrese, dzivokla_nr)

    mycursor.execute(sql, val)
    mydb.commit()

    mydb.close()

    return {
    "loma": "Iedzīvotājs",
    "personas_kods": personas_kods,
    "vards": vards,
    "uzvards": uzvards,
    "epasts": epasts,
    "adrese": adrese,
    "dzivokla_nr": dzivokla_nr
  }

  def ievadit_saimnieka_datus():

    '''
    Funkcija pieņem None tipa vērtību. Šī funkcija nostrādā kad lietotājs reģistrācijas laikā izvēlās "īrnieka" lomu. 
    No lietotāja tiek pieprasīti vairāki ievadi ar personas datiem. Tad no lietotāja tiek pieprasīts ievadīt datus par māju kas tam pieder. Kad visi dati tika ievadīti pareizi tie tiek ierakstīti datubāzē.
    '''

    mydb, mycursor = pievienoties_db()

    personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu: "), "Personas kods")
    vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
    uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
    epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")

    print("\nIevadiet informāciju par pārvaldāmo māju:")

    adrese = parbaudit_tuksu_lauku(input("Adrese: "), "Adrese")
    majas_numurs = parbaudit_skaitli(input("Mājas numurs: "), "Mājas numurs")
    dzivoklu_skaits = parbaudit_skaitli(input("Dzīvokļu skaits: "), "Dzīvokļu skaits")
    stavi = parbaudit_skaitli(input("Stāvu skaits: "), "Stāvu skaits")

    sql = "INSERT INTO saimnieki (personas_kods, vards, uzvards, epasts, parvaldamas_majas_adrese) VALUES (%s, %s, %s, %s, %s)"
    val = (personas_kods, vards, uzvards, epasts, adrese)

    mycursor.execute(sql, val)

    sql = "INSERT INTO majas (adrese, majas_nr, dz_sk, stavi) VALUES (%s, %s, %s, %s)"
    val = (adrese, majas_numurs, dzivoklu_skaits, stavi)

    mycursor.execute(sql, val)
    mydb.commit()

    mydb.close()

    return {
    "loma": "Saimnieks",
    "personas_kods": personas_kods,
    "vards": vards,
    "uzvards": uzvards,
    "epasts": epasts,
    "adrese": adrese,
    "majas_numurs": majas_numurs,
    "dzivoklu_skaits": dzivoklu_skaits,
    "stavi": stavi
    }

  def registret_lietotaju():
    '''
    Funkcija pieņem None tipa vērtību. Šī funkcija nostrādā kad lietotājs galvenajā izvēlnē izvēlas opciju "Reģistrēt jaunu lietotāju". 
    No lietotāja tiek pieprasīts izvēlēties lietotāju ar kādu lomu tas vēlas reģistrēt (katrai lomai ir savs atbilstošais numurs) un pēc izvēlētās lomas tiek palaista atbilstoša funkcija.
    '''

    print("Laipni lūdzam komunālo pakalpojumu kalkulātorā!")
    print("Izvēlieties, kas reģistrējas:")
    print("1 - Iedzīvotājs")
    print("2 - Saimnieks")

    izvele = input("Jūsu izvēle: ").strip()

    if izvele == "1":
      lietotajs = lietotaja_registracija.ievadit_iedzivotaja_datus()
    elif izvele == "2":
      lietotajs = lietotaja_registracija.ievadit_saimnieka_datus()
    else:
      raise ValueError("Kļūda: jāievada 1 vai 2.")

    print("\nReģistrācija veiksmīga.")
    return lietotajs