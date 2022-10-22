#!/bin/bash
# Using cURL to show response size in bytes
curl -s -o /dev/null -X GET $1 -D file.txt; cat file.txt | grep Allow | sed 's/Allow: //g';
