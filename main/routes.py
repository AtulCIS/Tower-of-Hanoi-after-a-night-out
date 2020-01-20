from flask import render_template
from main import app


@app.route("/")
@app.route("/home")
def home():
    toh = TowerOfHanoi()
    num = toh.get_number()
    test1 = toh.test_values(2, 5, 1, 3, 5)  # E(2,5,1,3,5) = 60
    test2 = toh.test_values(3, 20, 4, 9, 17)  # E(3,20,4,9,17) = 2358
    return render_template("main.html", num=num, test1=test1, test2=test2)

class TowerOfHanoi:
    def __init__(self):
        """initialization of modulus to have positive numbers """
        self.mod = 10 ** 9

    def test_values(self, n, k, a, b, c):
        """This function will evaluate the standards expression result """
        return self.get_square_travelled(n, k, a, b, c)

    @staticmethod
    def get_square_travelled(n, k, a, b, c):
        """This function does the actual calculations for the test results """
        g = (2 ** (n + 2) - 3 - (-1) ** n) // 6
        return 2 * g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)

    def get_number(self):
        """The main function to evaluate the ∑1≤n≤10000 E(n,10n,3n,6n,9n) """
        total_number = 0  # expected number of squares travelled
        previous, current = 0, 1  # current position and previous position
        k, a, b, c = 10, 3, 6, 9
        for n in range(1, 10000 + 1):
            expected_number = (
                2 * current * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)
            ) % self.mod
            total_number = (total_number + expected_number) % self.mod
            previous, current = current, (current + 2 * previous + 1) % self.mod
            k = (k * 10) % self.mod
            a = (a * 3) % self.mod
            b = (b * 6) % self.mod
            c = (c * 9) % self.mod
        return total_number

    @staticmethod
    def get_square_travelled(n, k, a, b, c):
        """This function does the actual calculations for the test results """
        g = (2 ** (n + 2) - 3 - (-1) ** n) // 6
        return 2 * g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)

    def get_number(self):
        """The main function to evaluate the ∑1≤n≤10000 E(n,10n,3n,6n,9n) """
        total_number = 0  # expected number of squares travelled
        previous, current = 0, 1  # current position and previous position
        k, a, b, c = 10, 3, 6, 9
        for n in range(1, 10000 + 1):
            expected_number = (
                2 * current * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)
            ) % self.mod
            total_number = (total_number + expected_number) % self.mod
            previous, current = current, (current + 2 * previous + 1) % self.mod
            k = (k * 10) % self.mod
            a = (a * 3) % self.mod
            b = (b * 6) % self.mod
            c = (c * 9) % self.mod
        return total_number
