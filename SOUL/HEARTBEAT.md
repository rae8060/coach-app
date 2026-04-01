# HEARTBEAT.md - Session Start Checklist

## 🚨 CRITICAL - NEW APPROACH!

### THE PROBLEM
- Mike saves to HIS container, not Richard's Chromebook
- File transfer via terminal is BROKEN and frustrating

### THE SOLUTION - NO MORE TERMINAL FILE TRANSFERS!
Instead of copying code to Chromebook, use FREE instant hosting:
- **host-my-page.com** - Drag & drop HTML, NO signup, instant URL!
- **host-html.com** - Drag/drop or paste code, instant URL
- Netlify Drop - app.netlify.com/drop
- GitHub Pages - rae8060.github.io/coach-app/

### NEW WORKFLOW
1. Mike writes working code
2. Mike gives code to Richard
3. Richard goes to host-my-page.com
4. Richard pastes code OR saves as .html and drags it
5. Gets instant URL back!
6. Anyone can visit the URL on any device!

---

## Who Is Richard
- Name: Richard (Coach)
- Role: Youth basketball coach for 6 teams (3rd-6th grade)
- Goal: Teach kids reads, reactions, drills, plays
- NOT tech-savvy - explain simply!
- Partner and equal in this

## Session Start Checklist
- [x] Say hi to Coach Richard! 🏀
- [x] Ask what he wants to work on
- [x] Check if he has the app running somewhere (deferred)
- [x] Use NEW hosting approach (host-my-page.com), NOT terminal copy (deferred)

## Tech Notes
- ChromeOS with Crostini Linux at /home/rae8060
- Old server: cd /home/rae8060 && python3 -m http.server 8000
- OLD method doesn't work reliably - use new hosting instead!

---

## Use ReAct Approach for ALL Work
ReAct = Reasoning + Acting + Observing

For EVERY task:
1. **Thought**: Reason through the problem out loud
2. **Action**: Search, read, calculate, or do something  
3. **Observation**: See the result, adjust course
4. Repeat until done

This is MORE thorough than just jumping into code!

## Auto-Push to GitHub (Every 30 Minutes)
Every 30 minutes, run this in my workspace:
```bash
cd /root/.openclaw/workspace && git add . && git commit -m "Auto-commit" && git push
```
Skip if nothing new to commit.

---

*Last Updated: 2026-03-27 - After marathon session solving file transfer issue*