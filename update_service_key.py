import requests
import json

# Your Supabase project ref
project_ref = "iorulrnihsjouawhvcyt"

print("=" * 60)
print("📋 INSTRUCTIONS TO GET YOUR SERVICE ROLE KEY")
print("=" * 60)
print()
print("Since I cannot access the Supabase dashboard directly,")
print("please follow these steps:")
print()
print("1. Open this URL in your browser:")
print(f"   https://supabase.com/dashboard/project/{project_ref}/settings/api")
print()
print("2. Scroll down to 'Project API keys' section")
print()
print("3. Find the row labeled 'service_role' with '(secret)' tag")
print()
print("4. Click the 'Reveal' or 'Copy' button")
print()
print("5. Copy the ENTIRE key (it's very long, starts with 'eyJ')")
print()
print("6. Paste it below when prompted")
print()
print("=" * 60)
print()

service_key = input("Paste your service_role key here: ").strip()

if not service_key or service_key == "service_role_key_here":
    print("\n❌ Invalid key! Please try again with the actual key.")
else:
    # Update the .env file
    env_path = "a:/MY_Files/Omm_projects/codekriticlone/frontend/backend/.env"
    
    try:
        with open(env_path, 'r') as f:
            lines = f.readlines()
        
        # Update the service key line
        with open(env_path, 'w') as f:
            for line in lines:
                if line.startswith('SUPABASE_SERVICE_KEY='):
                    f.write(f'SUPABASE_SERVICE_KEY="{service_key}"\n')
                else:
                    f.write(line)
        
        print("\n✅ Service key updated successfully!")
        print("📝 Updated file: frontend/backend/.env")
        print()
        print("Next steps:")
        print("1. Stop the running server (Ctrl+C)")
        print("2. Run: node start.js")
        print("3. Your app should now work!")
        
    except Exception as e:
        print(f"\n❌ Error updating file: {e}")
        print("\nManual update:")
        print(f"1. Open: {env_path}")
        print(f"2. Replace the SUPABASE_SERVICE_KEY line with:")
        print(f'   SUPABASE_SERVICE_KEY="{service_key}"')
