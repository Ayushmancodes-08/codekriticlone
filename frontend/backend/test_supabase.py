"""
Quick test script to verify Supabase connection
Run this to test if your Supabase setup is working correctly
"""
import os
import sys
from pathlib import Path

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def test_connection():
    print("🔍 Testing Supabase Connection...")
    print("=" * 50)
    
    # Check environment variables
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_anon_key = os.getenv('SUPABASE_ANON_KEY')
    supabase_service_key = os.getenv('SUPABASE_SERVICE_KEY')
    
    print(f"\n✓ SUPABASE_URL: {supabase_url}")
    print(f"✓ SUPABASE_ANON_KEY: {'*' * 20}...{supabase_anon_key[-10:] if supabase_anon_key else 'NOT SET'}")
    print(f"✓ SUPABASE_SERVICE_KEY: {'*' * 20}...{supabase_service_key[-10:] if supabase_service_key and len(supabase_service_key) > 30 else 'NOT SET or PLACEHOLDER'}")
    
    if not supabase_url or not supabase_service_key:
        print("\n❌ Missing required environment variables!")
        print("   Please check your .env file")
        return False
    
    if supabase_service_key == "service_role_key_here":
        print("\n⚠️  WARNING: service_role key is still a placeholder!")
        print("   Please follow instructions in GET_SERVICE_KEY.md to get your actual key")
        return False
    
    # Try to connect
    try:
        from supabase import create_client
        supabase = create_client(supabase_url, supabase_service_key)
        
        # Test query
        print("\n🔄 Testing database query...")
        result = supabase.table('admins').select('*').execute()
        
        print(f"✅ Connection successful!")
        print(f"   Found {len(result.data)} admin(s) in database")
        
        # List all tables
        print("\n📊 Checking tables...")
        tables = ['admins', 'judges', 'criteria', 'teams', 'scores', 'team_config', 'timer_config']
        for table in tables:
            try:
                result = supabase.table(table).select('*').limit(1).execute()
                print(f"   ✓ {table}")
            except Exception as e:
                print(f"   ✗ {table}: {str(e)}")
        
        print("\n🎉 Supabase is configured correctly!")
        return True
        
    except Exception as e:
        print(f"\n❌ Connection failed: {str(e)}\n")
        print("Common issues:")
        print("  - Service role key is incorrect")
        print("- Project URL is wrong")
        print("  - Tables haven't been created yet")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
