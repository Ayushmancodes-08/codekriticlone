# 🔧 UptimeRobot Configuration Fix

## ⚠️ If 405 Errors Continue After Render Deploys

The code fix has been pushed, but you need to **change UptimeRobot settings** as well!

---

## ✅ Quick Fix: Change Monitor Type in UptimeRobot

### Option 1: Change to HTTP(s) - GET (Recommended)

1. Go to https://uptimerobot.com/dashboard
2. Click on your monitor → **Edit**
3. Find **"Monitor Type"** or **"Request Type"**
4. Change from `HEAD` to **`GET`** ✅
5. Click **Save**

**Why:** GET is more reliable and returns actual response data.

---

### Option 2: Wait for Render Deployment

If Render is still deploying:

1. Go to https://dashboard.render.com
2. Check your `codekriticlone` service
3. Look for **"Deploy in progress..."** or **"Service is live"**
4. If deploying: Wait 1-2 more minutes
5. If live: The HEAD requests should now work!

---

## 🧪 Test the Endpoints Yourself

```bash
# Test with GET (should work)
curl https://codekriticlone.onrender.com/health
# Should return: {"status":"healthy","timestamp":"...","database":"connected"}

# Test with HEAD (should work after deploy)
curl -I https://codekriticlone.onrender.com/health
# Should return: HTTP/1.1 200 OK
```

---

## 🎯 Recommended UptimeRobot Settings

**Monitor #1:**
- URL: `https://codekriticlone.onrender.com/health`
- Monitor Type: **HTTP(s) - GET** ← Change this!
- Interval: 5 minutes

**Monitor #2:**
- URL: `https://codekriticlone.onrender.com/ping`
- Monitor Type: **HTTP(s) - GET** ← Change this!
- Interval: 10 minutes

---

## ✅ After Making Changes

1. Save both monitors with GET method
2. Wait 1 minute
3. Check dashboard
4. Both should show ✅ **UP**
5. Incident will auto-resolve

---

**TL;DR: In UptimeRobot, edit both monitors and change request type to GET instead of HEAD!** 🚀
