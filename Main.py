from Komunalo_pakalpojumu_kalkulators.calculations.Rekina_Pievienosana import pievienot_rekinu
from Komunalo_pakalpojumu_kalkulators.calculations.Rekina_Redigesana import rediget_rekinu
from Komunalo_pakalpojumu_kalkulators.calculations.Rekina_Dzesana import dzest_rekinu
from Komunalo_pakalpojumu_kalkulators.calculations.Rekinu_Apskate import rekinu_apskate
from Komunalo_pakalpojumu_kalkulators.calculations.Rekinu_Filtresana import filtre_rekinus
from Komunalo_pakalpojumu_kalkulators.calculations.Rekinu_Meklesana import rekinu_meklesana
from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini

from Komunalo_pakalpojumu_kalkulators.integrity.MaksajumuAprekins import aprekinit_komunalos_maksajumus
from Komunalo_pakalpojumu_kalkulators.integrity.Videja_paterina_aprekins import aprekinit_videjo_paterinu
from Komunalo_pakalpojumu_kalkulators.integrity.automatiska_atjaunosana import atjaunot_aprekinu
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import (
    parbaudit_tuksu_lauku,
    parbaudit_skaitli,
    parbaudit_epastu,
)

from Komunalo_pakalpojumu_kalkulators.data.Datu_Attelosana_Grafikos import DatuAttelosanaGrafikos
from Komunalo_pakalpojumu_kalkulators.data.Datu_Eksportesana import DatuEksportesana
from Komunalo_pakalpojumu_kalkulators.data.Izmainu_Analize_Pa_Periodiem import IzmainuAnalizePaPeriodiem
from Komunalo_pakalpojumu_kalkulators.data.Lielako_Izdevumu_Noteiksana import LielakoIzdevumuNoteiksana
from Komunalo_pakalpojumu_kalkulators.data.Rekinu_Salidzinasana import RekinuSalidzinasana
from Komunalo_pakalpojumu_kalkulators.data.Statistikas_Generesana import StatistikasGeneresana


lietotaji = []


