#!/bin/bash
#n=0;
#
#echo " ";
#echo "Converting:"
#echo " ";
#
#for pngfile in "$@"; do
#
#  jpgfile=${epsfile%.eps}.jpg
#
#  echo "$((++n)): $epsfile to $jpgfile."
#
#  convert -density 300x300 $epsfile $jpgfile
#
#done
#
#echo " ";
#echo "$((n)) files were converted from EPS to JPG format."
cd figs2
#for i in $(find . | grep eps); do
for AFILE in $(find . -iname "*.eps"); do
#    echo ${AFILE} "${AFILE%.*}".png;
    convert ${AFILE} "${AFILE%.*}".png;
#    echo "${AFILE}";
#    echo "${AFILE%.*}";
#    convert ${i} "${AFILE%%.*}".png;
done
