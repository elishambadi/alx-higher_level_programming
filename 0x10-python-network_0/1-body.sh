#!/bin/bash
# curling based on status
a=$(curl "$1" -L -s -i| grep HTTP/); if [[ "$a" == *'200'* ]]; then curl -L "$1"; fi

