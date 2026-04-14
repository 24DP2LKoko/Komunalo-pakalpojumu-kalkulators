from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import parbaudit_veselu_skaitli


def dzest_rekinu():
    print("=== Rēķina dzēšana ===")

    rekina_id = parbaudit_veselu_skaitli(
        input("Ievadiet rēķinu ID: "),
        "Rēķina ID"
    )

    for i, rekins in enumerate(rekini):
        if rekins["id"] == rekina_id:
            del rekini[i]
            print("Rēķins dzēsts!")
            return

    print("Rēķins nav atrasts.")