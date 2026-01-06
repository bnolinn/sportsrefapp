import json
import sys

def load_records(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'.")
        sys.exit(1)

def generate_matrix(records):
    teams = sorted(records.keys())
    team_col_width = max(len(team) for team in teams)
    cell_width = 4
    header = f"{'Tm':<{team_col_width}}"
    for team in teams:
        header += f" {team:^{cell_width}}"
    
    separator = "-" * len(header)
    lines = [header, separator]
    for team in teams:
        row = f"{team:<{team_col_width}}"
        for opponent in teams:
            if team == opponent:
                row += f" {'--':^{cell_width}}"
            else:
                wins = records[team][opponent]['W']
                row += f" {wins:^{cell_width}}"
        lines.append(row)
    
    lines.append(separator)
    lines.append(header)
    return "\n".join(lines)

filename = sys.argv[1]
records = load_records(filename)
print("\nHead-to-Head Records Matrix")
print("=" * 43)
print(generate_matrix(records))