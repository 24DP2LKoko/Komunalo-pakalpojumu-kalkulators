# saraksts, kur glabāsim rēķinus
from rekini import rekini

def pievienot_rekinu():
    id = len(rekini) + 1
    print("=== Jauna rēķina pievienošana ===")
    
    veids = input("Ievadiet pakalpojuma veidu (ūdens, elektrība utt.): ")
    summa = float(input("Ievadiet summu: "))
    datums = input("Ievadiet datumu (YYYY-MM-DD): ")
    periods = input("Ievadiet periodu (piemēram, 2025-03): ")
    
    rekins = {
        "id": id,
        "veids": veids,
        "summa": summa,
        "datums": datums,
        "periods": periods
    }
    
    rekini.append(rekins)
    
    print("Rēķins veiksmīgi pievienots!\n")


# testēšana
if __name__ == "__main__":
    pievienot_rekinu()
    print(rekini)