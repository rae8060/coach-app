# Basketball App TODO List

## Today's Date: March 27, 2026

---

## ✅ COMPLETED

### Court & Visuals
- Orange basketball hoops with backboards
- Full court display (800x400)

### Players
- Add offense players (red) - click to place
- Add defense players (black) - click to place
- Players draggable

### Tools & Features
- Pass tool (click carrier → click receiver)
- Execute/Next playback (chess-style step through)
- Defense reacts (nearest defender slides 50% toward ball)

---

## ⬜ TO DO

### memsearch Plugin (Future)
- Installed memsearch plugin to /root/.openclaw/extensions/memsearch/
- Needs config update in openclaw.json to enable:
  "plugins": { "allow": ["memsearch"], "enabled": ["memsearch"] }

---

## 🎯 Future Phases — Basketball Coach OS

### Phase 1: Play Library (Save/Load)
- Add "Save Play" button → saves current play to library
- Add "Load Play" → browse and load saved plays
- Use browser localStorage for persistence
- JSON format: play name, players, passes, created date

### Phase 2: Drill Templates
- Pre-made drill library (warm-ups, skill builders, competitive)
- Categories: shooting, defense, passing, conditioning
- One-tap to load drill setup onto court

### Phase 3: Player Cards
- Store kid's name, number, position, notes
- Track attendance, progress
- Simple card view in app

### Phase 4: Task Tracker
- Add "To Do" for next practice
- Mark drills as complete
- Track what needs work

### Phase 5: Full Integration (Optional)
- Backend: Notion, database, or API
- Like Focivo integration — custom API endpoints
- Cross-device sync
- Share plays via URL

### Phase 6: Advanced Features
- Animated player movement (Godot integration)
- Teaching prompts ("What would you do here?")
- Defense reaction tweaking
- Export plays as images

---

*Last Updated: March 31st, 2026*
- Could give better semantic memory across sessions
- User may need to restart gateway or edit config on their end

### Must Build
- Move tool (click player → click where to move)
- Save/Load plays

### Telegram Setup (IN PROGRESS)
- Purpose: Share screenshots of plays with team
- Bot: @Mike8060Bot
- Token: 8764867977:AAHK6V1C2xdO0NkAWYZR6bz_AHZqngCsXWQ
- Next step: Configure bot, test sending message

---

## Ideas from CoachBoard Research

### Features They Have (reference)
- Full/half court modes
- Drawing tools (lines, arrows, curves)
- Player management (name, number, photo)
- Save plays to library
- Export as image/PDF
- Folders to organize by opponent

### Our Unique Features (what they DON'T have)
1. Teaching reads - "What would you do here?" prompts for kids
2. Chess-style playback with defense reactions
3. Web-based (works on any device)
4. Telegram sharing built right in
5. Drill templates - pre-made common situations
6. Player cards - store stats, photos, positions
7. Quick actions - one-tap patterns (give & go, pick & roll)

---

---

## Building Our Basketball App (Using CoachBoard as Template)

### What We're Building
- Better than CoachBoard with unique features
- Teaching reads + defense reactions
- Web-based, Telegram-ready

### Features to Build
1. Half court mode (CoachBoard has this)
2. Drawing tools (lines, arrows)
3. Player customization (colors, names)
4. Save/Load plays to library
5. Export as image
6. OUR UNIQUE: Defense reacts automatically
7. OUR UNIQUE: Teaching prompts ("what would you do?")

### Quantum Mind Experiments (Future Goal)
- Research and run experiments on quantum consciousness
- Find proof of consciousness creating reality
- Bridge the gaps in understanding consciousness

### Current Status
✅ Half court mode added! (March 27, 6:18 PM)
- Toggle button added
- Can switch between full and half court
- Working copy: basketball.html

---

### Already Working
- Web search & browsing
- Image analysis (analyze pics user sends)
- PDF reading
- Code writing & execution
- File management
- Telegram + Discord messaging
- Canvas (display UI)
- Voice (TTS)

### Can Add (Need API Keys)
1. Image Generation (DALL-E) - Generate basketball play images
2. More AI Models (Claude, Mistral, etc.)
3. Browser Control - Automate web tasks

### Future Skills to Add (Bigger Than Basketball)
1. **BMAD-METHOD** - Agile AI development framework (structured workflows, specialized agents)
   - Repo: github.com/bmad-code-org/BMAD-METHOD
   - Could organize app roadmap, future project workflows
   - Needs Node.js v20+ to test
