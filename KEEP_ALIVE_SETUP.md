# Keep-Alive Cron Setup Guide

## Why You Need This

Free-tier hosting services (Railway, Render, etc.) often put inactive apps to "sleep" after 15-30 minutes of no activity. This guide shows you how to set up automatic pinging to keep your backend always active.

## ✅ Health Endpoints Added

Your backend now has three endpoints:

1. **`GET /`** - Root endpoint with API info
2. **`GET /health`** - Full health check (tests database connection)
3. **`GET /ping`** - Lightweight ping (just returns "pong")

## Setup Options

### Option 1: UptimeRobot (Recommended - Free & Easy)

**Best for: Simple monitoring without configuration**

1. **Go to** https://uptimerobot.com
2. **Sign up** (free account)
3. **Add New Monitor:**
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `CodeKriti Backend`
   - URL: `https://YOUR-BACKEND-URL.railway.app/ping`
   - Monitoring Interval: `5 minutes`
   - Alert Contacts: Your email (optional)

4. **Save** - Done!

**Benefits:**
- ✅ Free forever (50 monitors)
- ✅ Email alerts if backend goes down
- ✅ 5-minute intervals
- ✅ Simple dashboard

---

### Option 2: Cron-Job.org (More Flexible)

**Best for: Custom scheduling**

1. **Go to** https://cron-job.org
2. **Sign up** (free account)
3. **Create Cronjob:**
   - Title: `Keep CodeKriti Alive`
   - Address: `https://YOUR-BACKEND-URL.railway.app/ping`
   - Schedule: Every 5 minutes
   - Enable: Yes

**Benefits:**
- ✅ Free (unlimited jobs)
- ✅ Custom cron expressions
- ✅ Execution history
- ✅ Email notifications

---

### Option 3: Render Cron Jobs (If using Render)

**Best for: Render-hosted backends**

1. **In Render Dashboard:**
2. **Create New Cron Job**
3. **Configure:**
   - Command: `curl https://YOUR-APP.onrender.com/ping`
   - Schedule: `*/5 * * * *` (every 5 minutes)

---

### Option 4: GitHub Actions (Advanced)

**Best for: Already using GitHub**

Create `.github/workflows/keep-alive.yml`:

```yaml
name: Keep Backend Alive

on:
  schedule:
    # Run every 5 minutes
    - cron: '*/5 * * * *'
  workflow_dispatch:

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping backend
        run: |
          curl -X GET https://YOUR-BACKEND-URL.railway.app/ping
          echo "Backend pinged successfully"
```

**Benefits:**
- ✅ No external service needed
- ✅ Free on GitHub
- ✅ Version controlled
- ✅ Easy to modify

---

## Quick Setup (Copy-Paste)

### UptimeRobot Quick Add

```
Monitor Type: HTTP(s)
URL: https://YOUR-BACKEND-URL/ping
Interval: 5 minutes
```

### Cron Expression for 5 Minutes

```
*/5 * * * *
```

### Curl Command to Test

```bash
curl https://YOUR-BACKEND-URL.railway.app/ping
```

**Expected Response:**
```json
{"status":"pong"}
```

---

## Recommended Settings

| Service | Interval | Endpoint |
|---------|----------|----------|
| UptimeRobot | 5 minutes | `/ping` |
| Cron-Job.org | 5 minutes | `/ping` |
| GitHub Actions | 5 minutes | `/ping` |
| Render Cron | 5 minutes | `/health` |

**Why `/ping` instead of `/health`?**
- Faster response (no database check)
- Less resource usage
- Sufficient for keep-alive

**Use `/health` when:**
- You want to monitor database connectivity
- You're setting up alerts
- You need detailed health status

---

## Testing Your Setup

1. **Deploy your backend** to Railway/Render

2. **Test endpoints manually:**
   ```bash
   # Test ping
   curl https://YOUR-BACKEND-URL/ping
   # Should return: {"status":"pong"}
   
   # Test health
   curl https://YOUR-BACKEND-URL/health
   # Should return: {"status":"healthy","timestamp":"..."}
   ```

3. **Set up cron service** (pick one from above)

4. **Wait 30 minutes** and check if backend is still responsive

5. **Check cron logs** to verify pings are working

---

## Troubleshooting

### Cron job fails
**Solution:** Check that your backend URL is correct and HTTPS

### Backend still going to sleep
**Solution:** 
- Verify cron is running (check cron service logs)
- Try reducing interval to 3 minutes
- Make sure you're using Railway/Render (not Vercel serverless)

### Too many requests error
**Solution:** Increase interval to 10 minutes

### Health endpoint returns "unhealthy"
**Solution:** Check Supabase connection and environment variables

---

## Cost & Limits

| Service | Free Tier | Paid |
|---------|-----------|------|
| UptimeRobot | 50 monitors, 5min interval | $7/mo for 1min |
| Cron-Job.org | Unlimited, any interval | Free forever |
| GitHub Actions | 2000 min/month | Free for public repos |
| Render Cron | Included with service | Free |

**Recommended:** Start with **UptimeRobot** or **Cron-Job.org** - both are free and reliable.

---

## Production Checklist

- [ ] Backend deployed to Railway/Render
- [ ] `/ping` endpoint working
- [ ] `/health` endpoint working
- [ ] Cron service set up (UptimeRobot/Cron-Job.org)
- [ ] Tested that backend stays alive for 1+ hour
- [ ] Email alerts configured (optional)
- [ ] Monitoring dashboard bookmarked

---

## Example URLs

Replace `YOUR-BACKEND-URL` with your actual backend URL:

**Railway:**
```
https://codekriti-production.up.railway.app/ping
https://codekriti-production.up.railway.app/health
```

**Render:**
```
https://codekriti-backend.onrender.com/ping
https://codekriti-backend.onrender.com/health
```

---

**Your backend will now stay active 24/7! 🚀**

No more cold starts or sleeping services. Users will always have a fast, responsive experience.
