while True:
    # Input of numbers
    b = input("Enter numbers(please separate with commas): ")
    sep = b.split(",")  # Separate the entered numbers into a list

    x = b.replace(",", "").replace(".", "")
    valid = all(i.isdigit() for i in x)
    print(x)

    if valid:
        a = [round(float(i), 3) for i in sep]
        ops = input("Enter operator: ")
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

    else:
        print("There is a non-digit in your numbers:", sep)
        continue
