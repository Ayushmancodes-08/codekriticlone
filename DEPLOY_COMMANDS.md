# Quick Deployment Commands

## Before You Start
1. Make sure your code is working locally
2. You have a GitHub account
3. You have a Railway account (https://railway.app)
4. You have a Vercel account (https://vercel.com)

## Step 1: Push to GitHub

```bash
cd a:\MY_Files\Omm_projects\codekriticlone

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment - Supabase migration complete"

# Create a new repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy Backend to Railway

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3 Select your repository
4. Set these values:
   - **Root Directory**: `frontend/backend`
   - **Start Command**: `uvicorn server:app --host 0.0.0.0 --port $PORT`
   
5. Add Environment Variables:
   ```
   SUPABASE_URL=https://iorulrnihsjouawhvcyt.supabase.co
   SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
   SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTA4NDcxMywiZXhwIjoyMDg2NjYwNzEzfQ.gGMaa38l2gSBDjxUuY9sNP6Isx-RuIRvK4Sb08d0IuM
   CORS_ORIGINS=*
   JWT_SECRET_KEY=change-this-to-something-secure
   ```

6. Click Deploy and wait ~2-3 minutes
7. **Copy your Railway URL** (e.g., `https://codekriti-production.up.railway.app`)

## Step 3: Deploy Frontend to Vercel

### Option A: Vercel Dashboard (Recommended)

1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

4. Add Environment Variables:
   ```
   REACT_APP_BACKEND_URL = https://YOUR-RAILWAY-URL.railway.app
   REACT_APP_SUPABASE_URL = https://iorulrnihsjouawhvcyt.supabase.co
   REACT_APP_SUPABASE_ANON_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
   REACT_APP_NAME = CODEKRITI4.O
   ```

5. Click "Deploy"

### Option B: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd a:\MY_Files\Omm_projects\codekriticlone
vercel

# Follow prompts, set environment variables when asked

# Deploy to production
vercel --prod
```

## Step 4: Update Backend CORS

Go back to Railway → Your Project → Variables

Update `CORS_ORIGINS` to:
```
CORS_ORIGINS=https://your-vercel-url.vercel.app,*
```

## Step 5: Test Your Deployment

1. Open your Vercel URL
2. Login as admin (username: `admin`, password: `admin123`)
3. Test all features!

---

## Troubleshooting

**Frontend shows "Network Error"**
→ Check REACT_APP_BACKEND_URL is set correctly to your Railway URL

**Backend shows CORS errors**
→ Update CORS_ORIGINS on Railway to include your Vercel domain

**"SUPABASE_URL must be set"**
→ Check environment variables are set on Railway

---

**You're done! 🎉**
