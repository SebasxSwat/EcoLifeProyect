from app import create_app, db
import pytest
from app.models.user import User
import uuid

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables within the context
        yield app
        db.session.remove()  # Cleanup session objects
        db.drop_all()
  

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    username = f"test_user_{uuid.uuid4()}"
    email = f"test_user_{uuid.uuid4()}@gmail.com"  
    user = User(
        username=username,
        name="Tesst2",
        lastname="Usser2",
        phone="123456789s02",
        email=email,
        password="test_psssassword2"  
    )
    db.session.add(user)
    db.session.commit()  
    yield user
