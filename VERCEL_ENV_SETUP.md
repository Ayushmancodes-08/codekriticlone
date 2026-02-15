# ⚡ VERCEL ENVIRONMENT VARIABLES - COPY & PASTE

## ✅ Backend is Live
https://codekriticlone.onrender.com

---

## 📝 HOW TO ADD ENVIRONMENT VARIABLES IN VERCEL

### Step 1: Go to Vercel Dashboard
https://vercel.com/dashboard

### Step 2: Click Your Project
Find your `codekriti` or `codekriticlone` project

### Step 3: Go to Settings
Click **Settings** → **Environment Variables**

### Step 4: Add These 4 Variables

**IMPORTANT: Just copy and paste the values exactly as shown below!**

---

### ✅ Variable 1

**Key:**
```
REACT_APP_BACKEND_URL
```

**Value:**
```
https://codekriticlone.onrender.com
```

**Environment:** Check ✅ Production, ✅ Preview, ✅ Development

---

### ✅ Variable 2

**Key:**
```
REACT_APP_SUPABASE_URL
```

**Value:**
```
https://iorulrnihsjouawhvcyt.supabase.co
```

**Environment:** Check ✅ Production, ✅ Preview, ✅ Development

---

### ✅ Variable 3

**Key:**
```
REACT_APP_SUPABASE_ANON_KEY
```

**Value:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs
```

**Environment:** Check ✅ Production, ✅ Preview, ✅ Development

---

### ✅ Variable 4

**Key:**
```
REACT_APP_NAME
```

**Value:**
```
CODEKRITI4.O
```

**Environment:** Check ✅ Production, ✅ Preview, ✅ Development

---

## 🎯 After Adding All Variables

1. Click **Save** for each variable
2. Go to **Deployments** tab
3. Click the **...** menu on latest deployment
4. Click **Redeploy**
5. Wait 2 minutes
6. ✅ Done!

---

## ⚙️ ALSO CHECK PROJECT SETTINGS

Make sure these are correct:

**Framework Preset:** Create React App  
**Root Directory:** `frontend`  
**Build Command:** `npm run build`  
**Output Directory:** `build`  
**Install Command:** `npm install`

---

## 🧪 Test After Deployment

Open your Vercel URL and try:
- Login as admin: `admin` / `admin123`
- If it works → Success! 🎉
- If not → Check browser console for errors

---

## 🔧 Common Issues

**"Network Error"**
→ Double-check `REACT_APP_BACKEND_URL` is exactly: `https://codekriticlone.onrender.com`

**CORS Error**
→ Go to Render → Environment → Set `CORS_ORIGINS` to: `https://your-vercel-url.vercel.app,*`

**Build Fails**
→ Check Root Directory is `frontend` not empty

---

**That's it! Just copy-paste these values exactly! 🚀**
