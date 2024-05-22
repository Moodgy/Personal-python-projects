import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkfont


class NumberDescriptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Description App")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.custom_font = tkfont.Font(family="Comic Sans", size=12)

        self.number_label = tk.Label(
            self.master, text="Enter a number:", font=self.custom_font, bg="#f0f0f0"
        )
        self.number_label.pack(pady=10)

        self.number_entry = tk.Entry(
            self.master, font=self.custom_font, width=10, justify="center"
        )
        self.number_entry.pack(pady=5)

        self.describe_button = tk.Button(
            self.master,
            text="Describe Number",
            font=self.custom_font,
            command=self.describe_number,
            bg="#4CAF50",
            fg="white",
        )
        self.describe_button.pack(pady=5)

        self.description_text = scrolledtext.ScrolledText(
            self.master,
            width=60,
            height=15,
            font=self.custom_font,
            wrap=tk.WORD,
            state="disabled",
        )
        self.description_text.pack(pady=10)

    def describe_number(self):
        try:
            number = int(self.number_entry.get())
            self.description_text.config(state="normal")
            self.description_text.delete(1.0, tk.END)
            descriptions = [
                f"The number itself: {number}",
                f"The position of the number in a sequence: {self.ordinal(number)}",
                f"The number written out in words: {self.number_to_words(number)}",
                f"Even: {self.is_even(number)}, Odd: {self.is_odd(number)}",
                f"Prime: {self.is_prime(number)}, Composite: {self.is_composite(number)}",
                f"Positive: {self.is_positive(number)}, Negative: {self.is_negative(number)}, Zero: {self.is_zero(number)}",
                f"Integer: {self.is_integer(number)}, Decimal: Not Applicable, Fraction: Not Applicable",
                f"Rational: {self.is_rational(number)}, Irrational: {self.is_irrational(number)}",
                f"Real: {self.is_real(number)}, Imaginary: {self.is_imaginary(number)}, Complex: {self.is_complex(number)}",
                f"The distance of the number from zero on the number line: {self.absolute_value(number)}",
                "Scientific Notation: Not Applicable",
                f"Numbers that can be multiplied together to get the original number: {self.factors(number)}",
                f"Numbers that the original number can be divided by without leaving a remainder: {self.multiples(number)}",
                f"Whether the number can be divided by another number without leaving a remainder: {self.divisibility(number)}",
                f"The result of multiplying a number by itself: {self.powers(number)}",
                f"The inverse operation of raising a number to a given power: {self.roots(number)}",
                "Percentage: Not Applicable",
                "Decimal Places: Not Applicable",
                f"The number flipped upside down: {self.reciprocal(number)}",
                f"An expression containing a root: {self.surd(number)}",
                f"A number in the Fibonacci sequence: {self.is_fibonacci(number)}",
                f"A number that is the reciprocal of the arithmetic mean of the reciprocals of a set of numbers: {self.is_harmonic(number)}",
                f"A number equal to the sum of its proper divisors: {self.is_perfect(number)}",
                f"A number for which the sum of its proper divisors is less than or greater than the number itself, respectively: {self.deficiency(number)}",
                "Lucky Number: True",
                f"A prime number that is one less than a power of two: {self.is_mersenne_prime(number)}",
                "Friendly Number: Not Applicable",
                f"The ratio between the sum of the proper divisors of a number and the number itself: {self.abundancy_index(number)}",
                f"The sum of the proper divisors of a number: {self.aliquot_sum(number)}",
                f"A number that can be expressed as the sum of two positive cubes in two different ways: {self.is_taxicab_number(number)}",
                f"An n-digit number that is the sum of the nth powers of its digits: {self.is_narcissistic(number)}",
            ]
            for desc in descriptions:
                self.description_text.insert(tk.END, desc + "\n\n")
            self.description_text.config(state="disabled")
        except ValueError:
            self.description_text.config(state="normal")
            self.description_text.delete(1.0, tk.END)
            self.description_text.insert(tk.END, "Please enter a valid integer.")
            self.description_text.config(state="disabled")

    def ordinal(self, num):
        if 10 <= num % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
        return str(num) + suffix

    def number_to_words(self, num):
        under_20 = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        above_100 = {100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}

        if num < 20:
            return under_20[int(num)]
        if num < 100:
            return tens[int(num) // 10] + ("" if num % 10 == 0 else " " + under_20[int(num) % 10])
        # find the appropriate pivot
        pivot = max([key for key in above_100.keys() if key <= num])
        return (
            self.number_to_words(num // pivot)
            + " "
            + above_100[pivot]
            + ("" if num % pivot == 0 else " " + self.number_to_words(num % pivot))
        )

    def is_even(self, num):
        return num % 2 == 0

    def is_odd(self, num):
        return not self.is_even(num)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_composite(self, num):
        return not self.is_prime(num) and num > 1

    def is_positive(self, num):
        return num > 0

    def is_negative(self, num):
        return num < 0

    def is_zero(self, num):
        return num == 0

    def is_integer(self, num):
        return num == int(num)

    def is_decimal(self, num):
        return False

    def is_fraction(self, num):
        return False

    def is_rational(self, num):
        return num == int(num) or num == round(num)

    def is_irrational(self, num):
        return not self.is_rational(num)

    def is_real(self, num):
        return num == int(num) or num == round(num)

    def is_imaginary(self, num):
        return not self.is_real(num) and num != 0

    def is_complex(self, num):
        return self.is_real(num) or self.is_imaginary(num)

    def absolute_value(self, num):
        return abs(num)

    def factors(self, num):
        factors_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors_list.append(i)
        return factors_list

    def multiples(self, num):
        multiples_list = []
        for i in range(1, 11):
            multiples_list.append(num * i)
        return multiples_list

    def divisibility(self, num):
        divisibility_list = []
        for i in range(2, num):
            if num % i == 0:
                divisibility_list.append(i)
        return divisibility_list

    def powers(self, num):
        square = num ** 2
        cube = num ** 3
        higher_powers = [num ** i for i in range(4, 11)]  # Higher powers up to the 10th
        return f"Square: {square}, Cube: {cube}, Higher Powers: {higher_powers}"

    def roots(self, num):
        root = num ** 0.5
        cube_root = num ** (1 / 3)
        higher_roots = [num ** (1 / i) for i in range(4, 11)]  # Higher roots up to the 10th
        return f"Square Root: {root}, Cube Root: {cube_root}, Higher Roots: {higher_roots}"

    def reciprocal(self, num):
        if num != 0:
            return 1 / num
        return "Undefined"

    def surd(self, num):
        return f"√{num}"

    def is_fibonacci(self, num):
        def is_perfect_square(x):
            return int(x ** 0.5) ** 2 == x

        return is_perfect_square(5 * num ** 2 + 4) or is_perfect_square(5 * num ** 2 - 4)

    def is_harmonic(self, num):
        return num == 1

    def is_perfect(self, num):
        if num < 2:
            return False
        factors_sum = sum(self.factors(num)[:-1])
        return factors_sum == num

    def deficiency(self, num):
        factors_sum = sum(self.factors(num)[:-1])
        if factors_sum < num:
            return f"Deficient: {factors_sum}"
        elif factors_sum > num:
            return f"Abundant: {factors_sum}"
        else:
            return "Perfect"

    def is_mersenne_prime(self, num):
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        p = 0
        while True:
            if is_prime(2 ** p - 1):
                if 2 ** p - 1 == num:
                    return True
                elif 2 ** p - 1 > num:
                    return False
            p += 1

    def abundancy_index(self, num):
        factors_sum = sum(self.factors(num)[:-1])
        return factors_sum / num

    def aliquot_sum(self, num):
        return sum(self.factors(num)[:-1])

    def is_taxicab_number(self, num):
        def find_taxicab_number():
            n = 2
            while True:
                found = {}
                for a in range(1, n):
                    for b in range(a, n):
                        result = a ** 3 + b ** 3
                        if result in found:
                            found[result].append((a, b))
                            if len(found[result]) == 2:
                                return result, found[result]
                        else:
                            found[result] = [(a, b)]
                n += 1

        result, pairs = find_taxicab_number()
        return num in pairs

    def is_narcissistic(self, num):
        num_str = str(num)
        power = len(num_str)
        return num == sum(int(x) ** power for x in num_str)


def main():
    root = tk.Tk()
    app = NumberDescriptionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    
#Made By: Mohamaed
#Special thanks to Asser, Ezz, and Adam
#This code is licensed under the MIT License.
#https://opensource.org/licenses/MIT
#Very small contribution from the OpenAI Corporation