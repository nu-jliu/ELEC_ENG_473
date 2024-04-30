import numpy as np
from scipy.stats import norm

import matplotlib.pyplot as plt

if __name__ == "__main__":
    num_samples = 100
    num_days = 100
    gamma = 0.5
    num_choice = 2

    result = np.zeros(shape=num_samples)

    mu_list = np.array([0.05, 0.1])
    std_list = np.sqrt(np.array([0.1, 0.3]))

    w_list = np.array([1, 1])

    mean_c = np.sum(mu_list) / 2.0
    std_c = np.sum(std_list**2) / 4.0

    for r in range(num_samples):

        val_curr = 1000
        for i in range(num_days):
            p_list = np.zeros(shape=num_choice)

            for j in range(num_choice):
                p_list[j] = ((1 - gamma) * w_list[j] / np.sum(w_list)) + (
                    gamma / num_choice
                )

            # p_list /= np.sum(p_list)
            index = np.random.choice(a=np.arange(0, num_choice), p=p_list)

            mu = mu_list[index]
            std = std_list[index]

            rate = np.random.normal(loc=mu, scale=std)
            val_curr *= 1 + rate
            reward = norm.cdf(rate, mean_c, std_c)

            # print(reward)

            for j in range(num_choice):
                x_hat = 0

                if index == j:
                    x_hat = reward / p_list[j]

                else:
                    pass

                w_list[j] = w_list[j] * np.exp(gamma * x_hat / num_choice)

        result[r] = val_curr

    mean = np.mean(result)
    std = np.std(result)

    print(mean, std)

    plt.plot(result)
    plt.show()
