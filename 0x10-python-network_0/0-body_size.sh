#!/bin/bash
# Script that shows the Content-Length from a HTTP request

curl -s "$1" | wc -c
