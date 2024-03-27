import unittest
import src


class TestApp(unittest.TestCase):

    def test_run_application(self):
        data = src.run_application()
        self.assertEqual(data, "PNG")


if __name__ == '__main__':
    unittest.main()