[![Build Status](https://travis-ci.org/trcook/cong_scrape.svg?branch=master)](https://travis-ci.org/trcook/cong_scrape)

# Setup:
Note: These instructions are specific to systems that can run docker-compose. At the moment, this is limited to osx/linux machines. Additionally, these instructions are oriented towards use on a desktop system.

1. Install Docker.
2. Download the repo and navigate to its root in a shell
    * Technically, you only need the `docker-compose.yml` file. You can just download that and put it in a directory with a subdirectory called `data`
3. Make sure Docker is running and is accessible (i.e. run `eval $(docker-machine env default)`)
4. ensure latest images are installed by running `docker-compose pull`
4. run `docker-compose run --rm get_plaws`
    * This pulls the list of public laws using the spider defined in `./plaw-scraper`
5. Now, run `docker-compose run --rm congress_scrape`
    * This will download the public laws and place them in the folder `./data/data`
    * It will take a long time. And it will re-run a number of times to ensure that it grabs every file requested.

## What you get:

At the end of this, you will have the following:
```
trcook/cong_scrape root:
| ...
├── data
│   ├── active.csv
│   ├── cache
│   │   ├── 93
│   │   ├── 94
│   │   ...
│   │   ├── 113
│   │   └── 114
│   ├── data
│   │   ├── 93
│   │   ├── 94
│   │   ...
│   │   ├── 113
│   │   └── 114
│   ├── log
│   │   ├── RUN_1_NOTCAPTURED.log
│   │   ├── RUN_2_NOTCAPTURED.log
│   │   ...
│   │   ├── RUN_29_NOTCAPTURED.log
│   │   └── RUN_30_NOTCAPTURED.log
| ...

```

`plaw2.csv` and `active.csv` are safe to delete, but they will contain some useful information about lingering files that did not get downloaded. 

You probably want to  keep `plaws.csv` since that has the list of all public laws downloaded and the the corresponding bill numbers.

Ok. Now it's time to search

# Searching

From your terminal (at the bash/shell prompt), at the repo root, call `docker-compose run search_plaws './data' -o ./data/output.csv --regex='REGEX STRING'` to generate search and matches.

```
 docker-compose run search_plaws './data' -o output.csv --regex="(extends(?:\s\w+){0,28}\sFY)"
```
matches FY after extends with as many as 28 words in between

A bunch of pre-compiled patterns are set in allpatterns.sh
in shell (terminal) run:
```
./allpatterns.sh
```

This will generate a file, out.csv that contains provisions and law numbers.


You can also run the regex search directly using: 
```
./plaw_scraper/billsearch/bills.py './data' -o ./data/output.csv --regex='REGEX STRING'
```

This might run a bit faster. but the search script is not really built for speed. It hits some major slowdown when multiple provisions are matched in a single bill using the same regex string. I might return to this at some point to fix it. but at the moment, it's a bit slow. If anyone has a good way of concatenating dictionaries, let me know. 
