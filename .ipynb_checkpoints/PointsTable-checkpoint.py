def update_points_table(points_table, team, goals_for, goals_against, result):
    if team not in points_table:
        points_table[team] = {
            "Played": 0, "Won": 0, "Drawn": 0, "Lost": 0,
            "GF": 0, "GA": 0, "GD": 0, "Points": 0
        }

    stats = points_table[team]
    stats["Played"] += 1
    stats["GF"] += goals_for
    stats["GA"] += goals_against
    stats["GD"] = stats["GF"] - stats["GA"]

    if result == "win":
        stats["Won"] += 1
        stats["Points"] += 3
    elif result == "draw":
        stats["Drawn"] += 1
        stats["Points"] += 1
    elif result == "loss":
        stats["Lost"] += 1


def print_points_table(points_table):
    print(f"{'Team':<10}{'P':<4}{'W':<4}{'D':<4}{'L':<4}{'GF':<4}{'GA':<4}{'GD':<4}{'Pts':<5}")
    print("-" * 50)
    sorted_table = sorted(points_table.items(), key=lambda x: (-x[1]['Points'], -x[1]['GD'], -x[1]['GF'], x[0]))
    for team, stats in sorted_table:
        print(f"{team:<10}{stats['Played']:<4}{stats['Won']:<4}{stats['Drawn']:<4}{stats['Lost']:<4}"
              f"{stats['GF']:<4}{stats['GA']:<4}{stats['GD']:<4}{stats['Points']:<5}")


# Example matches: (team1, team2, goals_team1, goals_team2)
matches = [
    ("Ranit", "Biprotik", 0, 1),
    ("Biprotik", "Soubhik", 3, 0),
    ("Soubhik", "Ranit", 2, 3),
    ("Dibsiyo", "Ranit", 3, 3),
    ("Soubhik", "Dibsiyo", 0, 1),
    ("Dibsiyo", "Biprotik", 1, 0),
    ("Arkaprava", "Dibsiyo", 0, 4),
    ("Dibsiyo", "Debarghya", 1, 4),
    ("Arkaprava", "Soubhik", 2, 0),
    ("Soubhik", "Debarghya", 0, 2),
    ("Arnab", "Dibsiyo", 4, 1),
    ("Arkaprava", "Arnab", 3, 2),
    ("Debarghya", "Ranit", 3, 1),
    ("Ranit", "Arkaprava", 0, 0),
    ("Biprotik", "Arkaprava", 3, 0),
    ("Arkaprava", "Debarghya", 0, 2),
    ("Debarghya", "Biprotik", 3, 0),
    ("Ranit", "Arnab", 1, 2),
    ("Arnab", "Debarghya", 2, 2),
    ("Biprotik", "Arnab", 2, 3)
]

points_table = {}

for team1, team2, g1, g2 in matches:
    if g1 > g2:
        update_points_table(points_table, team1, g1, g2, "win")
        update_points_table(points_table, team2, g2, g1, "loss")
    elif g1 < g2:
        update_points_table(points_table, team1, g1, g2, "loss")
        update_points_table(points_table, team2, g2, g1, "win")
    else:
        update_points_table(points_table, team1, g1, g2, "draw")
        update_points_table(points_table, team2, g2, g1, "draw")

print_points_table(points_table)
