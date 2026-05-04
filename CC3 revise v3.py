import pandas as pd   # Pandas library usage

class MeanMedianModeOfGroupedDataCalculator:  # Base class
    def __init__(self):
        self.results = []   # store results per run
        self.sequence = 1   # run counter
        self.data = []
        self.n = 0

    def show_kwargs(self, **kwargs):  # Arbitrary keyword arguments (**kwargs)
        print("\nShowing keyword arguments (kwargs):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

    def factorial(self, n):   # Recursion example (factorial)
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

class ExtendedCalculator(MeanMedianModeOfGroupedDataCalculator): # Inheritance + Method Overriding
#Mean
    def calculate_mean(self):  # Override method
        print("\n[Overridden] Using pandas for mean calculation...")
        df = pd.DataFrame(self.data, columns=["Lower", "Upper", "Freq"])
        df["Mid"] = (df["Lower"] + df["Upper"]) / 2
        mean = (df["Mid"] * df["Freq"]).sum() / df["Freq"].sum()
        return mean
#Median 
    def calculate_median(self):  
        cf = [0]
        running = 0
        for _, _, f in self.data:
            running += f
            cf.append(running)

        half = running / 2
        index = 0
        for i in range(self.n):
            if cf[i] >= half:
                index = i
                break

        L = self.data[index][0]
        f = self.data[index][2]
        cf_before = 0 if index == 0 else cf[index - 1]
        h = self.data[index][1] - self.data[index][0]

        return L + ((half - cf_before) / f) * h
#Mode
    def calculate_mode(self):
        highest = 0
        pos = 0
        for i in range(self.n):
            if self.data[i][2] > highest:
                highest = self.data[i][2]
                pos = i

        L = self.data[pos][0]
        f1 = self.data[pos][2]
        f0 = self.data[pos - 1][2] if pos > 0 else 0
        f2 = self.data[pos + 1][2] if pos < self.n - 1 else 0
        h = self.data[pos][1] - self.data[pos][0]

        denom = (f1 - f0) + (f1 - f2)
        if denom == 0:
            raise ZeroDivisionError

        return L + ((f1 - f0) / denom) * h
#Rounding
    def format_value(self, value):
        return int(value) if float(value).is_integer() else round(value, 2)

    def sort_data(self):  # Sort using list
        self.data = sorted(self.data, key=lambda x: x[0])

    def show_first_class(self): # Tuple slicing
        if len(self.data) > 0:
            first = self.data[0]
            print("\nFirst Class (tuple):", first)
            print("Lower & Upper only (slice):", first[0:2])

    def validate_intervals(self): # Validate intervals
        for i in range(1, self.n):
            if self.data[i][0] < self.data[i - 1][1]:
                print("\nError: Class intervals overlap.")
                raise ValueError

    def get_class_dict(self):  # Dictionary (class mapping)
        class_dict = {}
        for i, (low, high, f) in enumerate(self.data):
            class_dict[f"Class {i+1}"] = {"Lower": low, "Upper": high, "Freq": f}
        return class_dict

    def total_frequency(self, *args): # Arbitrary arguments (*args)
        return sum(args)

# MAIN PROGRAM
results = []  # store results per run
sequence = 1  # run counter
calc = ExtendedCalculator()   # Using subclass with overriding

while True:
    try: 
        print("\n================================================")
        print("   Mean, Median, Mode of Grouped Data Calculator")
        print("================================================")
    
        n = int(input("\nHow Many classes? "))
        if n <= 0:
            print("Error: Number of classes must be a positive integer.")
            raise ValueError

        calc.n = n
        calc.data = []

        # Input Section
        for i in range(calc.n): 
            print("\nClass", str(i + 1))
            low = float(input("  Lower: "))
            high = float(input("  Upper: "))
            f = int(input("  Frequency: "))

            if high <= low:
                print("Error: Upper class must be greater than lower class.")
                raise ValueError
            if f < 0:
                print("Error: Frequency cannot be negative.")
                raise ValueError

            calc.data.append((low, high, f))   # store as tuple

        # SORTING CLASSES BY LOWER BOUND
        calc.sort_data()

        print("\nSorted Class Intervals:")
        print("----------------------------")
        print(" Lower   Upper   Frequency")
        for low, high, f in calc.data:
            print(" ", low, " ", high, " ", f)
        print("----------------------------")

        # Validations
        calc.validate_intervals()

        # Demonstrations
        calc.show_first_class()            # tuple + slicing
        class_dict = calc.get_class_dict() # dictionary
        print("\nClass Dictionary:", class_dict)

        # kwargs demo
        calc.show_kwargs(Author="Alexis", Subject="CC3", Year=2026)

        # Calculations
        mean = calc.format_value(calc.calculate_mean())
        median = calc.format_value(calc.calculate_median())
        mode = calc.format_value(calc.calculate_mode())

        print("\nRESULTS:")
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
    
        # SAVE RESULTS
        results.append({"run": sequence,"mean": mean,"median": median,"mode": mode,"classes": calc.data[:]})
        sequence += 1
    
    except ValueError:
        print("\nPlease enter a valid numeric input")
    except ZeroDivisionError:
        print("\nCannot divide by zero (check frequencies)")
    except Exception as e:
        print("\nUnexpected Error:", e)

    choice = input("\nDo you want to run again? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        if len(results) == 0:
            print("\nProgram Ended. Goodbye!")
        else:
            print("\nProgram Finished. Goodbye!")
        break
