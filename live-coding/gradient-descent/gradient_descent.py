points = [(2, 4), (4, 2)]


def F(w):
    return sum((w * x - y)**2 for x, y in points)


def dF(w):
    return sum(2 * (w * x - y) * x for x, y in points)


# Gradient descent
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
