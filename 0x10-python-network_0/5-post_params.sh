#!/bin/bash
# Send POST request with params
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
