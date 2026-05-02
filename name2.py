n = 5

for i in range(n):

    # C
    if i == 0 or i == n-1:
        print("####", end=" ")
    else:
        print("#   ", end=" ")

    # H
    print(" ", end="")
    if i == n//2:
        print("#####", end=" ")
    else:
        print("#   #", end=" ")

    # A
    print(" ", end="")
    if i == 0:
        print(" ### ", end=" ")
    elif i == n//2:
        print("#####", end=" ")
    else:
        print("#   #", end=" ")

    # I
    print(" ", end="")
    if i == 0 or i == n-1:
        print("#####", end=" ")
    else:
        print("  #  ", end=" ")

    # T
    print(" ", end="")
    if i == 0:
        print("#####", end=" ")
    else:
        print("  #  ", end=" ")

    # H
    print(" ", end="")
    if i == n//2:
        print("#####", end=" ")
    else:
        print("#   #", end=" ")

    # R
    print(" ", end="")
    if i == 0 or i == n//2:
        print("#### ", end=" ")
    elif i < n//2:
        print("#   #", end=" ")
    else:
        print("#  # ", end=" ")

    # A
    print(" ", end="")
    if i == 0:
        print(" ### ", end=" ")
    elif i == n//2:
        print("#####", end=" ")
    else:
        print("#   #", end=" ")

    # Space between words
    print("   ", end=" ")

    # C
    if i == 0 or i == n-1:
        print("####", end=" ")
    else:
        print("#   ", end=" ")

    # P
    print(" ", end="")
    if i == 0 or i == n//2:
        print("#### ", end=" ")
    elif i < n//2:
        print("#   #", end=" ")
    else:
        print("#    ", end=" ")

    print()