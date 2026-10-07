# Basic gradient descent

Fit the line `y = w * x` (with no intercept) to the points `(2, 4)` and `(4, 2)` using the demonstration from the course screenshot.

- `F(w)` computes the sum of squared prediction errors.
- `dF(w)` computes its derivative with respect to `w`.
- Each iteration updates the weight using `w = w - eta * gradient`, with learning rate `eta = 0.01`.

The basic and separated versions require Python 3 with no external dependencies. Run from the repository root:

```bash
python3 live-coding/gradient-descent/gradient_descent.py
```

The script prints 10 iterations. The weight approaches `0.8`, and the loss approaches `7.2`, down from an initial loss of `20`.

Each line prints the gradient at the current weight and the weight and loss before and after the update:

```text
iteration 0: gradient = -32.0000, w: 0.0000 -> 0.3200, loss: 20.0000 -> 11.8080
```

A negative gradient increases the weight; a positive gradient decreases it. Subtracting the gradient chooses the downhill direction, with the learning rate controlling the step size.

For classroom experiments, change the learning rate, initial weight, or number of iterations and observe how convergence changes.

## Version 2: separate modeling and algorithm

`gradient_descent_separated.py` organizes the demonstration into two sections:

- **Modeling:** the training points, loss function `F`, and derivative `dF` define the problem.
- **Algorithm:** `gradientDescent(F, dF, d)` accepts those functions and performs the updates without accessing the training points directly. It returns the final weight.

```bash
python3 live-coding/gradient-descent/gradient_descent_separated.py
```

This version keeps the current basic example's 10 iterations and before-and-after output. After 10 updates, the weight is approximately `0.7952` and the loss is approximately `7.2005`.

The `d = 2` value and `d` parameter are retained from the screenshot, but are unused: this model still has just one scalar weight. To demonstrate a different scalar optimization problem, pass a different loss function and its derivative to the same algorithm.

## Version 3: random data and multiple weights

`gradient_descent_random.py` generates 100,000 examples. Each input has five normally distributed features, and its target is `true_w.dot(x)` plus normally distributed noise, using true weights `[1, 2, 3, 4, 5]`. A fixed random seed makes classroom runs repeatable; change the seed to generate another dataset.

This version requires NumPy. Install and run from the repository root (preferably in a virtual environment):

```bash
python3 -m pip install -r live-coding/gradient-descent/requirements.txt
python3 live-coding/gradient-descent/gradient_descent_random.py
```

The modeling section defines the mean squared error and its gradient. Averaging over the examples keeps the loss and gradient from growing simply because more examples were added. The algorithm now uses `d` to initialize a vector of five weights with `np.zeros(d)` and prints the gradient vector and before-and-after weights and loss.

The default remains 10 updates with learning rate `0.01`, showing the first steps toward the true weights rather than full convergence. To run longer, change the final call to `gradientDescent(F, dF, d, iterations=500)`. Each update processes all 100,000 examples, so longer runs take more time. With enough updates, learned weights should approach the true weights and mean squared error should approach approximately 1, reflecting the added noise.
