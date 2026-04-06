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
    
    
# -------------------------------------------------------------
# Ejercicio 2: Contar tarjetas amarillas

def contar_amarillas(datos):
    total = 0
    equipos = {}

    for partido in datos["matches"]:
        eq1 = partido["team1"]
        eq2 = partido["team2"]
        am1 = partido["yellow_cards"]["team1"]
        am2 = partido["yellow_cards"]["team2"]
        total += am1 + am2
        equipos[eq1] = equipos.get(eq1, 0) + am1
        equipos[eq2] = equipos.get(eq2, 0) + am2

    print("\n" + "-" * 45)
    print("  TARJETAS AMARILLAS")
    print("-" * 45)
    print("  Total en el torneo:", total)
    print("\n  Por equipo (orden alfabetico):")
    for equipo, cantidad in sorted(equipos.items()):
        print("   ", equipo, "->", cantidad)
    print("-" * 45 + "\n")
