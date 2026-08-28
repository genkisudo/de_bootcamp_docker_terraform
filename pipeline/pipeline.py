import sys

print("arguments", sys.argv)

if len(sys.argv) < 2:
    sys.exit(f"Usage: python {sys.argv[0]} <month>")

try:
    month = int(sys.argv[1])
except ValueError:
    sys.exit(f"Invalid month {sys.argv[1]!r}: must be an integer")

print(f"Running pipeline for month {month}")