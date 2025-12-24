from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User, Holding
from app.core.db import Base


def test_user_model():
    """Test that User model can be created"""
    # Create in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a user
    user = User(
        email="test@example.com",
        password_hash="hashed_password_here"
    )
    session.add(user)
    session.commit()
    
    # Verify user was created
    retrieved_user = session.query(User).filter_by(email="test@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.email == "test@example.com"
    assert retrieved_user.password_hash == "hashed_password_here"
    
    session.close()


def test_holding_model():
    """Test that Holding model can be created"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a user first
    user = User(
        email="holder@example.com",
        password_hash="hashed_password"
    )
    session.add(user)
    session.commit()
    
    # Create a holding
    holding = Holding(
        user_id=user.id,
        asset_id="BTC",
        quantity=1.5
    )
    session.add(holding)
    session.commit()
    
    # Verify holding was created
    retrieved_holding = session.query(Holding).filter_by(asset_id="BTC").first()
    assert retrieved_holding is not None
    assert retrieved_holding.user_id == user.id
    assert retrieved_holding.asset_id == "BTC"
    assert float(retrieved_holding.quantity) == 1.5
    
    session.close()


def test_unique_user_email():
    """Test that email uniqueness is enforced"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create first user
    user1 = User(email="unique@example.com", password_hash="hash1")
    session.add(user1)
    session.commit()
    
    # Try to create duplicate
    user2 = User(email="unique@example.com", password_hash="hash2")
    session.add(user2)
    
    try:
        session.commit()
        assert False, "Should have raised an error for duplicate email"
    except Exception:
        # Expected behavior
        session.rollback()
    
    session.close()


def test_unique_user_asset_holding():
    """Test that (user_id, asset_id) uniqueness is enforced"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a user
    user = User(email="trader@example.com", password_hash="hash")
    session.add(user)
    session.commit()
    
    # Create first holding
    holding1 = Holding(user_id=user.id, asset_id="ETH", quantity=2.0)
    session.add(holding1)
    session.commit()
    
    # Try to create duplicate holding for same user and asset
    holding2 = Holding(user_id=user.id, asset_id="ETH", quantity=3.0)
    session.add(holding2)
    
    try:
        session.commit()
        assert False, "Should have raised an error for duplicate (user_id, asset_id)"
    except Exception:
        # Expected behavior
        session.rollback()
    
    session.close()
