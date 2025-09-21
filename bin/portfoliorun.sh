#!/bin/bash
# portfoliorun

if [ ! -f var/portfolio.sqlite3 ]; then
  echo -e "Error: can't find database var/portfolio.sqlite3 \nTry: ./bin/portfoliodb create"
  exit 1
fi

flask --app portfolio --debug run --host 0.0.0.0 --port 8000
