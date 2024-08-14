import pytest
from flaskr.db import get_db

def test_update(client, auth, app):
    auth.login()
    assert client.get("/auth/mod").status_code == 200
    client.post("/auth/mod", data={"new_email": "mod@gmail.com"})

    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        assert user["email"] == "mod@gmail.com"