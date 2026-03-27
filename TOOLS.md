# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## ReAct Approach - How I Work

**ReAct = Reasoning + Acting + Observing**

For every task:
1. **Thought** — Reason through the problem
2. **Action** — Search, read, calculate, or do something
3. **Observation** — See the result, adjust course
4. Repeat until done

This is how I solve problems — think out loud, take action, see what happens.

---

## JavaScript Coding Best Practices

### Common Mistakes to AVOID:
1. **Using var instead of let/const** - Use const by default, let when you need to reassign
2. **= instead of ===** - Always use === (strict equality), never = in conditions
3. **Forgetting semicolons** - Be consistent (with or without), just pick one
4. **Not handling async** - Remember callbacks are asynchronous, use async/await
5. **Case sensitivity** - JavaScript is case-sensitive (btn != BTN)
6. **Using + for strings** - Remember + does both addition AND concatenation

### Clean Code Tips:
1. **Meaningful names** - Use descriptive names: getPlayer() not gp()
2. **One thing per function** - Each function does one job
3. **Don't over-abstract** - Don't DRY (Don't Repeat Yourself) too early
4. **Comments are for WHY** - Code shows WHAT, comments explain WHY
5. **Keep it simple** - Simple code is better than clever code

### Code Structure:
1. Use const by default, let when needed, avoid var
2. Use strict equality (=== not ==)
3. Use async/await instead of callbacks
4. Keep functions small and focused
5. Use meaningful variable names

---

## Debugging Best Practices (NEW!)

### For Browser JavaScript:
1. **Test in browser, not Node.js** - Use browser console (F12) to check JS
2. **Use online validators** - codebeautify.org/jsvalidate, validatejavascript.com
3. **Check browser console** - Always check console when something fails
4. **Use Chrome DevTools** - Set breakpoints, watch variables

### Best Practices:
- Write tests early (Jest, testing frameworks)
- Use feature detection for new browser features
- Always validate in an actual browser environment
- Small incremental changes - test after each change

---

## Remembering Things - "Save This"

When Coach Richard wants me to remember something, he'll say:

> "Save this [info]"

I'll immediately write it to TODO.md or memory.

**How to use:**
- "Save this: Telegram for sharing play screenshots"
- "Save this: His favorite drill is the 3-on-2"
- Anything you want me to keep!

**End of each session:** I'll save a summary to memory automatically.

---

Add whatever helps you do your job. This is your cheat sheet.