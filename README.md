**File descriptions:**

value_statement.txt: Will contain our value statement / grant identity. Currently empty.

variables.csv: Table of project IDs, names, and variables. Currently just the messy 'R1' variables from original spreadsheet.

value_functions.py: file of potential value functions. Currently just contains greens_equally(), which only cares about the 'R1_Group' variable, and assigns value 1 to each 'green' project.

allocate.py: Calls a value function from value_functions and splits the £3m according to the scores.

allocation.csv: Table of the money allocated to each project.