class komunalo_maksu_kalkulators:
    def paradit_sakuma_izvelni(self):
        while True:
            print("\n=== KOMUNĀLO PAKALPOJUMU KALKULATORS ===")
            print("1. Reģistrēties")
            print("2. Autorizēties")
            print("3. Iziet")

            izvele = input("Izvēlieties darbību: ").strip()

            if izvele == "1":
                try:
                    lietotajs = self.registret_lietotaju_lokali()
                    self.paradit_lietotaja_paneli(lietotajs)
                except Exception as kluda:
                    print(f"Kļūda: {kluda}")

            elif izvele == "2":
                try:
                    lietotajs = self.autorizet_lietotaju_lokali()
                    if lietotajs is not None:
                        self.paradit_lietotaja_paneli(lietotajs)
                except Exception as kluda:
                    print(f"Kļūda: {kluda}")

            elif izvele == "3":
                print("Programma tiek aizvērta.")
                break

            else:
                print("Kļūda: ievadiet 1, 2 vai 3.")

    def registret_lietotaju_lokali(self):
        print("\nLaipni lūdzam komunālo pakalpojumu kalkulatorā!")
        print("Izvēlieties, kas reģistrējas:")
        print("1 - Iedzīvotājs")
        print("2 - Saimnieks")

        izvele = input("Jūsu izvēle: ").strip()

        if izvele == "1":
            personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu: "), "Personas kods")
            vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
            uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
            epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")
            adrese = parbaudit_tuksu_lauku(input("Ievadiet adresi: "), "Adrese")
            dzivokla_nr = parbaudit_skaitli(input("Ievadiet dzīvokļa nr.: "), "Dzīvokļa nr.")

            lietotajs = {
                "loma": "Iedzīvotājs",
                "personas_kods": personas_kods,
                "vards": vards,
                "uzvards": uzvards,
                "epasts": epasts,
                "adrese": adrese,
                "dzivokla_nr": dzivokla_nr,
            }

        elif izvele == "2":
            personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu: "), "Personas kods")
            vards = parbaudit_tuksu_lauku(input("Ievadiet vārdu: "), "Vārds")
            uzvards = parbaudit_tuksu_lauku(input("Ievadiet uzvārdu: "), "Uzvārds")
            epasts = parbaudit_epastu(input("Ievadiet e-pastu: "), "E-pasts")

            print("\nIevadiet informāciju par pārvaldāmo māju:")
            adrese = parbaudit_tuksu_lauku(input("Adrese: "), "Adrese")
            majas_numurs = parbaudit_skaitli(input("Mājas numurs: "), "Mājas numurs")
            dzivoklu_skaits = parbaudit_skaitli(input("Dzīvokļu skaits: "), "Dzīvokļu skaits")
            stavi = parbaudit_skaitli(input("Stāvu skaits: "), "Stāvu skaits")

            lietotajs = {
                "loma": "Saimnieks",
                "personas_kods": personas_kods,
                "vards": vards,
                "uzvards": uzvards,
                "epasts": epasts,
                "adrese": adrese,
                "majas_numurs": majas_numurs,
                "dzivoklu_skaits": dzivoklu_skaits,
                "stavi": stavi,
            }

        else:
            raise ValueError("Kļūda: jāievada 1 vai 2.")

        for esoss in lietotaji:
            if esoss["personas_kods"] == lietotajs["personas_kods"]:
                raise ValueError("Kļūda: lietotājs ar šādu personas kodu jau pastāv.")

        lietotaji.append(lietotajs)
        print("\nReģistrācija veiksmīga.")
        return lietotajs

    def autorizet_lietotaju_lokali(self):
        print("\n=== LIETOTĀJA AUTORIZĀCIJA ===")
        print("Izvēlieties lietotāja tipu:")
        print("1 - Iedzīvotājs")
        print("2 - Saimnieks")

        izvele = input("Jūsu izvēle: ").strip()
        personas_kods = parbaudit_tuksu_lauku(input("Ievadiet personas kodu: "), "Personas kods")

        meklejama_loma = None
        if izvele == "1":
            meklejama_loma = "Iedzīvotājs"
        elif izvele == "2":
            meklejama_loma = "Saimnieks"
        else:
            print("Kļūda: jāievada 1 vai 2.")
            return None

        for lietotajs in lietotaji:
            if lietotajs["personas_kods"] == personas_kods and lietotajs["loma"] == meklejama_loma:
                print("\nAutorizācija veiksmīga.")
                return lietotajs

        print("Kļūda: lietotājs netika atrasts.")
        return None

    def paradit_lietotaja_paneli(self, lietotajs):
        while True:
            print("\n=== LIETOTĀJA PANELIS ===")
            print(f"Sveicināti, {lietotajs.get('vards', '')} {lietotajs.get('uzvards', '')}!")
            print(f"Jūsu loma: {lietotajs.get('loma', 'Nav zināma')}")

            print("\n--- Galvenā izvēlne ---")
            print("1. Pievienot rēķinu")
            print("2. Rediģēt rēķinu")
            print("3. Dzēst rēķinu")
            print("4. Apskatīt rēķinus")
            print("5. Filtrēt rēķinus")
            print("6. Meklēt rēķinus")
            print("7. Aprēķināt komunālos maksājumus")
            print("8. Aprēķināt vidējo patēriņu")
            print("9. Automātiski atjaunot aprēķinu")
            print("10. Attēlot datus")
            print("11. Eksportēt datus")
            print("12. Analizēt izmaiņas pa periodiem")
            print("13. Noteikt lielākos izdevumus")
            print("14. Salīdzināt rēķinus")
            print("15. Ģenerēt statistiku")
            print("16. Rediģēt profilu")
            print("17. Dzēst lietotāju")
            print("18. Izrakstīties")

            izvele = input("Izvēlieties darbību: ").strip()

            try:
                if izvele == "1":
                    pievienot_rekinu()

                elif izvele == "2":
                    rediget_rekinu()

                elif izvele == "3":
                    dzest_rekinu()

                elif izvele == "4":
                    rekinu_apskate()

                elif izvele == "5":
                    filtre_rekinus()

                elif izvele == "6":
                    rekinu_meklesana()

                elif izvele == "7":
                    self.aprekinat_komunalos_maksajumus_interaktivs()

                elif izvele == "8":
                    self.aprekinat_videjo_paterinu_interaktivs()

                elif izvele == "9":
                    self.atjaunot_aprekinu_interaktivs()

                elif izvele == "10":
                    DatuAttelosanaGrafikos(rekini)

                elif izvele == "11":
                    self.eksportet_datus_interaktivs()

                elif izvele == "12":
                    rezultats = IzmainuAnalizePaPeriodiem(rekini)
                    print("\nIzmaiņu analīze pa periodiem:")
                    for ieraksts in rezultats:
                        print(ieraksts)

                elif izvele == "13":
                    tops = input("Ievadiet, cik lielākos izdevumus attēlot (Enter = 3): ").strip()
                    if tops == "":
                        tops = 3
                    else:
                        tops = int(tops)

                    rezultats = LielakoIzdevumuNoteiksana(rekini, tops)
                    print("\nLielākie izdevumi:")
                    for ieraksts in rezultats:
                        print(ieraksts)

                elif izvele == "14":
                    rezultats = RekinuSalidzinasana(rekini)
                    print("\nRēķinu salīdzinājums:")
                    for periods, summa in rezultats.items():
                        print(f"{periods}: {summa} EUR")

                elif izvele == "15":
                    rezultats = StatistikasGeneresana(rekini)
                    print("\nStatistika:")
                    for atslega, vertiba in rezultats.items():
                        print(f"{atslega}: {vertiba}")

                elif izvele == "16":
                    self.rediget_profilu(lietotajs)

                elif izvele == "17":
                    if self.dzest_lietotaju(lietotajs):
                        break

                elif izvele == "18":
                    print("Izrakstīšanās veiksmīga.")
                    break

                else:
                    print("Kļūda: ievadiet skaitli no 1 līdz 18.")

            except Exception as kluda:
                print(f"Kļūda: {kluda}")

    def aprekinat_komunalos_maksajumus_interaktivs(self):
        print("\n=== KOMUNĀLO MAKSĀJUMU APRĒĶINS ===")

        udens_paterins = input("Ievadiet ūdens patēriņu: ")
        udens_tarifs = input("Ievadiet ūdens tarifu: ")
        elektribas_paterins = input("Ievadiet elektrības patēriņu: ")
        elektribas_tarifs = input("Ievadiet elektrības tarifu: ")
        gazes_paterins = input("Ievadiet gāzes patēriņu: ")
        gazes_tarifs = input("Ievadiet gāzes tarifu: ")
        apkures_paterins = input("Ievadiet apkures patēriņu: ")
        apkures_tarifs = input("Ievadiet apkures tarifu: ")

        rezultats = aprekinit_komunalos_maksajumus(
            udens_paterins,
            udens_tarifs,
            elektribas_paterins,
            elektribas_tarifs,
            gazes_paterins,
            gazes_tarifs,
            apkures_paterins,
            apkures_tarifs
        )

        print("\nAprēķina rezultāts:")
        print(f"Ūdens maksa: {rezultats['udens_maksa']} EUR")
        print(f"Elektrības maksa: {rezultats['elektribas_maksa']} EUR")
        print(f"Gāzes maksa: {rezultats['gazes_maksa']} EUR")
        print(f"Apkures maksa: {rezultats['apkures_maksa']} EUR")
        print(f"Kopējā summa: {rezultats['kopeja_summa']} EUR")

    def aprekinat_videjo_paterinu_interaktivs(self):
        print("\n=== VIDĒJĀ PATĒRIŅA APRĒĶINS ===")
        dati = input("Ievadiet patēriņus, atdalot ar komatiem (piemēram: 10,20,30): ")
        paterinu_saraksts = [x.strip() for x in dati.split(",")]
        rezultats = aprekinit_videjo_paterinu(paterinu_saraksts)
        print(f"Vidējais patēriņš: {rezultats}")

    def atjaunot_aprekinu_interaktivs(self):
        print("\n=== AUTOMĀTISKA APRĒĶINA ATJAUNOŠANA ===")

        udens_paterins = input("Ievadiet ūdens patēriņu: ")
        udens_tarifs = input("Ievadiet ūdens tarifu: ")
        elektribas_paterins = input("Ievadiet elektrības patēriņu: ")
        elektribas_tarifs = input("Ievadiet elektrības tarifu: ")
        gazes_paterins = input("Ievadiet gāzes patēriņu: ")
        gazes_tarifs = input("Ievadiet gāzes tarifu: ")
        apkures_paterins = input("Ievadiet apkures patēriņu: ")
        apkures_tarifs = input("Ievadiet apkures tarifu: ")

        rezultats = atjaunot_aprekinu(
            udens_paterins,
            udens_tarifs,
            elektribas_paterins,
            elektribas_tarifs,
            gazes_paterins,
            gazes_tarifs,
            apkures_paterins,
            apkures_tarifs
        )

        print("\nAtjaunotais rezultāts:")
        print(f"Ūdens maksa: {rezultats['udens_maksa']} EUR")
        print(f"Elektrības maksa: {rezultats['elektribas_maksa']} EUR")
        print(f"Gāzes maksa: {rezultats['gazes_maksa']} EUR")
        print(f"Apkures maksa: {rezultats['apkures_maksa']} EUR")
        print(f"Kopējā summa: {rezultats['kopeja_summa']} EUR")

    def eksportet_datus_interaktivs(self):
        print("\n=== DATU EKSPORTĒŠANA ===")
        fails = input("Ievadiet faila nosaukumu: ").strip()
        formats = input("Ievadiet formātu (xlsx/pdf): ").strip().lower()
        rezultats = DatuEksportesana(rekini, fails, formats)
        print(f"Dati eksportēti failā: {rezultats}")

    def rediget_profilu(self, lietotajs):
        print("\n=== PROFILA REDIĢĒŠANA ===")

        if lietotajs.get("loma") == "Iedzīvotājs":
            print("1. Vārds")
            print("2. Uzvārds")
            print("3. Personas kods")
            print("4. Adrese")
            print("5. Dzīvokļa numurs")

            izvele = input("Izvēlieties darbību: ").strip()

            if izvele == "1":
                lietotajs["vards"] = parbaudit_tuksu_lauku(input("Ievadiet jauno vārdu: "), "Vārds")
            elif izvele == "2":
                lietotajs["uzvards"] = parbaudit_tuksu_lauku(input("Ievadiet jauno uzvārdu: "), "Uzvārds")
            elif izvele == "3":
                lietotajs["personas_kods"] = parbaudit_tuksu_lauku(input("Ievadiet jauno personas kodu: "), "Personas kods")
            elif izvele == "4":
                lietotajs["adrese"] = parbaudit_tuksu_lauku(input("Ievadiet jauno adresi: "), "Adrese")
            elif izvele == "5":
                lietotajs["dzivokla_nr"] = parbaudit_skaitli(input("Ievadiet jauno dzīvokļa numuru: "), "Dzīvokļa numurs")
            else:
                print("Kļūda: ievadiet skaitli no 1 līdz 5.")
                return

        elif lietotajs.get("loma") == "Saimnieks":
            print("1. Vārds")
            print("2. Uzvārds")
            print("3. Personas kods")
            print("4. E-pasts")
            print("5. Adrese")
            print("6. Mājas numurs")
            print("7. Dzīvokļu skaits")
            print("8. Stāvu skaits")

            izvele = input("Izvēlieties darbību: ").strip()

            if izvele == "1":
                lietotajs["vards"] = parbaudit_tuksu_lauku(input("Ievadiet jauno vārdu: "), "Vārds")
            elif izvele == "2":
                lietotajs["uzvards"] = parbaudit_tuksu_lauku(input("Ievadiet jauno uzvārdu: "), "Uzvārds")
            elif izvele == "3":
                lietotajs["personas_kods"] = parbaudit_tuksu_lauku(input("Ievadiet jauno personas kodu: "), "Personas kods")
            elif izvele == "4":
                lietotajs["epasts"] = parbaudit_epastu(input("Ievadiet jauno e-pastu: "), "E-pasts")
            elif izvele == "5":
                lietotajs["adrese"] = parbaudit_tuksu_lauku(input("Ievadiet jauno adresi: "), "Adrese")
            elif izvele == "6":
                lietotajs["majas_numurs"] = parbaudit_skaitli(input("Ievadiet jauno mājas numuru: "), "Mājas numurs")
            elif izvele == "7":
                lietotajs["dzivoklu_skaits"] = parbaudit_skaitli(input("Ievadiet jauno dzīvokļu skaitu: "), "Dzīvokļu skaits")
            elif izvele == "8":
                lietotajs["stavi"] = parbaudit_skaitli(input("Ievadiet jauno stāvu skaitu: "), "Stāvu skaits")
            else:
                print("Kļūda: ievadiet skaitli no 1 līdz 8.")
                return

        print("Dati ir veiksmīgi atjaunināti.")

    def dzest_lietotaju(self, lietotajs):
        print("\n=== LIETOTĀJA DZĒŠANA ===")
        atbilde = input("Vai esat pārliecināts, ka vēlaties dzēst lietotāju? (Jā/Nē): ")

        if atbilde == "Jā":
            if lietotajs in lietotaji:
                lietotaji.remove(lietotajs)
            print("Lietotājs veiksmīgi dzēsts.")
            return True

        print("Darbība atcelta.")
        return False


if __name__ == "__main__":
    programma = komunalo_maksu_kalkulators()
    programma.paradit_sakuma_izvelni()