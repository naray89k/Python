#! /bin/bash

rename "s/ //" * 
rename "s/ /_/g" *
jupyter nbconvert --to script *.ipynb
chmod 755 *.py
