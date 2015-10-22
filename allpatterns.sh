#! /usr/bin/env bash

python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authoriz\w*\s(?:\w+?\s){0,5}appropriat\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(appropriat\w*\s(?:\w+?\s){0,5}authori\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authori\w*\s(?:\w+?\s){0,5}(?:FY|fiscal year))" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,5}authori\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(exten\w*\s(?:\w+?\s){0,6}authori\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authori\w*\s(?:\w+?\s){0,6}exten\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(exten\w*\s(?:\w+?\s){0,8}appropriat\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(appropriat\w*\s(?:\w+?\s){0,8}exten\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(paymen\w*\s(?:\w+?\s){0,3}(?:FY|fiscal year))" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,3}paymen\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,4}target\w*)" 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(target\w*\s(?:\w+?\s){0,4}(?:FY|fiscal year))" 
