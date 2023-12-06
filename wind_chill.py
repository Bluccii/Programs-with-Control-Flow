# Import all necessary modules for the code.
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
t = float(sys.argv[1])
v = float(sys.argv[2])

# if statement used to determine if t is more than 50, then outputs a statement
if t > 50:
    stdio.writeln(f"Value of t must be <= 50 F")

# if statement used to determine if v is less than or equal to 3, then outputs a statement
elif v <= 3:
    stdio.writeln(f"Value of v must be > 3 mph")

# Calculates and outputs wind chill if other if statements are by-passed
else:
    wind_chill = (35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16))
    stdio.writeln(wind_chill)
