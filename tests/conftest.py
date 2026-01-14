import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Set SQLite BEFORE importing server
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from server import app, db


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
        yield test_client
        with app.app_context():
            db.drop_all()