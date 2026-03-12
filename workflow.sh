#!/bin/bash
set -e # Para o script se qualquer comando falhar

# Identidade USA Standard para atribuição de conquistas
git config user.name "PkLavc"
git config user.email "patrickajm@gmail.com"

# Verifica se houve mudança real antes de criar PR
if git diff --exit-code history.json index.html; then
    echo "Nenhuma mudança detectada. Pulando merge."
    exit 0
fi

BRANCH="uptime-dashboard-$(date +%Y%m%d-%H%M%S)"
git checkout -b $BRANCH

git add history.json index.html

# Determina a mensagem de commit baseada no código de saída do monitor.py
if [ "$MONITOR_EXIT_CODE" -eq 1 ]; then
    git commit -m "alert: service interruption detected
    
    Automated uptime check detected service interruption.
    Dashboard updated with latest metrics.
    
    Services monitored:
    - GitHub Pages (https://pklavc.github.io/)
    - CodePulse Monorepo (https://pklavc.github.io/codepulse-monorepo/)"
else
    git commit -m "stats: update uptime dashboard metrics
    
    Automated uptime check completed successfully.
    Dashboard updated with latest metrics and visualizations.
    
    Services monitored:
    - GitHub Pages (https://pklavc.github.io/)
    - CodePulse Monorepo (https://pklavc.github.io/codepulse-monorepo/)"
fi

git push origin $BRANCH --force

# Criar e Mesclar PR com metadados profissionais
PR_URL=$(gh pr create --title "📊 Uptime Dashboard: $(date +'%Y-%m-%d %H:%M')" \
                      --body "Automated uptime dashboard update and metrics synchronization.

**Changes:**
- Updated uptime metrics in history.json
- Refreshed dashboard visualizations in index.html
- Generated new statistical data for all services

**Services Monitored:**
- GitHub Pages (https://pklavc.github.io/)
- CodePulse Monorepo (https://pklavc.github.io/codepulse-monorepo/)

**Dashboard:** [index.html](./index.html)

📈 Pull Shark Achievement: Automated dashboard update completed." \
                      --base main --head $BRANCH)

echo "Merging PR: $PR_URL"
gh pr merge "$PR_URL" --merge --delete-branch --admin