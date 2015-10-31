#! /usr/bin/env bash

python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:authoriz\w*\s(?:\w+?\s){0,5}appropriat\w*)[^\.]+?[\.])" --min

# template this line if keyword at beginning of sentance
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)(?:Authoriz\w*\s(?:\w+?\s){0,5}appropriat\w*)[^\.]+?[\.])" --min
# This should get sentence before authorize appropriations at start of sentence
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "
((?:\.\s|\n|^)[A-Z](?:\w|\s)+?\.\sAuthoriz\w*\s(?:\w+?\s){0,5}appropriat\w*)[^\.]+?[\.])" --min

python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:appropriat\w*\s(?:\w+?\s){0,5}authori\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:authori\w*\s(?:\w+?\s){0,5}(?:FY|fiscal year))[^\.]+?[\.])"    --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:\s(?:FY|fiscal year)\s(?:\w+?\s){0,5}authori\w*)[^\.]+?[\.])"   --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:exten\w*\s(?:\w+?\s){0,6}authori\w*)[^\.]+?[\.])"              --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:authori\w*\s(?:\w+?\s){0,6}exten\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:exten\w*\s(?:\w+?\s){0,8}appropriat\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:appropriat\w*\s(?:\w+?\s){0,8}extend\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:paymen\w*\s(?:\w+?\s){0,3}(?:FY|fiscal year))[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:\s(?:FY|fiscal year)\s(?:\w+?\s){0,3}paymen\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:\s(?:FY|fiscal year)\s(?:\w+?\s){0,4}target\w*)[^\.]+?[\.])"  --min
python ./plaw_scraper/billsearch/bills.py "./data" -o out.csv --regex "((?:^|\n|\.\s)[A-Z][^\.]+?(?:target\w*\s(?:\w+?\s){0,4}(?:FY|fiscal year))[^\.]+?[\.])"  --min
