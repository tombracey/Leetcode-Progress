#!/bin/bash

# Count the problems solved and create a new graph
python progress_tracking/progress_tracker.py
python progress_tracking/plot.py

# Overwrites README to ensures the progress image updates - had issues with it caching
timestamp=$(date +%s)
cat <<EOF > README.md
## LeetCode Progress
Auto-updates on push:

![Progress Graph](progress_tracking/progress.png?v=$timestamp)

I'm starting with the [SQL 50 Study Plan](https://leetcode.com/studyplan/top-sql-50/)
EOF

# Push to GitHub
git add .
git commit -m "Pushed by submit.sh"
git push
