#!/usr/bin/env bash

echo 'Scraping autotrader.com ....'
rm autotrader.csv
scrapy crawl autotrader -o autotrader.csv -L INFO
echo 'Mission has been completed'