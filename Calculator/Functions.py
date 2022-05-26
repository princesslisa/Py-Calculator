while True:
    # Input of numbers
    b = input("Enter numbers(please separate with commas): ")
    sep = b.split(",")  # Separate the entered numbers into a list

    # Checks if the input is all digits or if there is a letter in between
    x = b.replace(",", "").replace(".", "")
    valid = all(i.isdigit() for i in x)
    print(x)

    if valid:
        # Converts the numbers to floats for calculation
        # Not converting to integers, in the event that there is a float in the entries
        a = [round(float(i), 3) for i in sep]

        # Checks for the operator sign and carries out operation
        ops = input('Enter operator: ')
        if ops == "-":
            c = a[0]
            i = 1
            while i < len(a):
                c -= a[i]
                i += 1
        elif ops == "+":
            c = a[0]
            i = 1
            while i < len(a):
                c += a[i]
                i += 1
        elif ops == "*":
            c = a[0]
            i = 1
            while i < len(a):
                c *= a[i]
                i += 1
        elif ops == "/":
            c = a[0]
            i = 1
            while i < len(a):
                c /= a[i]
                i += 1
        print("Therefore,", b.replace(",", ops), "= ", c)
        break

    # If there is a non-digit character in the entries, it writes out the entries and asks you to enter input again
    else:
        print("There is a non-digit in your numbers:", sep)
        continue
