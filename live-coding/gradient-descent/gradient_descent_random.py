import numpy as np


######################################################################
# Modeling: what we want to compute

# Generate artificial data. Fix the seed for repeatable classroom runs.
rng = np.random.default_rng(0)
true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []
for i in range(100000):
    x = rng.standard_normal(d)
    y = true_w.dot(x) + rng.standard_normal()
    points.append((x, y))


def F(w):
    return sum((w.dot(x) - y)**2 for x, y in points) / len(points)


def dF(w):
    return sum(2 * (w.dot(x) - y) * x for x, y in points) / len(points)


######################################################################
# Algorithms: how we compute it

def gradientDescent(F, dF, d, iterations=10, eta=0.01):
    w = np.zeros(d)
    for t in range(iterations):
        value = F(w)
        gradient = dF(w)
        new_w = w - eta * gradient
        new_value = F(new_w)

        print(
            f"iteration {t}: "
            f"gradient = {np.array2string(gradient, precision=4, floatmode='fixed')}, "
            f"w: {np.array2string(w, precision=4, floatmode='fixed')} -> "
            f"{np.array2string(new_w, precision=4, floatmode='fixed')}, "
            f"loss: {value:.4f} -> {new_value:.4f}"
        )

        w = new_w

    return w


if __name__ == "__main__":
    learned_w = gradientDescent(F, dF, d)
    print(f"True weights:    {true_w}")
    print(f"Learned weights: {learned_w}")
