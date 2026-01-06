# Brady Nolin Engineering Prompt Solution

## Problem Description

Given a JSON file containing each team's win-loss records versus opponents, create a code solution that builds and displays a matrix of head-to-head records. The table should show the number of wins each team has against every other team.

## Solution Overview

This Python script reads a JSON file with team records and generates a formatted text table displaying the head-to-head wins matrix.

### Key Components

1. **Data Loading**: The `load_records()` function loads and parses the JSON file, handling potential errors like missing files or invalid JSON.

2. **Matrix Generation**: The `generate_matrix()` function processes the records to create a tabular representation:
   - Extracts and sorts team names alphabetically
   - Calculates appropriate column widths for alignment
   - Builds the table header and rows
   - Uses wins data for each team-opponent pair
   - Places "--" for self-matches

## How to Run

1. Ensure you have Python 3 installed
2. Place JSON file in the same directory as `main.py`
3. Run the script with the JSON filename as an argument:

```bash
python main.py records.json
```

## Example Output

```
Head-to-Head Records Matrix
===========================================
Tm   BRO BSN CHC CIN NYG PHI PIT STL
-------------------------------------------
BRO   --  10  15  15  14  14  15  11
BSN  12   --  13  13  13  14  12   9
CHC   7   9   --  12   7  16   8  10
CIN   7   9  10   --  13  13  13   8
NYG   8   9  15   9   --  12  15  13
PHI   8   8   6   9  10   --  13   8
PIT   7  10  14   9   7   9   --   6
STL  11  13  12  14   9  14  16   --
-------------------------------------------
Tm   BRO BSN CHC CIN NYG PHI PIT STL
```
