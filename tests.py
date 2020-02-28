import unittest
import task
from datetime import date


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

    def test4(self):
        list = []
        assert(task.getList(list) is None)

        list.append("Apple")
        assert(task.getList(list) is None)

        list.append("Orange")
        testList = task.getList(list)
        assert(testList[0] == "Apple")
        assert(testList[1] == "Orange")

        list.append("Grapes")
        testList = task.getList(list)
        assert(testList[0] == "Apple")
        assert(testList[1] == "Grapes")

        print("Passed List Test.")

    def test5(self):
        date1 = date(1990, 5, 20)
        date2 = date(1990, 5, 20)
        assert(task.calcDate(date1, date2) == 0)

        date1 = date(1990, 5, 20)
        date2 = date(1990, 6, 20)
        assert(task.calcDate(date1, date2) == 1)

        date1 = date(1990, 5, 20)
        date2 = date(2020, 2, 27)
        assert(task.calcDate(date1, date2) == 10875)


if __name__ == '__main__':
    unittest.main()
