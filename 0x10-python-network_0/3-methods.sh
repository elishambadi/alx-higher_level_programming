#!/bin/bash
# Display allowed methods
curl -i -s -L "$1" -o /dev/null | grep Content-Type | sed "s/Content-Type: //g"
