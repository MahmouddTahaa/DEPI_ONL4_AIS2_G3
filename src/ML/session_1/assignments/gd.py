import numpy as np


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
    X = np.array([1, 2, 3, 4, 5])
    y = 5 * X + 2

    gd = SimpleGradientDescentOptimizer()

    w, b, wb = gd.gradient_descent(
        X, y, np.random.random() * 10, np.random.random() * 10, 0.01, 100
    )

    print(w * X + b)


if __name__ == "__main__":
    main()
