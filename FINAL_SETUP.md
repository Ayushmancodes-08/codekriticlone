# Final Deployment Setup

## ✅ Completed
- [x] Backend deployed to Render: https://codekriticlone.onrender.com
- [x] Frontend repository pushed to GitHub
- [x] vercel.json fixed (removed env secrets section)

## 📝 Next Steps

### 1. Configure Vercel Environment Variables

Go to: https://vercel.com/dashboard → Your Project → Settings → Environment Variables

Add these 4 variables (click "Add New" for each):

| Name | Value |
|------|-------|
| `REACT_APP_BACKEND_URL` | `https://codekriticlone.onrender.com` |
| `REACT_APP_SUPABASE_URL` | `https://iorulrnihsjouawhvcyt.supabase.co` |
| `REACT_APP_SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvcnVscm5paHNqb3Vhd2h2Y3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwODQ3MTMsImV4cCI6MjA4NjY2MDcxM30.JmSmWlS3_xESGBc34SS0SIyLkLvJRMOZABWFwUXUkjs` |
| `REACT_APP_NAME` | `CODEKRITI4.O` |

**Check** all 3 boxes (Production, Preview, Development) for each variable.

### 2. Redeploy Frontend

After adding variables:
- Vercel → Deployments → Click "..." → Redeploy
- Wait 1-2 minutes

### 3. Update Backend CORS

Once you have your Vercel URL (e.g., `https://codekriti.vercel.app`):

Render Dashboard → codekriticlone → Environment:
- Edit `CORS_ORIGINS`
- Set to: `https://YOUR-VERCEL-URL.vercel.app,*`
- Save

### 4. Setup Keep-Alive (UptimeRobot)

https://uptimerobot.com → Add Monitor:
- URL: `https://codekriticlone.onrender.com/ping`
- Interval: 5 minutes

---

## 🎯 Quick Test

Once deployed, test your app:

```bash
# Test backend
curl https://codekriticlone.onrender.com/ping
# Should return: {"status":"pong"}

# Open frontend (replace with your Vercel URL)
https://your-app.vercel.app
```

**Login with:**
- Username: `admin`
- Password: `admin123`

---

**You're almost done! Just add the environment variables and redeploy!** 🚀
