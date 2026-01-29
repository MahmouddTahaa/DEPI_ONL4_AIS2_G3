import numpy as np
import matplotlib.pyplot as plt
import sys


class SimpleGradientDescentOptimizer:
    def calculate_gradient(self, X, y, w, b):
        m = len(y)
        y_hat = X * w + b

        partial_w = (1 / m) * np.dot(X, (y_hat - y))
        partial_b = (1 / m) * np.sum(y_hat - y)

        return partial_w, partial_b

    def calculate_gd_step(self, param, gradient, lr):
        return param - lr * gradient

    def gradient_descent(self, X, y, w_init, b_init, lr, num_iters):
        wb = []
        w = w_init
        b = b_init

        for _ in range(num_iters):
            partial_w, partial_b = self.calculate_gradient(X, y, w, b)
            w = self.calculate_gd_step(w, partial_w, lr)
            b = self.calculate_gd_step(b, partial_b, lr)
            wb.append((w, b))

        return w, b, wb


def main():
    x = np.array([1, 2, 3, 4])
    y = np.array([2, 2.8, 3.6, 4.5])

    w_init = 0
    b_init = 0
    alpha = 0.01
    num_iterations = 20

    optimizer = SimpleGradientDescentOptimizer()

    w, b, wb = optimizer.gradient_descent(x, y, w_init, b_init, alpha, num_iterations)

    print(f"Optimized parameters: bias = {b}, slope = {w}")

    sse_values = []
    for w_iter, b_iter in wb:
        y_hat = w_iter * x + b_iter
        sse = np.sum((y_hat - y) ** 2)
        sse_values.append(sse)

    for i, sse in enumerate(sse_values):
        if (i + 1) % 20 == 0:
            print(f"iteration {i + 1}, SSE: {sse}")

    y_pred = w * x + b
    print(f"\nPredicted values: {y_pred}")

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(num_iterations), sse_values, label="SSE")
    plt.xlabel("Iteration")
    plt.ylabel("SSE")
    plt.title("SSE over iterations")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(x, y, color="blue", label="Data Points")
    plt.plot(x, b + w * x, color="red", label="Regression Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Linear Regression Fit Line")
    plt.legend()

    plt.tight_layout()
    plt.show()

    X_new = int(input("Please enter a new value for prediction: "))
    y_new = w * X_new + b
    print(f"Predicted value for X={X_new}: {y_new}")


if __name__ == "__main__":
    main()
