from app import app, db
from models import User
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_home_page_response_code(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status, '200 OK')

    def test_db_connection(self):
        try:
            db.session.query("select 1")
        except Exception:
            self.fail("can't connect to database")

    def test_create_default_user_status(self):
        resp = self.app.get("add-user")
        self.assertEqual(resp.status, '200 OK')

    def test_create_default_user_in_db(self):
        len_before = len(User.query.all())
        self.app.get("add-user")
        len_after = len(User.query.all())
        self.assertEqual(len_after - len_before, 1)

    def test_create_default_user_attrs(self):
        self.app.get("add-user")
        user = db.session.query(User).order_by(User.id.desc()).first()
        self.assertEqual(user.login.replace(" ", ""), 'userEmail@yandex.ru')
        self.assertEqual(user.password.replace(" ", ""), 'userPassword')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
