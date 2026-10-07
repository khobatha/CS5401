######################################################################
# Modeling: what we want to compute

points = [(2, 4), (4, 2)]
d = 2  # Retained from the screenshot; unused in this scalar example.


def F(w):
    return sum((w * x - y)**2 for x, y in points)


def dF(w):
    return sum(2 * (w * x - y) * x for x, y in points)


######################################################################
# Algorithms: how we compute it

def gradientDescent(F, dF, d):
    # The algorithm uses the supplied loss and derivative functions.
    # d is unused because w is a single number, not a vector.
    w = 0
    eta = 0.01
    for t in range(10):
        value = F(w)
        gradient = dF(w)
        new_w = w - eta * gradient
        new_value = F(new_w)

        print(
            f"iteration {t}: "
            f"gradient = {gradient:.4f}, "
            f"w: {w:.4f} -> {new_w:.4f}, "
            f"loss: {value:.4f} -> {new_value:.4f}"
        )

        w = new_w

    return w


if __name__ == "__main__":
    gradientDescent(F, dF, d)
