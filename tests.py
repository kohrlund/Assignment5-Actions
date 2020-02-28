import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        # Test radius of 5
        expected = 5*5*3.14159
        self.assertEqual(expected, task.getArea(5))

        # Test radius of 0
        expected = 0
        self.assertEqual(expected, task.getArea(0))

        # Test radius of -1 (invalid)
        expected = None
        assert(task.getArea(-1) is None)
        print("Passed Area Test.")


if __name__ == '__main__':
    unittest.main()
