# Vercel Environment Variables Setup

## Your Backend URL
✅ **Backend deployed:** https://codekriticlone.onrender.com

## Step-by-Step Instructions

### 1. Go to Vercel Dashboard
- Open: https://vercel.com/dashboard
- Click on your `codekriti` project

### 2. Navigate to Settings
- Click **Settings** tab
- Click **Environment Variables** in left sidebar

### 3. Add Each Variable

Click **"Add New"** for each of these:

#### Variable 1:
```
Name: REACT_APP_BACKEND_URL
Value: https://codekriticlone.onrender.com
Environment: Production, Preview, Development (check all)
```

#### Variable 2:
```
Name: REACT_APP_SUPABASE_URL
Value: https://iorulrnihsjouawhvcyt.supabase.co
Environment: Production, Preview, Development (check all)
```

#### Variable 3:
```
Name: REACT_APP_SUPABASE_ANON_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
Environment: Production, Preview, Development (check all)
```

#### Variable 4:
```
Name: REACT_APP_NAME
Value: CODEKRITI4.O
Environment: Production, Preview, Development (check all)
```

### 4. Save All Variables
- Click **Save** for each variable

### 5. Redeploy
- Go to **Deployments** tab
- Click the **three dots (...)** on the latest deployment
- Click **Redeploy**
- Wait 1-2 minutes

## Then Update Backend CORS

### 1. Go to Render Dashboard
- Open: https://dashboard.render.com
- Click on your `codekriticlone` service

### 2. Update CORS
- Click **Environment** in left sidebar
- Find `CORS_ORIGINS`
- Click **Edit**
- Change to: `https://your-vercel-url.vercel.app,*`
- Click **Save**

(Replace `your-vercel-url.vercel.app` with your actual Vercel domain)

---

✅ **That's it! Your app should now work perfectly!**

Test by opening your Vercel URL and logging in as:
- Username: `admin`
- Password: `admin123`
