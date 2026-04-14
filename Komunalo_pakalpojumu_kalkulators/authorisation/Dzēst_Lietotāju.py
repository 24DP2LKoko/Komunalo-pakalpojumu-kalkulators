from Komunalo_pakalpojumu_kalkulators.authorisation.db_utils import pievienoties_db


class dzest_lietotaju:

    def dzest_irnkieku(personas_kods, lietotajs):
        '''
        Funkcija dzest_irnkieku pieņem str tipa vērtību personas_kods un dict tipa vērtību lietotajs
        un neatgriež vērtību
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo lietotāju? (Jā/Nē): ").strip().lower()

        if atbilde in ["jā", "ja"]:
            sql = "DELETE FROM irnieki WHERE personas_kods = %s"
            val = (personas_kods,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Lietotājs veiksmīgi dzēsts.")

        elif atbilde in ["nē", "ne"]:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")

        else:
            print("Nederīga izvēle. Ievadiet 'Jā' vai 'Nē'.")

        mycursor.close()
        mydb.close()

    def dzest_ipasnieku(personas_kods, lietotajs):
        '''
        Funkcija dzest_ipasnieku pieņem str tipa vērtību personas_kods un dict tipa vērtību lietotajs
        un neatgriež vērtību
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo īpašnieku? (Jā/Nē): ").strip().lower()

        if atbilde in ["jā", "ja"]:
            sql_majas = "DELETE FROM majas WHERE adrese IN (SELECT parvaldamas_majas_adrese FROM ipasnieks WHERE personas_kods = %s)"
            val = (personas_kods,)
            mycursor.execute(sql_majas, val)

            sql_ipasnieks = "DELETE FROM ipasnieks WHERE personas_kods = %s"
            mycursor.execute(sql_ipasnieks, val)

            mydb.commit()
            print("Īpašnieks un viņa mājas veiksmīgi dzēstas.")

        elif atbilde in ["nē", "ne"]:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")

        else:
            print("Nederīga izvēle. Ievadiet 'Jā' vai 'Nē'.")

        mycursor.close()
        mydb.close()

    def dzest_maju(adrese, lietotajs):
        '''
        Funkcija dzest_maju pieņem str tipa vērtību adrese un dict tipa vērtību lietotajs
        un neatgriež vērtību
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo māju? (Jā/Nē): ").strip().lower()

        if atbilde in ["jā", "ja"]:
            sql = "DELETE FROM majas WHERE adrese = %s"
            val = (adrese,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Māja veiksmīgi dzēsta.")

        elif atbilde in ["nē", "ne"]:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")

        else:
            print("Nederīga izvēle. Ievadiet 'Jā' vai 'Nē'.")

        mycursor.close()
        mydb.close()