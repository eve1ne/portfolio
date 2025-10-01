#!/bin/bash
# portfoliodb

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Sanity check command line options
usage() {
  echo "Usage: $0 (create|destroy|reset|dump)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

# Parse argument.  $1 is the first argument
case $1 in
  "create")
    mkdir -p var/uploads
    sqlite3 var/portfolio.sqlite3 < sql/schema.sql
    sqlite3 var/portfolio.sqlite3 < sql/data.sql
    cp portfolio/static/uploads/* var/uploads/
    ;;

  "destroy")
    rm -rf var/portfolio.sqlite3 var/uploads
    ;;

  "reset")
    # Remove old database and uploads
    rm -rf var/portfolio.sqlite3 var/uploads

    # Recreate folders
    mkdir -p var/uploads/public
    mkdir -p var/uploads/private

    # Load schema and public data
    sqlite3 var/portfolio.sqlite3 < sql/schema.sql
    sqlite3 var/portfolio.sqlite3 < sql/data_public.sql

    # Load private data if exists
    if [ -f sql/data_private.sql ]; then
        sqlite3 var/portfolio.sqlite3 < sql/data_private.sql
    fi

    # Copy uploads
    cp -r portfolio/static/uploads/public/* var/uploads/public/
    # if [ -d portfolio/static/uploads/private ]; then
        # cp -r portfolio/static/uploads/private/* var/uploads/private/
    # fi
    ;;

  "dump")
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM projects'
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM artworks'
    ;;
  *)
    usage
    exit 1
    ;;
esac
