cd /Users/tom/Documents/Programming/congress_scrape/bill_info_scraper
drmall
docker kill $(docker ps -a)
docker build -t trcook/congress .
cd /Users/tom/Documents/Programming/congress_scrape
docker-compose build
docker-compose run --rm congress_scrape
docker run --rm -it --entrypoint='/bin/bash' -v $(pwd)/data:/data trcook/congress
