from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini


def rekinu_apskate():
    '''
    Funkcija rekinu_apskate pieņem None tipa vērtību
    un neatgriež vērtību
    '''

    print("\n=== RĒĶINU APSKATE ===")

    if not rekini:
        print("Rēķinu saraksts ir tukšs.\n")
        return

    print("-" * 72)
    print(f"{'ID':<5} {'Veids':<20} {'Summa (EUR)':<15} {'Datums':<12} {'Periods':<10}")
    print("-" * 72)

    for r in rekini:
        print(f"{r['id']:<5} {r['veids']:<20} {r['summa']:<15} {r['datums']:<12} {r['periods']:<10}")

    print("-" * 72)