#!/bin/bash
set -e

mkdocs build
rm -rf site/.git
mkdocs gh-deploy

TMP_DIR=$(mktemp -d)

cp -R site/. "$TMP_DIR"

cd "$TMP_DIR"
git init
git add .
git commit -m "update site"

git branch -M main
git remote add origin https://github.com/NavigationBA/NavigationBA_Codes.git
git push -f origin main

cd -
rm -rf "$TMP_DIR"
rm -rf site