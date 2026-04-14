from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import parbaudit_tuksu_lauku


def rekinu_meklesana():
    '''
    Funkcija rekinu_meklesana pieņem None tipa vērtību
    un neatgriež vērtību
    '''

    print("=== Meklēšana ===")

    atsl = parbaudit_tuksu_lauku(
        input("Ievadiet meklējamo vērtību (ID, veids, datums, periods vai summa): "),
        "Meklēšanas lauks"
    ).lower()

    atrasti = False

    print("\nID | Veids | Summa (EUR) | Datums | Periods")
    print("-------------------------------------------------------")

    for r in rekini:
        if (
            atsl in str(r["id"]).lower()
            or atsl in r["veids"].lower()
            or atsl in r["datums"].lower()
            or atsl in r["periods"].lower()
            or atsl in str(r["summa"]).lower()
        ):
            print(f"{r['id']} | {r['veids']} | {r['summa']} | {r['datums']} | {r['periods']}")
            atrasti = True

    if not atrasti:
        print("Nekas netika atrasts.\n")