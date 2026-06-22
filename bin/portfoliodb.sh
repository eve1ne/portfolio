#!/bin/bash
# portfoliodb
set -Eeuo pipefail

usage() {
  echo "Usage: $0 (create|destroy|reset|dump)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

case $1 in
  "create")
    mkdir -p var/uploads/assets
    mkdir -p var/uploads/public
    mkdir -p var/uploads/cs
    mkdir -p var/uploads/media
    mkdir -p var/uploads/animation
    sqlite3 var/portfolio.sqlite3 < sql/schema.sql
    sqlite3 var/portfolio.sqlite3 < sql/data.sql
    cp -r portfolio/static/uploads/* var/uploads/
    ;;

  "destroy")
    rm -rf var/portfolio.sqlite3 var/uploads
    ;;

  "reset")
    rm -rf var/portfolio.sqlite3 var/uploads
    mkdir -p var/uploads/assets
    mkdir -p var/uploads/public
    mkdir -p var/uploads/cs
    mkdir -p var/uploads/media
    mkdir -p var/uploads/animation

    sqlite3 var/portfolio.sqlite3 < sql/schema.sql
    sqlite3 var/portfolio.sqlite3 < sql/data.sql

    if [ -f sql/data_private.sql ]; then
      sqlite3 var/portfolio.sqlite3 < sql/data_private.sql
    fi

    # only copy if source folder exists and has content
    [ -d portfolio/static/uploads/assets ]    && cp -r portfolio/static/uploads/assets/*    var/uploads/assets/
    [ -d portfolio/static/uploads/public ]    && cp -r portfolio/static/uploads/public/*    var/uploads/public/
    [ -d portfolio/static/uploads/cs ]        && cp -r portfolio/static/uploads/cs/*        var/uploads/cs/
    [ -d portfolio/static/uploads/media ]     && cp -r portfolio/static/uploads/media/*     var/uploads/media/
    [ -d portfolio/static/uploads/animation ] && cp -r portfolio/static/uploads/animation/* var/uploads/animation/
  ;;

  "dump")
    echo "=== work_sections ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM work_sections'

    echo "=== cs_projects ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM cs_projects'

    echo "=== cs_project_roles ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM cs_project_roles'

    echo "=== cs_project_sections ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM cs_project_sections'

    echo "=== cs_section_highlights ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM cs_section_highlights'

    echo "=== art_projects ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM art_projects'

    echo "=== art_project_media ==="
    sqlite3 -batch -line var/portfolio.sqlite3 'SELECT * FROM art_project_media'
    ;;

  *)
    usage
    exit 1
    ;;
esac
