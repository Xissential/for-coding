class GroupedDataCalculator:

    def __init__(self):
        self.data = []   # list
        self.n = 0

    # 🔹 Input data
    def input_data(self):
        self.n = int(input("\nHow Many classes? "))
        if self.n <= 0:
            raise ValueError("Number of classes must be positive")

        self.data = []

        for i in range(self.n):
            print("\nClass", i + 1)
            low = float(input("  Lower: "))
            high = float(input("  Upper: "))
            f = int(input("  Frequency: "))

            if high <= low:
                raise ValueError("Upper must be greater than lower")
            if f < 0:
                raise ValueError("Frequency cannot be negative")

            # store as tuple
            self.data.append((low, high, f))  

    # 🔹 Sort using list
    def sort_data(self):
        self.data = sorted(self.data, key=lambda x: x[0])

    # 🔹 Tuple slicing
    def show_first_class(self):
        if len(self.data) > 0:
            first = self.data[0]
            print("\nFirst Class (tuple):", first)
            print("Lower & Upper only (slice):", first[0:2])

    # 🔹 Validate intervals
    def validate_intervals(self):
        for i in range(1, self.n):
            if self.data[i][0] < self.data[i - 1][1]:
                raise ValueError("Class intervals overlap")

    # 🔹 Set (unique frequencies)
    def get_unique_frequencies(self):
        freq_set = {f for _, _, f in self.data}
        print("\nUnique Frequencies (set):", freq_set)

    # 🔹 Dictionary (class mapping)
    def get_class_dict(self):
        class_dict = {}
        for i, (low, high, f) in enumerate(self.data):
            class_dict[f"Class {i+1}"] = {"Lower": low, "Upper": high, "Freq": f}
        return class_dict

    # 🔹 Arbitrary arguments (*args)
    def total_frequency(self, *args):
        return sum(args)

    # 🔹 Mean
    def calculate_mean(self):
        total_fx = 0
        freqs = []

        for low, high, f in self.data:
            mid = (low + high) / 2
            total_fx += mid * f
            freqs.append(f)

        total_f = self.total_frequency(*freqs)  # using *args

        if total_f == 0:
            raise ZeroDivisionError

        return total_fx / total_f

    # 🔹 Median
    def calculate_median(self):
        cf = []
        running = 0

        for _, _, f in self.data:
            running += f
            cf.append(running)

        half = running / 2

        for i in range(self.n):
            if cf[i] >= half:
                index = i
                break

        L = self.data[index][0]
        f = self.data[index][2]
        cf_before = 0 if index == 0 else cf[index - 1]
        h = self.data[index][1] - self.data[index][0]

        return L + ((half - cf_before) / f) * h

    # 🔹 Mode
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

    def format_value(self, value):
        return int(value) if value.is_integer() else round(value, 2)


# 🔹 MAIN PROGRAM
while True:
    try:
        calc = GroupedDataCalculator()

        calc.input_data()
        calc.sort_data()
        calc.validate_intervals()

        # 🔹 Demonstrations
        calc.show_first_class()            # tuple + slicing
        calc.get_unique_frequencies()      # set

        class_dict = calc.get_class_dict() # dictionary
        print("\nClass Dictionary:", class_dict)

        # 🔹 Calculations
        mean = calc.format_value(calc.calculate_mean())
        median = calc.format_value(calc.calculate_median())
        mode = calc.format_value(calc.calculate_mode())

        print("\nRESULTS:")
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)

    except Exception as e:
        print("Error:", e)

    if input("\nRun again? (yes/no): ").lower() not in ("yes", "y"):
        break