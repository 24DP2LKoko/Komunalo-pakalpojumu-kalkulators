from calculations.rekini import rekini

def filtre_rekinus():
    print("=== Filtrēšana ===")
    
    veids = input("Veids (Enter = izlaist): ")
    summa = input("Maksimālā summa (Enter = izlaist): ")
    datums = input("Datums (YYYY-MM-DD, Enter = izlaist): ")
    
    rezultati = []
    
    for r in rekini:
        if veids and r["veids"].lower() != veids.lower():
            continue
        
        if summa and r["summa"] > float(summa):
            continue
        
        if datums and r["datums"] != datums:
            continue
        
        rezultati.append(r)
    
    if rezultati:
        print("\nAtrasti rēķini:")
        for r in rezultati:
            print(r)
    else:
        print("Nav atrasti rēķini.")
