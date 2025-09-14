# OSINT Harvester Report

Скрипт превращает JSON-вывод theHarvester в интерактивный HTML-отчёт:
- вкладки: Hosts / IPs / Emails / Sources / TLDs
- подсветка рисков (High / Medium / Info)
- быстрые ссылки: crt.sh, urlscan, VirusTotal, Shodan, Censys, SecurityTrails, dnstwist
- экспорт в CSV / Excel / PDF / Print
- тёмная тема
- *_summary.json для автоматики (CI/алертов)

## Использование
```bash
python3 json2html_ultra_max.py \
  -i ./examples/harvester_*.json \
  -o ./reports/index.html \
  --title "OSINT Report: example.com" \
  --export-csv

open ./reports/index.html


---

# 2) Скрипт запуска
```bash
mkdir -p scripts reports examples .github/workflows
cat > scripts/harvest-report.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
TITLE="${1:-OSINT Harvester Report}"
IN_GLOB="${2:-./examples/*.json}"
OUT="./reports/index.html"

mkdir -p reports
python3 ./json2html_ultra_max.py -i ${IN_GLOB} -o "${OUT}" --title "${TITLE}" --export-csv
echo "Report saved to ${OUT}"
