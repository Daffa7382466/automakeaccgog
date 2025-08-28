class Perceptron:
    """A simple single-layer perceptron for binary classification."""

    def __init__(self, input_size, learning_rate=0.1):
        self.learning_rate = learning_rate
        # +1 for bias weight
        self.weights = [0.0] * (input_size + 1)

    def predict(self, inputs):
        activation = self.weights[0]
        for weight, value in zip(self.weights[1:], inputs):
            activation += weight * value
        return 1 if activation >= 0 else 0

    def train(self, training_inputs, labels, epochs=10):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                update = self.learning_rate * (label - prediction)
                self.weights[0] += update
                for i in range(len(inputs)):
                    self.weights[i + 1] += update * inputs[i]
