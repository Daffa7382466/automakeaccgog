import unittest
from perceptron import Perceptron


class TestPerceptron(unittest.TestCase):
    def test_or_gate(self):
        training_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        labels = [0, 1, 1, 1]
        p = Perceptron(input_size=2)
        p.train(training_inputs, labels, epochs=10)
        predictions = [p.predict(x) for x in training_inputs]
        self.assertEqual(predictions, labels)


if __name__ == "__main__":
    unittest.main()
