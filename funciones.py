import json


def cargar_datos(ruta="euro_modificado.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------------------------------------------
# Ejercicio 1: Listar todos los partidos
# -------------------------------------------------------------
def listar_partidos(datos):
    print("\n" + "-" * 70)
    print("  PARTIDOS -", datos["name"])
    print("-" * 70)
    for i, partido in enumerate(datos["matches"], 1):
        equipo1 = partido["team1"]
        equipo2 = partido["team2"]
        ft = partido["score"].get("ft", ["?", "?"])
        am1 = partido["yellow_cards"]["team1"]
        am2 = partido["yellow_cards"]["team2"]
        print(" ", i, ".", equipo1, "vs", equipo2, "|", ft[0], "-", ft[1], "| Amarillas:", equipo1, am1, "-", equipo2, am2)
    print("=" * 70 + "\n")