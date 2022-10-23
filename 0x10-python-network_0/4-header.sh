#!/bin/bash
# Sending header to server
curl -X -s GET --header 'X-School-User-Id: 98' "$1"
