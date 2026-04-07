class lietotaja_registracija:
  from Datu_validacija import parbaudit_skaitli, parbaudit_tuksu_lauku, parbaudit_epastu
  import mysql.connector
  def pievienoties_db():
    mydb = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_dominiks",
    password="wDCZqbM3v2D!3Er",
    database="freedb_dzivokli"
)
  def ievadit_iedzivotaja_datus():
    
    '''
    Funkcija ievadit_iedzivotaja_datus pieņem None tipa vērtību
    un atgriež dict tipa vērtību iedzivotajs
    '''
    
    vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
    uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
    epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")
    adrese = parbaudit_tuksu_lauku(input("Ievadiet adresi: "), "Adrese")
    dzivokla_nr = parbaudit_skaitli(input("Ievadiet dzīvokļa nr.: "), "Dzīvokļa nr.")

    iedzivotajs = {
      "loma": "Iedzīvotājs",
      "vards": vards,
      "uzvards": uzvards,
      "epasts": epasts,
      "adrese": adrese,
      "dzivokla_nr": dzivokla_nr
    }

    return iedzivotajs

  def ievadit_saimnieka_datus():

    '''
    Funkcija ievadit_saimnieka_datus pieņem None tipa vērtību
    un atgriež dict tipa vērtību saimnieks
    '''

    vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
    uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
    epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")
    parvaldama_majas_adrese = parbaudit_tuksu_lauku(input("Ievadiet pārvaldāmās mājas adresi: "),
    "Pārvaldāmās mājas adrese")

    print("\nIevadiet informāciju par pārvaldāmo māju:")
    adrese = parbaudit_tuksu_lauku(input("Adrese: "), "Adrese")
    majas_numurs = parbaudit_skaitli(input("Mājas numurs: "), "Mājas numurs")
    dzivoklu_skaits = parbaudit_skaitli(input("Dzīvokļu skaits: "), "Dzīvokļu skaits")
    stavi = parbaudit_skaitli(input("Stāvu skaits: "), "Stāvu skaits")

    saimnieks = {
      "loma" : "Saimnieks",
      "vards": vards,
      "uzvards": uzvards,
      "epasts": epasts,
      "parvaldama_majas_adrese": parvaldama_majas_adrese,
      "maja": {
        "adrese": adrese,
        "majas_numurs": majas_numurs,
        "dzivoklu_skaits": dzivoklu_skaits,
        "stavi": stavi
      }
    }

    return saimnieks

  def registret_lietotaju():
    '''
    Funkcija registret_lietotaju pieņem None tipa vērtību
    un atgriež dict tipa vērtību lietotajs
    '''

    print("Laipni lūdzam komunālo pakalpojumu kalkulātorā!")
    print("Izvēlieties, kas reģistrējas:")
    print("1 - Iedzīvotājs")
    print("2 - Saimnieks")

    izvele = input("Jūsu izvēle: ").strip()

    if izvele == "1":
      lietotajs = ievadit_iedzivotaja_datus()
    elif izvele == "2":
      lietotajs = ievadit_saimnieka_datus()
    else:
      raise ValueError("Kļūda: jāievada 1 vai 2.")

    print("\nReģistrācija veiksmīga.")
    return lietotajs

  if __name__ == "__main__":
    try:
      lietotajs = registret_lietotaju()
      print("\nReģistrētie dati:")
      print(lietotajs)
    except ValueError as kluda:
      print(kluda)