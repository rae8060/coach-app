# Basketball App Research - Court Design

## Court Colors (Verified Working on Chromebook)
- Floor: #B49860 (tan)
- Lines: #fff (white)  
- Paint areas: rgba(128,0,128,0.3) (purple with transparency)
- Borders: #8B4513 (brown)

## Hoop Design (ORANGE + WHITE = VISIBLE)
- Rim: Orange circle (#ff6600) with WHITE border (#fff, lineWidth=2)
- Backboard: White vertical rectangle (#fff)
- Size: Small radius (12 pixels)
- Both sides must have white outline to stand out against tan floor

## Court Structure (800x400 canvas)
1. Center line (vertical)
2. Center circle (radius 50)
3. Paint rectangles (key): 150x100 and 150x140
4. Free throw circles (radius 50)
5. 3-point arcs (radius 150)
6. Corner lines from baseline

## Key Lesson
- Orange hoops blend into tan court (#B49860) without white outline
- ALWAYS add white stroke around orange rim for visibility
- Use named colors or verify hex colors work on Chromebook

## WORKING BASE VERSION (Saved!)
- File: basketball-court-base.html
- Date: 2026-03-27 (Late night session)
- Contains: Full court with both hoops visible
- This is the starting point for future development

## What To Build Next (From This Base)
1. Add players (click to add offense/defense)
2. Pass/Move tools
3. Execute queue
4. Defense reactions
5. Zone dropdown
6. Save/Load

## User's Goal
- Build basketball coaching app for youth teams
- Use on Chromebook
- Simple, step-by-step instructions

---

*Last Updated: 2026-03-27 (Late night session)*