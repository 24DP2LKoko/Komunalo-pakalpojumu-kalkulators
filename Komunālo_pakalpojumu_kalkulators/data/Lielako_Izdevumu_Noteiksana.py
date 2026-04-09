from MaksajumuAprekins import aprekinit_pakalpojumu_maksu

def LielakoIzdevumuNoteiksana(rekinu_saraksts, tops=3):
    """
    funkcija LielakoIzdevumuNoteiksana pieņem list tipa vērtību rekinu_saraksts un int tipa vērtību tops un atgriež list tipa vērtību lielako_izdevumu_saraksts
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    visi_izdevumi = []
    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        for p in rekins.get("pakalpojumi", []):
            veids = p.get("veids", "Nezināms")
            maksa = round(aprekinit_pakalpojumu_maksu(p["paterins"], p["tarifs"]), 2)
            
            visi_izdevumi.append({
                "periods": periods,
                "veids": veids,
                "summa": maksa
            })

    # Kārto sarakstu dilstošā secībā un atgriež tikai doto skaitu "tops" elementu
    lielako_izdevumu_saraksts = sorted(visi_izdevumi, key=lambda x: x["summa"], reverse=True)[:tops]
    return lielako_izdevumu_saraksts