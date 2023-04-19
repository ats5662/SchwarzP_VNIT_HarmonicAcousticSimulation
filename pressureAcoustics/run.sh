#!/bin/sh
7z x SchwarzPLinerMeshMeterTet4.7z
cfs -t8 -d InputDeck
rm *.cdb
cp history/* .
rm -rf history
python postProcessResults.py
