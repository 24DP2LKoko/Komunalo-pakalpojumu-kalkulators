from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import parbaudit_personas_kodu
from Komunalo_pakalpojumu_kalkulators.authorisation.db_utils import pievienoties_db


def LietotajaAutorizacija():
    '''
    Funkcija LietotajaAutorizacija pieņem None tipa vērtību
    un atgriež dict tipa vērtību lietotajs vai None tipa vērtību None
    '''

    print("=== LIETOTĀJA AUTORIZĀCIJA ===")
    print("Izvēlieties lietotāja tipu:")
    print("1 - Iedzīvotājs")
    print("2 - Saimnieks")

    izvele = input("Jūsu izvēle: ").strip()
    personas_kods = parbaudit_personas_kodu(
        input("Ievadiet personas kodu (XXXXXX-XXXXX): "),
        "Personas kods"
    )

    mydb, mycursor = pievienoties_db()

    if izvele == "1":
        sql = "SELECT personas_kods, vards, uzvards, epasts, adrese, dz_nr FROM irnieki WHERE personas_kods = %s"
        mycursor.execute(sql, (personas_kods,))
        rezultats = mycursor.fetchone()

        mycursor.close()
        mydb.close()

        if rezultats:
            lietotajs = {
                "loma": "Iedzīvotājs",
                "personas_kods": rezultats[0],
                "vards": rezultats[1],
                "uzvards": rezultats[2],
                "epasts": rezultats[3],
                "adrese": rezultats[4],
                "dzivokla_nr": rezultats[5]
            }
            print("\nAutorizācija veiksmīga.")
            return lietotajs

        print("Lietotājs ar šādu personas kodu netika atrasts.")
        return None

    elif izvele == "2":
        sql = "SELECT personas_kods, vards, uzvards, epasts, parvaldamas_majas_adrese FROM ipasnieks WHERE personas_kods = %s"
        mycursor.execute(sql, (personas_kods,))
        rezultats = mycursor.fetchone()

        mycursor.close()
        mydb.close()

        if rezultats:
            lietotajs = {
                "loma": "Saimnieks",
                "personas_kods": rezultats[0],
                "vards": rezultats[1],
                "uzvards": rezultats[2],
                "epasts": rezultats[3],
                "adrese": rezultats[4]
            }
            print("\nAutorizācija veiksmīga.")
            return lietotajs

        print("Īpašnieks ar šādu personas kodu netika atrasts.")
        return None

    else:
        mycursor.close()
        mydb.close()
        raise ValueError("Jāievada 1 vai 2.")