import openpyxl
from fpdf import FPDF
from MaksajumuAprekins import aprekinit_pakalpojumu_maksu

def DatuEksportesana(rekinu_saraksts, fails, formats="xlsx"):
    """
    funkcija DatuEksportesana pieņem list tipa vērtību rekinu_saraksts, str tipa vērtību fails un str tipa vērtību formats un atgriež str tipa vērtību fails
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    # Izveidojam rindu datus no rēķiniem un aprēķinām summas
    rindas = []
    for rekins in rekinu_saraksts:
        for p in rekins.get("pakalpojumi", []):
            maksa = round(aprekinit_pakalpojumu_maksu(p["paterins"], p["tarifs"]), 2)
            rindas.append((rekins.get("periods", "?"), p.get("veids", "?"), p["paterins"], p["tarifs"], maksa))

    if formats == "xlsx":
        if not fails.endswith(".xlsx"): fails += ".xlsx"
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Periods", "Pakalpojums", "Patēriņš", "Tarifs", "Summa (EUR)"])
        for rinda in rindas: ws.append(list(rinda))
        wb.save(fails)
        return fails
        
    elif formats == "pdf":
        if not fails.endswith(".pdf"): fails += ".pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        
        # Pievieno rindas PDF tabulai
        for rinda in rindas:
            for vertiba in rinda:
                pdf.cell(35, 8, str(vertiba), border=1)
            pdf.ln()
            
        pdf.output(fails)
        return fails
        
    else:
        raise ValueError(f"Kļūda: nezināms formāts '{formats}'.")