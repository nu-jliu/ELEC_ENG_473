import random
import matplotlib.pyplot as plt

if __name__ == "__main__":
    stock_val = 100.0

    values = []

    for i in range(100):
        val_s1 = stock_val / 2
        val_s2 = stock_val / 2

        ret_s1 = random.uniform(-1.0, 1.0)
        ret_s2 = random.uniform(-2.0, 8.0)

        new_s1 = val_s1 * (1.0 + ret_s1 / 100.0)
        new_s2 = val_s2 * (1.0 + ret_s2 / 100.0)

        stock_val = new_s1 + new_s2

        print(f"Total value at day {i + 1} is {stock_val}")

        values.append(stock_val)

plt.plot(values)
plt.xlabel("Days")
plt.ylabel("Total Return [$]")
plt.show()
