from authorisation.db_utils import pievienoties_db

class dzest_lietotaju:
    
    def dzest_irnkieku(personas_kods, lietotajs):

        '''
        funkcija dzest_irnieku pieņem personas_kodu kā string un lietotajs kā dict, un neko neatgriež.
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo lietotāju? (Jā/Nē): ")

        if atbilde == "Jā":
            sql = "DELETE FROM iedzivotaji WHERE personas_kods = %s"
            val = (personas_kods,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Lietotājs veiksmīgi dzēsts.")
        else:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")
        
        mydb.close()

    def dzest_ipasnieku(personas_kods, lietotajs):

        '''
        funkcija dzest_ipasnieku pieņem personas_kodu kā string un lietotajs kā dict, un neko neatgriež.
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo īpašnieku? (Jā/Nē): ")

        if atbilde == "Jā":
            
            sql_majas = "DELETE FROM majas WHERE adrese IN (SELECT parvaldamas_majas_adrese FROM saimnieki WHERE personas_kods = %s)"
            val = (personas_kods,)
            mycursor.execute(sql_majas, val)
            
            
            sql_ipasnieks = "DELETE FROM saimnieki WHERE personas_kods = %s"
            mycursor.execute(sql_ipasnieks, val)
            
            mydb.commit()
            print("Īpašnieks un viņa mājas veiksmīgi dzēstas.")
        else:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")
        
        mydb.close()

    def dzest_maju(adrese, lietotajs):

        '''
        funkcija dzest_maju pieņem adresi kā string un lietotajs kā dict, un neko neatgriež.
        '''

        mydb, mycursor = pievienoties_db()

        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst šo māju? (Jā/Nē): ")

        if atbilde == "Jā":
            sql = "DELETE FROM majas WHERE adrese = %s"
            val = (adrese,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Māja veiksmīgi dzēsta.")
        else:
            print("Darbība atcelta. Atgriežamies uz galveno izvēlni.")
        
        mydb.close()