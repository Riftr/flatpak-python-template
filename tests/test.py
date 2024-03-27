import unittest
import my_sample_app


class TestApp(unittest.TestCase):

    def test_run_application(self):
        data = my_sample_app.run_application()
        self.assertEqual(data, "PNG")


if __name__ == '__main__':
    unittest.main()
