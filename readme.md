# Setup:
Note: These instructions are specific to systems that can run docker-compose. At the moment, this is limited to osx/linux machines. Additionally, these instructions are oriented towards use on a desktop system.

1. Install Docker.
2. Download the repo and navigate to its root in a shell
    * Technically, you only need the `docker-compose.yml` file. You can just download that and put it in a directory with a subdirectory called `data`
3. Make sure Docker is running and is accessible (i.e. run `eval $(docker-machine env default)`)
4. run `docker-compose run --rm get_plaws`
    * This pulls the list of public laws using the spider defined in `./plaw-scraper`
5. Now, run `docker-compose run congress_scrape`
    * This will download the public laws and place them in the folder `./data/data`
    * It will take a long time. And it will re-run a number of times to ensure that it grabs every file requested.
6. Now it's time to search

# Searching

Call `docker-compose run search_plaws './data' -o ./data/output.csv --regex='REGEX STRING'` to generate search and matches.

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
