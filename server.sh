#!/usr/bin/env bash

clear

export PYTHONPATH=$PYTHONPATH:../astroimages-fits/
export FITS_FOLDER=${PWD%/*}/FITS_FOLDER/

./astroimages_api/server.py
