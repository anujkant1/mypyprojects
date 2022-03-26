"""Hex Grid,
Displays a simplle tessellation of a hexagon grid."""

# Set up the constants:
X_REPEAT = 20  # How many times to tessellate horizontally.
Y_REPEAT = 20  # How many times to tessellate vertically.

for y in range(Y_REPEAT):
    # Display the top half of the hexagon:
    for x in range(X_REPEAT):
        print(r"/ \_", end="")
    print()

    # Display the bottome half of the hexagon:
    for x in range(X_REPEAT):
        print(r"\_/", end="")
    print()
