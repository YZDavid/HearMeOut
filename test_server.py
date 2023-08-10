from server import app
import unittest

class ServerTest(unittest.TestCase):

    # Access Homepage
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Access About Page
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Access Summariser
    def test_summariser(self):
        tester = app.test_client(self)
        response = tester.get("/summariser")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Access URL Summariser
    def test_url_summariser(self):
        tester = app.test_client(self)
        response = tester.get("/url_summariser")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Access Latest Conversions
    def test_latest(self):
        tester = app.test_client(self)
        response = tester.get("/latest")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Access History
    def test_history(self):
        tester = app.test_client(self)
        response = tester.get("/history")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

if __name__ == "__main__":
    unittest.main()