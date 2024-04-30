import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mu_apple = 0.05
    std_apple = np.sqrt(0.1)

    mu_msft = 0.1
    std_msft = np.sqrt(0.3)

    mu_list = np.array([mu_apple, mu_msft])
    std_list = np.array([std_apple, std_msft])

    total_days = 100

    num_samples = 100

    total_apple = mu_apple
    total_msft = mu_msft

    count_apple = 1
    count_msft = 1

    indices = np.array([0, 1])

    results = np.zeros(shape=num_samples)

    for i in range(num_samples):

        val_curr = 1000
        vals = np.zeros(shape=total_days + 1)
        vals[0] = val_curr

        for j in range(total_days):
            avg_apple = total_apple / count_apple
            avg_msft = total_msft / count_msft

            rate = 0
            if avg_apple > avg_msft:
                rate = np.random.normal(mu_apple, std_apple)
                total_apple += rate
                count_apple += 1

            elif avg_msft > avg_apple:
                rate = np.random.normal(mu_msft, std_msft)
                total_msft += rate
                count_msft += 1

            else:
                index = np.random.choice(indices)
                rate = np.random.normal(mu_list[index], std_list[index])

                if index == 0:
                    total_apple += rate
                    count_apple += 1
                else:
                    total_msft += rate
                    count_msft += 1

            val_curr *= 1 + rate
            vals[j + 1] = val_curr

        results[i] = val_curr

    mean = np.mean(results)
    std = np.std(results)

    print(mean, std)

    plt.plot(results)
    plt.show()
