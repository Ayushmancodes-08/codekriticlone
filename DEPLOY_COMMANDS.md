# Quick Deployment - Render + Vercel (100% FREE)

## 1️⃣ Backend → Render.com

1. Go to https://render.com → Sign up with GitHub
2. **New +** → **Web Service**
3. Connect your GitHub repo
4. **Configure:**
   - Root Directory: `frontend/backend`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn server:app --host 0.0.0.0 --port $PORT`
   - Plan: **FREE**

5. **Environment Variables:**
   ```
   SUPABASE_URL=https://iorulrnihsjouawhvcyt.supabase.co
   SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
   SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTA4NDcxMywiZXhwIjoyMDg2NjYwNzEzfQ.gGMaa38l2gSBDjxUuY9sNP6Isx-RuIRvK4Sb08d0IuM
   CORS_ORIGINS=*
   JWT_SECRET_KEY=change-this-in-production
   PORT=10000
   ```

6. **Deploy** → Copy your URL (e.g., `https://codekriti-backend.onrender.com`)

## 2️⃣ Frontend → Vercel

1. Go to https://vercel.com → Sign up
2. **Import** your GitHub repo
3. **Configure:**
   - Root Directory: `frontend`
   - Framework: Create React App
   - Build: `npm run build`

4. **Environment Variables:**
   ```
   REACT_APP_BACKEND_URL=https://YOUR-RENDER-URL.onrender.com
   REACT_APP_SUPABASE_URL=https://iorulrnihsjouawhvcyt.supabase.co
   REACT_APP_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
   REACT_APP_NAME=CODEKRITI4.O
   ```

5. **Deploy** → App is live!

## 3️⃣ Keep-Alive → UptimeRobot

1. Go to https://uptimerobot.com → Sign up
2. **Add Monitor:**
   - URL: `https://YOUR-RENDER-URL.onrender.com/ping`
   - Interval: 5 minutes
3. Done! Backend stays active 24/7

## 4️⃣ Update CORS

Render Dashboard → Environment → Update:
```
CORS_ORIGINS=https://your-vercel-app.vercel.app,*
```

---

**✅ Total Cost: $0/month**

**Login:** `admin` / `admin123`

See DEPLOYMENT_INSTRUCTIONS.md for detailed guide.
