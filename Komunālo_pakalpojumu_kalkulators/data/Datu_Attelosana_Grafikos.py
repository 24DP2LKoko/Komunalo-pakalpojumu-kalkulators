def DatuAttelosanaGrafikos(rekinu_saraksts):
    """
    funkcija DatuAttelosanaGrafikos pieņem list tipa vērtību rekinu_saraksts un atgriež None tipa vērtību None
    """

    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    print(f"{'Periods':<15} | {'Veids':<20} | {'Summa (EUR)':<15}")
    print("-" * 55)

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        veids = rekins.get("veids", "Nav norādīts")
        summa = rekins.get("summa", 0)

        print(f"{periods:<15} | {veids:<20} | {round(summa, 2):<15}")