results = [] # dito naka store yung results per run
sequence = 1 # run counter

while True:
    try:
        print("\n================================================")
        print("   Mean, Median, Mode of Group Data Calculator")
        print("================================================")

        n = int(input("\nHow many classes? "))

        if n <= 0:
            print("Number of classes must be positive.")
            continue

        data = []
        valid_input = True

        # INPUT SECTION
        for i in range(n):
            print("\nClass " + str(i + 1))
            low = float(input("  Lower: "))
            high = float(input("  Upper: "))
            f = int(input("  Frequency: "))

            if high <= low:
                print("Upper bound must be greater than lower bound.")
                valid_input = False
                break

            if f < 0:
                print("Frequency cannot be negative.")
                valid_input = False
                break

            data = data + [[low, high, f]]

        if not valid_input:
            continue

        # SORT WITHOUT lambda (Bubble Sort)
        for a in range(len(data)):
            for b in range(len(data) - 1):
                if data[b][0] > data[b + 1][0]:
                    temp = data[b]
                    data[b] = data[b + 1]
                    data[b + 1] = temp

        # VALIDATE INTERVALS
        valid_intervals = True
        for i in range(1, n):
            prev_high = data[i - 1][1]
            curr_low = data[i][0]

            if curr_low < prev_high:
                print("\nERROR: Class intervals overlap.")
                valid_intervals = False
                break

        if not valid_intervals:
            continue

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

        mode = L + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * h

        # ROUNDING
        if mean.is_integer():
            mean = int(mean)
        else:
            mean = round(mean, 2)

        if median.is_integer():
            median = int(median)
        else:
            median = round(median, 2)

        if mode.is_integer():
            mode = int(mode)
        else:
            mode = round(mode, 2)

        # OUTPUT
        print("\nRESULTS:")
        print("----------------------------")
        print(" Mean   :", mean)
        print(" Median :", median)
        print(" Mode   :", mode)
        print("----------------------------")

        # SAVE RESULTS (no append)
        results = results + [{
            "run": sequence,
            "mean": mean,
            "median": median,
            "mode": mode,
            "classes": data[:]
        }]

        sequence = sequence + 1

    except ValueError:
        print("\nValue Error: Please enter valid numeric input.")
    except TypeError:
        print("\nType Error: Invalid type encountered.")
    except ZeroDivisionError:
        print("\nZero Division Error: Division by zero occurred.")
    except IndexError:
        print("\nIndex Error: Something went wrong with list indexing.")
    except FileNotFoundError:
        print("\nFile Not Found Error: The file you tried to access does not exist.")
    except ModuleNotFoundError:
        print("\nModule Not Found Error: A required module is missing.")
    except SyntaxError:
        print("\nSyntax Error: There is a syntax issue in your input or code.")
    except Exception as e:
        print("\nUnexpected Error:", e)

    choice = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("\nProgram Finished. Goodbye!")
        break

# SUMMARY
print("\n====================================")
print("        SUMMARY OF ALL RESULTS      ")
print("====================================")

for item in results:
    print("\nMean   :", item["mean"])
    print("Median :", item["median"])
    print("Mode   :", item["mode"])