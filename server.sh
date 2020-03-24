#!/usr/bin/env bash

clear

export PYTHONPATH=$PYTHONPATH:../astroimages-fits/:../astroimages-file-drivers
export FITS_FOLDER=${PWD%/*}/FITS_FOLDER/

./astroimages_api/server.py
