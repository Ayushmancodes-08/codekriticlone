# Getting Your Supabase Service Role Key

Since the browser tool is unavailable, please follow these steps to get your service role key:

## Steps:

1. **Go to Your Supabase Dashboard**
   - URL: https://supabase.com/dashboard/project/iorulrnihsjouawhvcyt/settings/api

2. **Find the Service Role Key**
   - Scroll down to the "Project API keys" section
   - Look for "service_role" (secret)
   - Click the "Reveal" button next to it
   - Copy the entire key (starts with `eyJ`)

3. **Update the Backend .env File**
   - Open: `frontend/backend/.env`
   - Replace the line:
     ```
     SUPABASE_SERVICE_KEY="service_role_key_here"
     ```
   - With:
     ```
     SUPABASE_SERVICE_KEY="eyJ...your-actual-service-role-key..."
     ```
   
4. **Save the file**

## ⚠️ IMPORTANT
The service_role key is different from the anon key and should be kept SECRET. Never commit it to version control!

## Why We Need It
The backend uses the service_role key to bypass Row Level Security policies and perform admin operations on the database.
