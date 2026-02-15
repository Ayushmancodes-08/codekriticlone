# 🔄 Complete Keep-Alive Setup (Backend + Database)

## Why This Matters

**Backend (Render):** Free tier sleeps after 15 minutes of inactivity  
**Database (Supabase):** Free tier stays active but connections benefit from regular pings

This guide sets up automatic pinging for BOTH services to ensure 24/7 uptime.

---

## 🎯 Quick Setup (Choose One Method)

### ✅ Method 1: UptimeRobot (Easiest - Recommended)

**Free forever, no configuration needed**

1. **Sign up:** https://uptimerobot.com

2. **Add Monitor #1 - Backend Health:**
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `CodeKriti Backend + DB`
   - URL: `https://codekriticlone.onrender.com/health`
   - Monitoring Interval: `5 minutes`
   - Alert Contacts: Your email

3. **Add Monitor #2 - Lightweight Ping:**
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `CodeKriti Ping`
   - URL: `https://codekriticlone.onrender.com/ping`
   - Monitoring Interval: `10 minutes`
   - Alert Contacts: Your email

**What this does:**
- `/health` endpoint → Checks backend AND database connection every 5 min
- `/ping` endpoint → Lightweight keepalive every 10 min
- Backend stays active 24/7 ✅
- Database connections stay warm ✅

---

### ✅ Method 2: Cron-Job.org (More Control)

1. **Sign up:** https://cron-job.org

2. **Create Job #1 - Health Check:**
   - Title: `CodeKriti Health Check`
   - URL: `https://codekriticlone.onrender.com/health`
   - Schedule: `*/5 * * * *` (every 5 minutes)
   - Save response: Yes (optional)

3. **Create Job #2 - Keep Warm:**
   - Title: `CodeKriti Ping`
   - URL: `https://codekriticlone.onrender.com/ping`
   - Schedule: `*/10 * * * *` (every 10 minutes)

---

### ✅ Method 3: GitHub Actions (Automatic)

**Already set up!** Just add your backend URL as a GitHub secret:

1. **GitHub Repository** → Settings → Secrets → Actions
2. **New secret:**
   - Name: `BACKEND_URL`
   - Value: `https://codekriticlone.onrender.com`
3. **Save**

The workflow in `.github/workflows/keep-alive.yml` will:
- Ping `/health` every 10 minutes (checks backend + database)
- Runs automatically via GitHub Actions
- Free for public repos!

---

## 🔍 What Each Endpoint Does

### `/health` - Full Health Check
```bash
curl https://codekriticlone.onrender.com/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-15T16:30:00Z",
  "database": "connected"
}
```

**What it checks:**
- ✅ Backend is running
- ✅ Database connection is active
- ✅ Supabase query succeeds

**Use for:** Primary monitoring (every 5 min)

---

### `/ping` - Lightweight Ping
```bash
curl https://codekriticlone.onrender.com/ping
```

**Response:**
```json
{
  "status": "pong",
  "timestamp": "2026-02-15T16:30:00Z"
}
```

**What it checks:**
- ✅ Backend responds
- ⚡ Fast (no database query)

**Use for:** Supplementary keepalive (every 10 min)

---

## 📊 Recommended Setup

**For maximum uptime, use BOTH monitors:**

| Service | Endpoint | Interval | Purpose |
|---------|----------|----------|---------|
| UptimeRobot | `/health` | 5 min | Check backend + database |
| UptimeRobot | `/ping` | 10 min | Keep backend warm |

**OR use GitHub Actions** which does both automatically every 10 minutes.

---

## 🧪 Test Your Setup

```bash
# Test health endpoint
curl https://codekriticlone.onrender.com/health
# Should return: {"status":"healthy","database":"connected"}

# Test ping endpoint
curl https://codekriticlone.onrender.com/ping
# Should return: {"status":"pong"}
```

---

## ✅ Setup Checklist

Complete ONE of these:

### Option A: UptimeRobot
- [ ] Created account at uptimerobot.com
- [ ] Added monitor for `/health` (5 min interval)
- [ ] Added monitor for `/ping` (10 min interval)
- [ ] Verified both monitors are green
- [ ] Tested for 1 hour - backend stays active

### Option B: Cron-Job.org
- [ ] Created account at cron-job.org
- [ ] Created cron for `/health` every 5 min
- [ ] Created cron for `/ping` every 10 min
- [ ] Verified both jobs run successfully

### Option C: GitHub Actions
- [ ] Added `BACKEND_URL` secret to GitHub repo
- [ ] Workflow file exists at `.github/workflows/keep-alive.yml`
- [ ] Checked Actions tab - workflow runs every 10 min
- [ ] Verified successful runs

---

## 💡 Pro Tips

**Use Multiple Methods:**
- Primary: UptimeRobot (with email alerts)
- Backup: GitHub Actions
- This redundancy ensures maximum uptime!

**Monitoring Intervals:**
- `/health` every 5 minutes → Catches issues quickly
- `/ping` every 10 minutes → Reduces load
- Combined: Backend never sleeps! 🎉

**Database Benefits:**
- Regular `/health` checks keep Supabase connections active
- Prevents connection timeouts
- Ensures instant response when users access your app

---

## 🎯 Final Test

After setup, wait 30 minutes then test:

1. **Open your app:** https://your-vercel-app.vercel.app
2. **Login immediately** - no cold start delay
3. **Check UptimeRobot dashboard** - 100% uptime
4. ✅ **Success!** Your app is now always-on!

---

**Your backend AND database will now stay active 24/7 for FREE!** 🚀
