# Supabase Setup Guide

This guide will help you set up Supabase for the CodeKriti Hackathon Platform.

## Step 1: Create a Supabase Account

1. Go to [https://supabase.com](https://supabase.com)
2. Sign up for a free account
3. Verify your email address

## Step 2: Create a New Project

1. Click "New Project" in your Supabase dashboard
2. Fill in the project details:
   - **Project Name**: `codekriti-hackathon` (or your preferred name)
   - **Database Password**: Choose a strong password and save it securely
   - **Region**: Select the closest region to your users
   - **Pricing Plan**: Free tier is sufficient for most hackathons
3. Click "Create New Project"
4. Wait 2-3 minutes for the project to initialize

## Step 3: Run the Database Schema

1. In your Supabase project dashboard, click on the **SQL Editor** icon in the left sidebar
2. Click "New Query"
3. Copy the entire contents of `backend/supabase_schema.sql`
4. Paste it into the SQL Editor
5. Click **"Run"** to execute the schema
6. Verify success - you should see "Success. No rows returned"

## Step 4: Verify Tables Created

1. Click on the **Table Editor** icon in the left sidebar
2. You should see 7 tables:
   - `admins`
   - `judges`
   - `criteria`
   - `teams`
   - `scores`
   - `team_config`
   - `timer_config`

## Step 5: Get Your API Keys

1. Click on the **Settings** icon (gear) in the left sidebar
2. Click on **API** under Project Settings
3. You'll need two keys:
   - **Project URL**: `https://xxxxxxxxx.supabase.co`
   - **anon public** key: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (long string)
   - **service_role** key: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (different long string)

> **⚠️ IMPORTANT**: The `service_role` key bypasses Row Level Security. Keep it secret and only use it in the backend!

## Step 6: Update Backend Environment Variables

1. Open `backend/.env`
2. Replace the MongoDB configuration with:

```env
SUPABASE_URL="https://your-project-ref.supabase.co"
SUPABASE_ANON_KEY="your-anon-public-key"
SUPABASE_SERVICE_KEY="your-service-role-key"
CORS_ORIGINS="*"
JWT_SECRET_KEY="hackathon-secret-key-change-in-production-123456"
```

3. Replace the placeholder values with your actual Supabase credentials from Step 5

## Step 7: Update Frontend Environment Variables

1. Create or update `frontend/.env`:

```env
REACT_APP_BACKEND_URL=http://localhost:8000
REACT_APP_SUPABASE_URL=https://your-project-ref.supabase.co
REACT_APP_SUPABASE_ANON_KEY=your-anon-public-key
```

## Step 8: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Step 9: Start the Application

```bash
# From the root directory
node start.js

# Or use the platform-specific scripts:
# Windows: start.bat
# PowerShell: start.ps1
# Linux/Mac: ./start.sh
```

## Verification

Once the application starts:

1. The backend should automatically create a default admin user:
   - **Username**: `admin`
   - **Password**: `admin123`

2. Test the connection by logging in at `http://localhost:3000`

## Troubleshooting

### "Cannot connect to database"
- Verify your `SUPABASE_URL` is correct
- Check that your `SUPABASE_SERVICE_KEY` is the service_role key, not the anon key
- Ensure your Supabase project is active (not paused)

### "Tables not found"
- Re-run the `supabase_schema.sql` in the SQL Editor
- Check the Table Editor to confirm all 7 tables exist

### "Authentication failed"
- Make sure the default admin was created (check backend logs)
- Try restarting the backend server

## Optional: Enable Row Level Security (RLS)

If you want to add an extra layer of security using Supabase's built-in RLS:

1. Go to the **Authentication** section in Supabase
2. Enable any desired auth providers
3. In the SQL Editor, uncomment the RLS sections in `supabase_schema.sql`
4. Create RLS policies as needed

For this application, we're using custom JWT auth, so RLS is optional.

## Production Deployment

When deploying to production:

1. **Change the JWT_SECRET_KEY** to a strong, random value
2. **Restrict CORS_ORIGINS** to your frontend domain only
3. **Never commit** `.env` files to version control
4. Consider enabling **Database Backups** in Supabase settings
5. Monitor your **Database Usage** to avoid hitting free tier limits

## Support

- Supabase Documentation: [https://supabase.com/docs](https://supabase.com/docs)
- Supabase Discord: [https://discord.supabase.com](https://discord.supabase.com)
