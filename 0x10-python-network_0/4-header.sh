#!/bin/bash
# Sending header to server
curl -X GET -s --header 'X-School-User-Id: 98' "$1"
