#! /usr/bin/env bash

python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authoriz\w*\s(?:\w+?\s){0,5}appropriat\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(appropriat\w*\s(?:\w+?\s){0,5}authori\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authori\w*\s(?:\w+?\s){0,5}(?:FY|fiscal year))" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,5}authori\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(exten\w*\s(?:\w+?\s){0,6}authori\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(authori\w*\s(?:\w+?\s){0,6}exten\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(exten\w*\s(?:\w+?\s){0,8}appropriat\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(appropriat\w*\s(?:\w+?\s){0,8}exten\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(paymen\w*\s(?:\w+?\s){0,3}(?:FY|fiscal year))" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,3}paymen\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(\s(?:FY|fiscal year)\s(?:\w+?\s){0,4}target\w*)" -k 
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "(target\w*\s(?:\w+?\s){0,4}(?:FY|fiscal year))" -k 
