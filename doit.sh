#!/bin/sh


while /usr/bin/inotifywait -qe close_write "./*.py"
do
        #pytest
        python -m unittest
done
