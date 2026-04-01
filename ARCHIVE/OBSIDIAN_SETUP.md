# OpenClaw + Obsidian Setup Guide

## What It Does
- OpenClaw pushes workspace to GitHub every 30 minutes
- Richard pulls into Obsidian vault
- Everything I write becomes searchable, linkable notes

## What We Need From Richard
1. Private GitHub repo (e.g., `openclaw-workspace`)
2. GitHub Personal Access Token (PAT) with `repo` scope
3. Clone the repo on his machine as Obsidian vault
4. Install Obsidian Git plugin (auto-pull every 30 mins)

## Steps Completed by Mike
- [ ] Check if git is installed
- [ ] Initialize git in workspace
- [ ] Set git config user.name/email
- [ ] Add remote with token
- [ ] Initial commit and push
- [ ] Set up auto-commit heartbeat (every 30 mins)

## Status
Richard needs to provide:
- GitHub Personal Access Token
- Repo HTTPS URL