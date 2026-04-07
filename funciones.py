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
    
# -------------------------------------------------------------
# Ejercicio 3: Buscar partidos de un equipo

def buscar_partidos_equipo(datos, nombre_equipo):
    nombre_equipo = nombre_equipo.strip()
    encontrados = []

    for partido in datos["matches"]:
        eq1 = partido["team1"]
        eq2 = partido["team2"]
        ft = partido["score"].get("ft", ["?", "?"])

        if nombre_equipo.lower() == eq1.lower():
            amarillas = partido["yellow_cards"]["team1"]
            encontrados.append((eq2, ft[0], ft[1], amarillas))
        elif nombre_equipo.lower() == eq2.lower():
            amarillas = partido["yellow_cards"]["team2"]
            encontrados.append((eq1, ft[1], ft[0], amarillas))

    print("\n" + "-" * 55)
    if not encontrados:
        print("  No se encontro el equipo:", nombre_equipo)
    else:
        print("  Partidos de", nombre_equipo.title(), "-", len(encontrados), "partidos")
        print("-" * 55)
        print("  Rival                     | Resultado | Amarillas")
        print("  " + "-" * 50)
        for rival, g1, g2, amarillas in encontrados:
            print("  ", rival, "|", g1, "-", g2, "| Amarillas:", amarillas)
    print("-" * 55 + "\n")
    
# -------------------------------------------------------------
# Ejercicio 4: Buscar goles de un jugador

def buscar_goles_jugador(datos, nombre_jugador):
    nombre_jugador = nombre_jugador.strip().lower()
    encontrados = []

    for partido in datos["matches"]:
        eq1 = partido["team1"]
        eq2 = partido["team2"]
        ft = partido["score"].get("ft", ["?", "?"])

        for gol in partido.get("goals1", []):
            if gol["name"].lower() == nombre_jugador:
                offset = gol.get("offset", 0)
                encontrados.append((eq1, eq2, gol["minute"], offset, ft[0], ft[1]))

        for gol in partido.get("goals2", []):
            if gol["name"].lower() == nombre_jugador:
                offset = gol.get("offset", 0)
                encontrados.append((eq1, eq2, gol["minute"], offset, ft[0], ft[1]))

    print("\n" + "-" * 65)
    if not encontrados:
        print("  No se encontro al jugador:", nombre_jugador.title())
    else:
        print("  Goles de", nombre_jugador.title(), "-", len(encontrados), "gol(es)")
        print("=" * 65)
        print("  Partido                           | Minuto | Resultado")
        print("  " + "-" * 60)
        for eq1, eq2, minuto, offset, g1, g2 in encontrados:
            if offset:
                print("  ", eq1, "vs", eq2, "| Minuto:", minuto, "+", offset, "| Resultado:", g1, "-", g2)
            else:
                print("  ", eq1, "vs", eq2, "| Minuto:", minuto, "| Resultado:", g1, "-", g2)
    print("=" * 65 + "\n")

# -------------------------------------------------------------
# Ejercicio 5: Clasificacion por goles

def clasificacion_por_goles(datos):
    equipos_goles = {}
    equipos_jugadores = {}

    for partido in datos["matches"]:
        eq1 = partido["team1"]
        eq2 = partido["team2"]

        for eq in (eq1, eq2):
            if eq not in equipos_goles:
                equipos_goles[eq] = 0
                equipos_jugadores[eq] = {}

        for gol in partido.get("goals1", []):
            if not gol.get("owngoal", False):
                equipos_goles[eq1] += 1
                jugador = gol["name"]
                equipos_jugadores[eq1][jugador] = equipos_jugadores[eq1].get(jugador, 0) + 1

        for gol in partido.get("goals2", []):
            if not gol.get("owngoal", False):
                equipos_goles[eq2] += 1
                jugador = gol["name"]
                equipos_jugadores[eq2][jugador] = equipos_jugadores[eq2].get(jugador, 0) + 1

    clasificacion = sorted(equipos_goles.items(), key=lambda x: x[1], reverse=True)

    print("\n" + "-" * 55)
    print("  CLASIFICACION POR GOLES -", datos["name"])
    print("-" * 55)
    for pos, (equipo, goles) in enumerate(clasificacion, 1):
        print("\n ", pos, ".", equipo, "---", goles, "gol(es)")
        jugadores = equipos_jugadores[equipo]
        if jugadores:
            for jugador, n in sorted(jugadores.items(), key=lambda x: x[1], reverse=True):
                print("      ", jugador, ":", n)
        else:
            print("       (sin goles anotados)")
    print("\n" + "-" * 55 + "\n")
