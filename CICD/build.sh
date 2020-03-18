#!/usr/bin/env bash


clear
# exit when any command fails
set -e

export PYTHONPATH=$PYTHONPATH:../astroimages-fits/
export FITS_FOLDER=${PWD%/*}/FITS_FOLDER/

echo "------------------------------------------------------------------"
echo "UNIT TESTS"
echo "------------------------------------------------------------------"
python -m unittest discover ./test/unit -v
