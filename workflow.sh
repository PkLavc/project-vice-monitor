#!/bin/bash
set -e # Exit on any error

# Random sleep between 1 and 300 seconds to avoid collisions
sleep $((RANDOM % 300 + 1))

# Set git user identity
git config user.name "PkLavc"
git config user.email "patrickajm@gmail.com"

# Skip if there are no real changes to commit
if git diff --exit-code history.json index.html uptime-badge.json assets/; then
    echo "No changes detected. Skipping merge."
    exit 0
fi

BRANCH="sre-dashboard-$(date +%Y%m%d-%H%M%S)"
git checkout -b $BRANCH

git add .

# Commit message options (randomized)
MESSAGES=(
    "metrics: update dashboard"
    "stats: sync uptime data"
    "ci: refresh reliability metrics"
    "monitor: update service status"
    "sre: dashboard metrics refresh"
)

ALERT_MESSAGES=(
    "alert: performance degradation detected"
    "alert: significant page size change detected"
    "alert: service disruption detected"
)

# Choose commit message based on monitor.py exit code
if [ "${MONITOR_EXIT_CODE:-0}" -eq 1 ]; then
    RANDOM_INDEX=$((RANDOM % ${#ALERT_MESSAGES[@]}))
    COMMIT_MSG="${ALERT_MESSAGES[$RANDOM_INDEX]}"
else
    RANDOM_INDEX=$((RANDOM % ${#MESSAGES[@]}))
    COMMIT_MSG="${MESSAGES[$RANDOM_INDEX]}"
fi

git commit -m "$COMMIT_MSG" -m "Co-authored-by: pklavc-labs <modderkcaheua@gmail.com>"

# Ensure the branch is up to date before pushing
git fetch origin
git rebase origin/main

git push origin $BRANCH --force

# Create and merge PR with professional metadata
if [ "${MONITOR_EXIT_CODE:-0}" -eq 1 ]; then
    PR_TITLE="🔴 SRE Dashboard: Performance Degradation Detected - $(date +'%Y-%m-%d %H:%M')"
else
    PR_TITLE="🟢 SRE Dashboard: All Systems Operational - $(date +'%Y-%m-%d %H:%M')"
fi

PR_URL=$(gh pr create --title "$PR_TITLE" \
                      --body "Automated SRE observability dashboard update and metrics synchronization.

**Changes:**
- Updated uptime metrics in history.json
- Refreshed SRE dashboard visualizations in index.html
- Generated new SLA metrics and performance data
- Updated Shields.io badge with current uptime percentage

**Services Monitored:**
- GitHub Pages (https://pklavc.github.io/)
- GitHub API (api.github.com/repos/PkLavc/codepulse-monorepo)

**Observability Features:**
- SLA calculations (24h, 7d, 30d)
- Performance metrics (DNS, TCP, Transfer times)
- Incident log tracking
- Security headers analysis
- Deep health checks

**Dashboard:** [index.html](./index.html)" \
                      --base main --head $BRANCH --fill)

echo "Merging PR: $PR_URL"
gh pr merge "$PR_URL" --merge --delete-branch --admin
