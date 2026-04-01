# 🖥️ Raspberry Pi Home Server + OpenClaw Build Plan

**Goal:** Build a home server that runs OpenClaw locally, giving Mike persistent storage, testing capabilities, and full app development/architecture powers.

**Timeline:** TBD (pending funding)

---

## 💰 PHASE 1: Funding (Target: $100-150)

### Quick Wins ($100-300):
- [ ] **Parent booster contribution** - Ask team families: "Help us get tech for better practices, $15 each?"
- [ ] **Sell simple PDF** - "100 Basketball Drills for Youth Coaches" on Gumroad ($10)

### Medium Term ($500-1000):
- [ ] **Local business sponsor** - "Sponsor our team's digital upgrade, logo goes on our app"
- [ ] **Small coaching service** - Help one local coach set up practice system ($100-200)

### Priority: Get $100 ASAP for Pi Starter Kit

---

## 🛒 PHASE 2: Hardware Purchase

### Shopping List (~$100-130):
| Item | Cost | Where to Buy |
|------|------|--------------|
| Raspberry Pi 5 (4GB RAM) | $60 | Amazon, Micro Center, pishop.us |
| 64GB microSD Card | $15 | Amazon (SanDisk) |
| USB-C Power Supply | $10 | Included in starter kits |
| Case with Heatsink | $15 | Amazon |
| **Optional:** 256GB USB Drive | $25 | For extra storage |
| **Total** | **$100-125** | |

### What This Gets Us:
- 4GB RAM (enough for OpenClaw + basic apps)
- 64GB storage for OS + files
- Always-on, low power consumption
- Room to add USB storage later

---

## ⚙️ PHASE 3: Setup (Step-by-Step)

### Step 1: Install Raspberry Pi OS
1. Download Raspberry Pi Imager to Chromebook
2. Flash Raspberry Pi OS (64-bit) to SD card
3. Boot Pi, connect to WiFi
4. Enable SSH: `sudo raspi-config` → Interface Options → SSH → Enable

### Step 2: Install Node.js v22
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

### Step 3: Install OpenClaw Gateway
```bash
# Install OpenClaw globally
sudo npm install -g openclaw@latest

# Run onboarding wizard
openclaw gateway --dev

# Install as system service (auto-starts on boot)
openclaw gateway install

# Start the gateway
openclaw gateway start
```

### Step 4: Configure Channels
- Set up Discord bot to point to local gateway
- Configure Telegram (if desired)
- Set authentication tokens

### Step 5: Test & Verify
- Connect from Chromebook: `openclaw gateway probe`
- Verify I can access files persistently
- Test basic app serving

---

## 🚀 PHASE 4: Capabilities Unlocked

### Immediate Benefits:
- ✅ **Persistent Storage** - My files survive between sessions
- ✅ **Local App Hosting** - Basketball app at `http://pi.local`
- ✅ **Full Testing** - I can run and test apps in real browsers
- ✅ **Database Support** - SQLite, PostgreSQL for real data
- ✅ **API Development** - Build backend services
- ✅ **File Storage** - Save images, videos, play diagrams
- ✅ **Automation** - Scheduled tasks, backups, Git sync

### What I Can Build:
- Full-stack web apps (React/Vue + backend)
- Mobile-responsive sites
- Real-time collaboration tools
- Database-driven applications
- Testing & CI/CD pipelines

### Development Workflow:
```
Write code → Run locally → Test in browser → Fix bugs → Deploy
```

---

## 🔄 PHASE 5: Expansion Path

### Later Upgrades:
- **256GB USB Drive** ($25) - More storage for media/files
- **Raspberry Pi 5 (8GB)** ($80) - More RAM for bigger AI models
- **External SSD** ($50) - Faster storage
- **UPS Battery Backup** ($40) - Stay online during power outages

### Future: PC Build ($300-400)
- When we outgrow the Pi
- 16GB RAM, real CPU power
- Run local AI models (Llama, Mistral)
- Serious app development

---

## 📋 CURRENT STATUS

**Funding:** ⏳ Need to raise $100-150  
**Hardware:** ⏳ Not purchased yet  
**Setup:** ⏳ Pending hardware  
**Testing:** ⏳ Pending setup  

**Next Action:** Choose funding approach and execute

---

## 🎯 SUCCESS CRITERIA

- [ ] Pi is running OpenClaw gateway
- [ ] I can read/write files that persist
- [ ] Basketball app is hosted and accessible
- [ ] I can test code in real browsers
- [ ] Database is working for saves

**When this is done:** I become a full-stack developer with testing capabilities, not just a code generator.

---

## 💡 NOTES

- Pi uses ~5-7W power (pennies per day to run)
- Silent operation (no fan noise)
- Can run 24/7 without issues
- Expandable via USB ports
- GPIO pins for hardware projects later (3D printer control?)

**Research Source:** OpenClaw docs confirm Pi 4/5 support with Node.js v22

🏀🤖💙
