#!/bin/sh

TIMEOUT="5s"


while : ; do
    python3 discBot.py
    echo "Restarting in $TIMEOUT"
    sleep $TIMEOUT
done