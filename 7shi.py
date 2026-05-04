import pandas as pd   # ✅ Pandas library usage

# 🔹 Base Calculator Class
class GroupedDataCalculator:

    def __init__(self):
        self.results = []   # store results per run
        self.sequence = 1   # run counter

    # 🔹 Arbitrary keyword arguments (**kwargs)
    def show_kwargs(self, **kwargs):
        print("\nShowing keyword arguments (kwargs):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

    # 🔹 Recursion example (factorial)
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


# 🔹 Inheritance + Method Overriding
class ExtendedCalculator(GroupedDataCalculator):

    # Override method to show pandas usage
    def calculate_mean_with_pandas(self, data):
        print("\n[Overridden] Using pandas for mean calculation...")
        df = pd.DataFrame(data, columns=["Lower", "Upper", "Freq"])
        df["Mid"] = (df["Lower"] + df["Upper"]) / 2
        mean = (df["Mid"] * df["Freq"]).sum() / df["Freq"].sum()
        return mean


# 🔹 MAIN PROGRAM
results = []  # store results per run
sequence = 1  # run counter
calc = ExtendedCalculator()   # ✅ Using subclass with overriding

while True:
    try:
        print("\n================================================")
        print("   Mean, Median, Mode of Grouped Data Calculator")
        print("================================================")

        n = int(input("\nHow Many classes? "))
        if n <= 0:
            print("Error: Number of classes must be a positive integer.")
            raise ValueError

        data = []
        # Input Section
        for i in range(n):
            print("\nClass " + str(i + 1))

            low = float(input("  Lower: "))
            high = float(input("  Upper: "))
            f = int(input("  Frequency: "))

            if high <= low:
                print("Error: Upper class must be greater than lower class.")
                raise ValueError

            if f < 0:
                print("Error: Frequency cannot be negative.")
                raise ValueError

            data.append([low, high, f])  # ✅ List usage

        # SORTING CLASSES BY LOWER BOUND
        for a in range(len(data)):
            for b in range(len(data) - 1):
                if data[b][0] > data[b + 1][0]:
                    data[b], data[b + 1] = data[b + 1], data[b]

        # CHECKING FOR OVERLAPPING CLASSES
        for i in range(1, n):
            prev_high = data[i - 1][1]
            curr_low = data[i][0]
            if curr_low < prev_high:
                print(f"\nError: Class {i} overlaps with previous class.")
                raise ValueError

        print("\nSorted Class Intervals:")
        print("----------------------------")
        print(" Lower   Upper   Frequency")
        for low, high, f in data:
            print(f" {low:<7} {high:<7} {f:<7}")
        print("----------------------------")

        # MEAN
        total_f = sum([row[2] for row in data])
        total_fx = sum([((row[0] + row[1]) / 2) * row[2] for row in data])

        if total_f == 0:
            raise ZeroDivisionError

        mean = total_fx / total_f

        # MEDIAN
        cf = []
        running = 0
        for row in data:
            running += row[2]
            cf.append(running)

        half = running / 2
        index = next(i for i in range(n) if cf[i] >= half)

        L = data[index][0]
        f = data[index][2]
        cf_before = 0 if index == 0 else cf[index - 1]
        h = data[index][1] - data[index][0]
        median = L + ((half - cf_before) / f) * h

        # MODE
        pos = max(range(n), key=lambda i: data[i][2])
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
        print(f" Mean   : {mean}")
        print(f" Median : {median}")
        print(f" Mode   : {mode}")
        print("----------------------------")

        # SAVE RESULTS
        results.append({"run": sequence, "mean": mean, "median": median, "mode": mode, "classes": data[:]})
        sequence += 1

        # 🔹 Extra Demonstrations
        calc.show_kwargs(Author="Alexis", Subject="Statistics", Year=2026)
        num = int(input("\nEnter a number for factorial demo: "))
        print(f"Factorial of {num} = {calc.factorial(num)}")
        print("Mean via pandas (override):", round(calc.calculate_mean_with_pandas(data), 2))

        # 🔹 Pandas demonstration tied to grouped data
        df = pd.DataFrame(data, columns=["Lower", "Upper", "Freq"])
        df["Mid"] = (df["Lower"] + df["Upper"]) / 2
        print("\nPandas DataFrame of your grouped data:\n", df)

        print("\nPandas Calculations:")
        print("  Mean   :", round((df["Mid"] * df["Freq"]).sum() / df["Freq"].sum(), 2))
        print("  Median (approx):", round(df["Mid"].median(), 2))
        print("  Mode (approx):", list(df["Mid"].mode()))

    except ValueError:
        print("\nPlease enter a valid numeric input")
    except ZeroDivisionError:
        print("\nCannot divide by zero (check frequencies)")
    except Exception as e:
        print("\nUnexpected Error:", e)

    choice = input("\nDo you want to run the program again? (yes/no): ").strip().lower()

    if choice not in ("yes", "y"):
        if len(results) == 0:
            print("\nProgram Ended. Goodbye!")
        else:
            print("\nSummary of All Runs:")
            print("===================================")
            for r in results:
                print(f"Run {r['run']}: Mean={r['mean']}, Median={r['median']}, Mode={r['mode']}")
                print("  Classes:", r['classes'])
            print("===================================")
            print("\nProgram Finished. Goodbye!")
        break

