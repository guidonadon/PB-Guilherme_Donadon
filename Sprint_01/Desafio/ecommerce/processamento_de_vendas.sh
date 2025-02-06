#!/bin/bash
mkdir -p /home/guidonadon/ecommerce/vendas
cp /home/guidonadon/ecommerce/dados_de_vendas.csv /home/guidonadon/ecommerce/vendas/dados_de_vendas.csv
mkdir -p /home/guidonadon/ecommerce/vendas/backup | cp /home/guidonadon/ecommerce/dados_de_vendas.csv /home/guidonadon/ecommerce/vendas/backup/dados-$(date +%Y%m%d).csv
find . -name dados-* -exec mv {} /home/guidonadon/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv \;
echo "Data e Hora: $(date '+%Y/%m/%d %H:%M')" >> /home/guidonadon/ecommerce/vendas/backup/relatorio.txt
head -n 2 /home/guidonadon/ecommerce/vendas/dados_de_vendas.csv | tail -n 1 | cut -d',' -f5 >> /home/guidonadon/ecommerce/vendas/backup/relatorio.txt
tail -n 1 /home/guidonadon/ecommerce/vendas/dados_de_vendas.csv | cut -d',' -f5 >> /home/guidonadon/ecommerce/vendas/backup/relatorio.txt
tail -n +2 /home/guidonadon/ecommerce/vendas/dados_de_vendas.csv | wc -l >> /home/guidonadon/ecommerce/vendas/backup/relatorio.txt
head /home/guidonadon/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv >> /home/guidonadon/ecommerce/vendas/backup/relatorio.txt
zip -r /home/guidonadon/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).zip /home/guidonadon/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv
rm /home/guidonadon/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv
rm /home/guidonadon/ecommerce/vendas/dados_de_vendas.csv
