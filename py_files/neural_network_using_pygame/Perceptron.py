import numpy as np


def cost_log_loss(y, y_pred):  # logloss
    epsilon = 1e-15
    n = y.shape[0]
    y_pred = np.where(y_pred == 1, 1 - epsilon, y_pred)
    y_pred = np.where(y_pred == 0, epsilon, y_pred)
    cost = (-1 / n) * sum(((y * np.log(y_pred)) + (1 - y) * (np.log(1 - y_pred))))
    return cost


def sigmoid(z):
    z = np.array(z, dtype=np.longdouble)
    return 1 / (1 + np.exp(-z))


class Perceptron:
    def __init__(self):
        self.weights = np.random.rand(1, 2) - 0.5
        self.biases = np.random.rand(1, ) - 0.5
        self.learning_rate = 0.01

    def guess(self, train_X):
        output_z = train_X.dot(self.weights.T) + self.biases
        output_a = sigmoid(output_z)
        output_a = np.where(output_a >= 0.5, 1, 0)
        return output_a

    def stochastic_gradient_descent(self, X, y):
        n = X.shape[0]
        epochs = 1
        for i in range(epochs):
            random_index = np.random.randint(0, n)

            sample_X = X[random_index].reshape(1, -1)
            sample_y = y[random_index].reshape(-1, )

            output_z = sample_X.dot(self.weights.T) + self.biases
            output_a = sigmoid(output_z)

            output_errors = output_a - sample_y.reshape(-1, 1)

            gradients = (1 / n) * (output_errors.T.dot(sample_X))
            gradients_biases = np.array([(1 / n) * np.sum(output_errors)], )

            self.weights -= self.learning_rate * gradients
            self.biases -= self.learning_rate * gradients_biases

    def batch_gradient_descent_log_loss(self, X, y):
        n = X.shape[0]
        epochs = 1
        for i in range(epochs):
            output_z = X.dot(self.weights.T) + self.biases
            output_a = sigmoid(output_z)

            # cost = cost_log_loss(y.reshape(-1, 1), output_a)

            output_errors = output_a - y.reshape(-1, 1)

            gradients = (1 / n) * (output_errors.T.dot(X))
            gradients_biases = (1 / n) * np.sum(output_errors)

            self.weights -= self.learning_rate * gradients
            self.biases -= self.learning_rate * gradients_biases

