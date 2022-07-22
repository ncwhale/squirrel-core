@echo off

cd %~dp0/..

poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --dev --output requirements.dev.txt

@echo on