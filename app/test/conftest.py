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
        #db.drop_all()
  

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    username = f"test_user_{uuid.uuid4()}"
    user = User(
        username=username,
        name="Tesst2",
        lastname="Usser2",
        phone="123456789s02",
        email="fabian@gmail.com",
        password="test_psssassword2"  # Asegúrate de hashear la contraseña si es necesario
    )
    db.session.add(user)
    db.session.commit()  # Commit changes within the context
    yield user    
  # Cleanup changes within the context

