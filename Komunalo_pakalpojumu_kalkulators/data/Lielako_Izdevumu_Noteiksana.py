def LielakoIzdevumuNoteiksana(rekinu_saraksts, tops=3):
    """
    funkcija LielakoIzdevumuNoteiksana pieņem list tipa vērtību rekinu_saraksts un int tipa vērtību tops un atgriež list tipa vērtību lielako_izdevumu_saraksts
    """

    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    visi_izdevumi = []

    for rekins in rekinu_saraksts:
        visi_izdevumi.append({
            "id": rekins.get("id", ""),
            "periods": rekins.get("periods", "Nav norādīts"),
            "veids": rekins.get("veids", "Nezināms"),
            "summa": round(float(rekins.get("summa", 0)), 2)
        })

    lielako_izdevumu_saraksts = sorted(
        visi_izdevumi,
        key=lambda x: x["summa"],
        reverse=True
    )[:tops]

    return lielako_izdevumu_saraksts