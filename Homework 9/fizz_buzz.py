counter = int(1)

while True:
    try:
        x = int(input("Pick a number between 1 and 100:"))
        if 1 <= x <= 100:
            for counter in range(1, x + 1):
                if counter % 3 == 0 and counter % 5 == 0:
                    print("fizzbuzz")
                elif counter % 3 == 0:
                    print("fizz")
                elif counter % 5 == 0:
                    print("buzz")
                else:
                    print(counter)
            break
        else:
            print("The selected number should be in range of 1 to 100! Try again.")
    except ValueError:
        print("Please insert a number(floats excluded)")


