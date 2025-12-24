#!/usr/bin/env python3
"""Quick verification script to test the setup"""
import requests
import sys

def test_server():
    """Test if the server is responsive"""
    try:
        response = requests.get("http://localhost:8001/health", timeout=5)
        print(f"✅ Server is running!")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running on port 8001")
        print("   Start it with: cd api && uvicorn app.main:app --reload --port 8001")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_database():
    """Test database connection and models"""
    from sqlalchemy import text
    from app.core.db import engine
    from app.models.user import User, Holding
    
    try:
        # Test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            assert result.scalar() == 1
        
        print("✅ Database connection successful!")
        print(f"   Database URL: {engine.url}")
        
        # Test that tables exist
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        assert 'users' in tables, "users table not found"
        assert 'holdings' in tables, "holdings table not found"
        
        print(f"✅ Database tables exist: {tables}")
        return True
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing NetWorth API Setup\n")
    
    # Test database first (doesn't require server)
    db_ok = test_database()
    print()
    
    # Test server
    server_ok = test_server()
    print()
    
    if db_ok and server_ok:
        print("🎉 All checks passed! Step 0 is complete.")
        print("\n📝 Next steps:")
        print("   1. Implement auth endpoints (/auth/register, /auth/login)")
        print("   2. Create JWT middleware")
        print("   3. Implement holdings CRUD")
        sys.exit(0)
    else:
        print("⚠️  Some checks failed. Review the errors above.")
        sys.exit(1)
