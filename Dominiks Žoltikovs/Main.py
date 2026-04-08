class komunalo_maksu_kalkulators:

    def paradit_lietotaja_paneli(lietotajs):

        '''
        Funkcija paradit_lietotaja_paneli pieņem dict tipa
        vērtību lietotajs un neatgriež vērtību
        '''

        def pievienoties_db():
            mydb = mysql.connector.connect(
            host="sql.freedb.tech",
            user="freedb_dominiks",
            password="wDCZqbM3v2D!3Er",
            database="freedb_dzivokli"
        
            )
        

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