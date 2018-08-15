import unittest
import ImageClassifierData

class Test(unittest.TestCase):
    def test_n_hot(self):
        test_labels = [
            ['cat', 'ant', 'dog'],
            ['plane', 'ant'],
            ['cat'],
        ]

        n_hot, classes = ImageClassifierData.make_n_hot_labels(test_labels)
        self.assertEqual(classes, ['ant', 'cat', 'dog', 'plane'])
        self.assertEqual(n_hot, [[1,1,1,0], [1,0,0,1], [0,1,0,0]])

if __name__ == '__main__':
    unittest.main()