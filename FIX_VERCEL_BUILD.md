# ⚡ QUICK FIX: Vercel Build Command Error

## The Problem
Vercel is trying to run `npm run dev` but your package.json doesn't have that script.

---

## ✅ THE FIX (30 seconds)

### In Vercel Dashboard:

1. **Go to:** https://vercel.com/dashboard → Your Project
2. **Click:** Settings → General
3. **Scroll to:** Build & Development Settings

**Change these:**

| Setting | Current (Wrong) | Change To (Correct) |
|---------|----------------|-------------------|
| Root Directory | ❓ | `frontend` |
| Framework Preset | ❓ | **Create React App** |
| Build Command | ❌ `npm run dev` | ✅ `npm run build` |
| Output Directory | ❓ | `build` |
| Install Command | ✅ | `npm install` |

4. **Click "Save"**
5. **Go to Deployments** → Click "..." → **Redeploy**

---

## ✅ Complete Vercel Settings

Copy these exact values:

**Build & Development Settings:**
```
Framework Preset: Create React App
Root Directory: frontend
Build Command: npm run build
Output Directory: build
Install Command: npm install
Development Command: npm start
```

**Environment Variables:** (Settings → Environment Variables)
```
REACT_APP_BACKEND_URL = https://codekriticlone.onrender.com
REACT_APP_SUPABASE_URL = https://iorulrnihsjouawhvcyt.supabase.co
REACT_APP_SUPABASE_ANON_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
REACT_APP_NAME = CODEKRITI4.O
```

---

## 🎯 Quick Checklist

- [ ] Root Directory = `frontend`
- [ ] Framework = Create React App
- [ ] Build Command = `npm run build`
- [ ] Output Directory = `build`
- [ ] All 4 environment variables added
- [ ] Redeployed

---

**After changing the build command to `npm run build`, deployment will work!** 🚀
