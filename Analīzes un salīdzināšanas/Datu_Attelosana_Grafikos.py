import matplotlib.pyplot as plt

def DatuAttelosanaGrafikos(rekinu_saraksts):
    """
    Pieņem list rekinu_saraksts, atgriež None.
    Attēlo joslu diagrammu ar izmaksām pa periodiem.
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    periodi = [r.get("periods", "?") for r in rekinu_saraksts]
    summas = [
        round(sum(p["paterins"] * p["tarifs"] for p in r.get("pakalpojumi", [])), 2)
        for r in rekinu_saraksts
    ]

    plt.figure(figsize=(10, 5))
    plt.bar(periodi, summas, color="steelblue")
    plt.title("Komunālo izmaksu sadalījums pa periodiem")
    plt.xlabel("Periods")
    plt.ylabel("Kopējā summa (EUR)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