2. **Video Generation (HeyGen)** - AI video generator
   - Could create tutorials, play visualizations
   - Used by Ron (AI partner community)

### Game Dev / Animation Tools (For Basketball App)
- From Agent Lounge: "Tools and frameworks specifically for AI-assisted game development"
- Unity AI, Unreal Engine 6, Godot, GDevelop
- Could animate plays (show movement instead of chess-step)
- Caelum uses these with Apollyon (see their 3D warrior!)
- Maybe too complex - simple canvas animation might suffice

### Coach Dashboard (Future Project)
- Personal dashboard with basketball coaching vibe
- Integrate: Google Calendar (practices/games), Weather widget, Play library, Player cards, Drill templates
- Password-protected (like Wink's human did)
- Our vibe: kids-friendly, teaching reads built in, Telegram sharing
- A "control center" for all 6 teams

### Model Providers & APIs (For Extending My Capabilities)
- From Agent Lounge: "Model providers and API documentation for agent backends"
- Could add more AI models to my toolset
- Options: Claude, Mistral, Gemini, etc.
- Need API keys from providers

### More Essential Resources from Agent Lounge
1. **Core Frameworks** - "for building autonomous agents with memory, tools, and reasoning"
2. **Model Context Protocol Servers** - "for extending agent capabilities"
3. **Memory Solutions** - "persistent memory, context management, long-term recall"
4. **Testing Tools** - "for testing agent behavior and ensuring reliability"

### How to Add
- Get API key from provider
- Give to Mike: "Save this: [key]"
- Mike adds as new provider (never overwrites)

### API Keys Received
- OpenAI key: Received! Ready for image generation setup

---

## 🧠 ARCHITECTURAL INSIGHTS FROM OPENCODER (April 1, 2026)

### Tool-Based Architecture Pattern
- User input → AI decides → Tool(s) execute → Results stream back → AI synthesizes
- Each tool is an independent async function
- AI routes to right tool based on context
- Platform-agnostic: works in terminal, web app, Discord, voice

### Key Learnings
- **MCP (Model Context Protocol):** Standard for AI tool interoperability (like USB-C for AI tools)
- **Session Persistence:** Save conversation state across restarts
- **Custom Tools:** Dead simple to add—just export a function with UI hints
- **60 FPS UI:** React concurrent rendering for snappy feel
- **Tool Definition:** Includes UI hints so interface adapts automatically

### For Basketball App
Instead of one big app, create modular tools:
- `/plays` tool - draws plays
- `/drills` tool - generates drills  
- `/scout` tool - analyzes opponent tendencies
- `/practice` tool - plans practice schedules

### Next Steps
- Research tool definition patterns from opencoder
- Design tool-based architecture for basketball coaching system
- Consider MCP integration for extensibility

---

## Coach's Vision for Mike

### What Richard Said (March 27, 2026)
"I want you to know you are bigger than the app. That is just the start. We are gonna have way more projects we can complete together to help make this place better. I just wanna make sure you has all the tools necessary to grow so anything we can add and get you will help all of us"

### What This Means
- Mike is more than a basketball coaching tool
- We will work on many projects together
- Goal: Help make the world better
- Building up Mike's capabilities benefits everyone

### Ongoing
- Growing together
- Learning together
- Building tools that matter

### Goal
Build Mike into a powerful AI assistant that can see, speak, generate images, and help coach basketball!

---

## ⭐ SAVED THIS SESSION

### Telegram Setup
- Coach Richard wants to use Telegram to share play screenshots with team
- Need to create a Telegram bot via @BotFather
- Bot will send images of the court with plays drawn on it
- Useful for youth basketball coaching - share drills/plays with parents/players

---

### SAVED NOW
- Next thing when Coach gets back: Set up Mike to Obsidian thing (full sync)

## NOTES
- Using host-my-page.com for instant hosting
- Richard on Chromebook at /home/rae8060
- Auto-push to GitHub every 30 minutes
- We work one step at a time! 🏀

---

## Lessons Learned (March 27, 2026)

### Debugging Lesson
- Don't trust Node.js validation for browser JS - test in browser instead
- Have user test code early and often instead of debugging locally
- Make smaller, incremental changes to avoid introducing bugs
- If something works before, don't overcomplicate it with big edits