import numpy as np


def sigmoid(z):
    z = 1 / (1 + np.exp(-z))
    return z


def sigmoid_der(z):
    return sigmoid(z)*(1-sigmoid(z))


class Neural:
    def __init__(self, input_nodes, hidden_nodes_1, hidden_nodes_2, output_nodes):
        self.learning_rate = 0.5

        self.weights_o_h2 = np.random.rand(output_nodes, hidden_nodes_2)-0.5
        self.weights_h2_h1 = np.random.rand(hidden_nodes_2, hidden_nodes_1)-0.5
        self.weights_h1_i = np.random.rand(hidden_nodes_1, input_nodes)-0.5

        self.biases_o = np.random.rand(output_nodes,)-0.5
        self.biases_h2 = np.random.rand(hidden_nodes_2,)-0.5
        self.biases_h1 = np.random.rand(hidden_nodes_1,)-0.5

    def forward(self, X):
        hidden_1_z = X.dot(self.weights_h1_i.T) + self.biases_h1
        hidden_1_a = sigmoid(hidden_1_z)

        hidden_2_z = hidden_1_a.dot(self.weights_h2_h1.T) + self.biases_h2
        hidden_2_a = sigmoid(hidden_2_z)

        output_z = hidden_2_a.dot(self.weights_o_h2.T) + self.biases_o
        output_a = sigmoid(output_z)
        return output_a

    def batch_gradient_descent(self, X, y):
        n = X.shape[0]
        epochs = 2000
        for i in range(epochs):
            hidden_1_z = X.dot(self.weights_h1_i.T) + self.biases_h1
            hidden_1_a = sigmoid(hidden_1_z)

            hidden_2_z = hidden_1_a.dot(self.weights_h2_h1.T) + self.biases_h2
            hidden_2_a = sigmoid(hidden_2_z)

            output_z = hidden_2_a.dot(self.weights_o_h2.T) + self.biases_o
            output_a = sigmoid(output_z)

            output_errors = output_a - y  # have a look at this if y is 1D reshape it
            gradients_o_h2 = (1/n)*(output_errors.T.dot(hidden_2_a))
            gradients_biases_o = (1/n)*np.array([np.sum(output_errors)],)

            hidden_errors_2 = (output_errors.dot(self.weights_o_h2)) * sigmoid_der(hidden_2_z)
            gradients_h2_h1 = (1/n)*(hidden_errors_2.T.dot(hidden_1_a))
            gradients_biases_h2 = (1/n)*(np.sum(hidden_errors_2, axis=0))

            hidden_errors_1 = (hidden_errors_2.dot(self.weights_h2_h1)) * sigmoid_der(hidden_1_z)
            gradients_h1_i = (1/n)*(hidden_errors_1.T.dot(X))
            gradients_biases_h1 = (1/n)*(np.sum(hidden_errors_1, axis=0))

            self.weights_o_h2 -= self.learning_rate * gradients_o_h2
            self.weights_h2_h1 -= self.learning_rate * gradients_h2_h1
            self.weights_h1_i -= self.learning_rate * gradients_h1_i

            self.biases_o -= self.learning_rate * gradients_biases_o
            self.biases_h2 -= self.learning_rate * gradients_biases_h2
            self.biases_h1 -= self.learning_rate * gradients_biases_h1


X_train = [[0, 0, 1],
           [0, 1, 0],
           [1, 0, 1],
           [1, 1, 0]]
y_train = [[0, 1, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
# y_train = [0, 1, 1, 1]

X_train = np.array(X_train)
y_train = np.array(y_train)
nn = Neural(3, 4, 3, 3)
nn.batch_gradient_descent(X_train, y_train)
print(nn.forward(X_train))
