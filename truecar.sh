#!/usr/bin/env bash

echo 'Scraping truecar.com ....'
rm truecar.csv
scrapy crawl truecar -o truecar.csv -L INFO
echo 'Mission has been completed'