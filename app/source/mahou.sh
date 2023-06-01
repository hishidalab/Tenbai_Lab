#!/bin/bash

set -eu

LC_CTYPE=C

echo -n "SECRET_KEY = '" > config/settings_local.py
tr -dc 'A-Za-z0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' </dev/urandom | head -c 50 >> config/settings_local.py
echo "'" >> config/settings_local.py