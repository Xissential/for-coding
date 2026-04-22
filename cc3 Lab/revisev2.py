results = []  # dito naka store yung results per run
sequence = 1  # run counter

while True:
    try:
        print("\n================================================")
        print("   Mean, Median, Mode of Group Data Calculator")
        print("================================================")

        n = int(input("\nHow Many classes? "))
        if n <= 0:
            print("Error: Number of classes must be a positive integer.")
            raise ValueError

        data = []

        # here yung Input Section
        for i in range(n):
            print("\nClass " + str(i + 1))

            low = float(input("  Lower: "))
            high = float(input("  Upper: "))
            f = int(input("  Frequency: "))

            if high <= low:
                raise ValueError

            if f < 0:
                print("Error: Frequency cannot be negative.")
                raise ValueError

            data = data + [[low, high, f]]

        # SORT (Bubble Sort)
        for a in range(len(data)):
            for b in range(len(data) - 1):
                if data[b][0] > data[b + 1][0]:
                    temp = data[b]
                    data[b] = data[b + 1]
                    data[b + 1] = temp

        # VALIDATE INTERVALS
        for i in range(1, n):
            prev_high = data[i - 1][1]
            curr_low = data[i][0]

            if curr_low < prev_high:
                print("\nError: Class intervals overlap.")
                raise ValueError

        print("\nSorted Class Intervals:")
        print("----------------------------")
        print(" Lower   Upper   Frequency")
        print("----------------------------")

        for low, high, f in data:
            print(" ", low, " ", high, " ", f)

        print("----------------------------")

        # MEAN
        total_f = 0
        total_fx = 0

        for i in range(n):
            mid = (data[i][0] + data[i][1]) / 2
            total_fx += mid * data[i][2]
            total_f += data[i][2]

        if total_f == 0:
            raise ZeroDivisionError

        mean = total_fx / total_f

        # MEDIAN
        cf = []
        running = 0

        for i in range(n):
            running += data[i][2]
            cf = cf + [running]

        half = running / 2

        index = 0
        for i in range(n):
            if cf[i] >= half:
                index = i
                break

        L = data[index][0]
        f = data[index][2]
        cf_before = 0 if index == 0 else cf[index - 1]
        h = data[index][1] - data[index][0]

        median = L + ((half - cf_before) / f) * h

        # MODE
        highest = 0
        pos = 0

        for i in range(n):
            if data[i][2] > highest:
                highest = data[i][2]
                pos = i

        L = data[pos][0]
        f1 = data[pos][2]
        f0 = data[pos - 1][2] if pos > 0 else 0
        f2 = data[pos + 1][2] if pos < n - 1 else 0
        h = data[pos][1] - data[pos][0]

        denom = (f1 - f0) + (f1 - f2)
        if denom == 0:
            raise ZeroDivisionError

        mode = L + ((f1 - f0) / denom) * h

        # ROUNDING
        mean = int(mean) if mean.is_integer() else round(mean, 2)
        median = int(median) if median.is_integer() else round(median, 2)
        mode = int(mode) if mode.is_integer() else round(mode, 2)

        # OUTPUT
        print("\nRESULTS:")
        print("----------------------------")
        print(" Mean   :", mean)
        print(" Median :", median)
        print(" Mode   :", mode)
        print("----------------------------")

        # SAVE RESULTS
        results = results + [{
            "run": sequence,
            "mean": mean,
            "median": median,
            "mode": mode,
            "classes": data[:]
        }]

        sequence += 1

    except ValueError:
        print("\nPlease enter a valid numeric input")
    except ZeroDivisionError:
        print("\nCannot divide by zero (check frequencies)")
    except Exception as e:
        print("\nUnexpected Error:", e)

    # ASK USER TO CONTINUE
    choice = input("\nDo you want to run the program again? (yes/no): ").strip().lower()

    if choice not in ("yes", "y"):
        if len(results) == 0:
            print("\nProgram Ended. Goodbye!")
        else:
            print("\nProgram Finished. Goodbye!")
        break