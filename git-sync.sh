#!/bin/bash
# Auto commit + push for ~/naagin

cd ~/naagin || exit

# pull latest first (safer than pushing blindly)
git pull --rebase origin main

# stage all changes
git add .

# commit with timestamp
git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')"

# push to remote
git push origin main
