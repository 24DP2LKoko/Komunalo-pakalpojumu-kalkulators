from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini

def dzest_rekinu():
    print("=== Rēķina dzēšana ===")

    rekina_id = int(input("Ievadiet rēķinu ID: "))

    for i, rekins in enumerate(rekini):
        if rekins["id"] == rekina_id:
            del rekini[i]
            print("Dzēst!")
            return

    print("Nav atrasts!")