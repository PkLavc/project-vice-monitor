#!/bin/bash
set -e # Para o script se qualquer comando falhar

# Identidade USA Standard para atribuição de conquistas
git config user.name "PkLavc"
git config user.email "patrickajm@gmail.com"

# Verifica se houve mudança real antes de criar PR
if git diff --exit-code history.json index.html uptime-badge.json; then
    echo "Nenhuma mudança detectada. Pulando merge."
    exit 0
fi

BRANCH="sre-dashboard-$(date +%Y%m%d-%H%M%S)"
git checkout -b $BRANCH

git add .

# Determina a mensagem de commit baseada no código de saída do monitor.py
if [ "${MONITOR_EXIT_CODE:-0}" -eq 1 ]; then
    git commit -m "alert: performance degradation detected" -m "Co-authored-by: pklavc-labs <modderkcaheua@gmail.com>"
else
    git commit -m "stats: update uptime dashboard metrics" -m "Co-authored-by: pklavc-labs <modderkcaheua@gmail.com>"
fi

# Garante sincronização do branch antes do push
git fetch origin
git rebase origin/main

git push origin $BRANCH --force

# Criar e Mesclar PR com metadados profissionais
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

**Dashboard:** [index.html](./index.html)

🚀 SRE Achievement: Automated observability update completed." \
                      --base main --head $BRANCH --fill)

echo "Merging PR: $PR_URL"
gh pr merge "$PR_URL" --merge --delete-branch --admin
