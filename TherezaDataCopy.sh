#!/bin/bash

#rsync --dry-run -rv --include '*/' --include 'dens*T*.dat' --exclude '*'\
# --prune-empty-dirs \
#QMCdataforLDA/ QMCdensdatacopy/
 
rsync  -rv --include '*/' --exclude '*/work/*' --include 'entropy*T*.dat' --include 'saf*T*.dat'  --include 'docc*T*.dat'  --include 'dens*T*.dat'  --exclude '*'  \
 --prune-empty-dirs \
QMCdataforLDA/ QMCdatacopy/

rm -r QMCdatacopy/U01
rm -r QMCdatacopy/U02
rm -r QMCdatacopy/U04
rm -r QMCdatacopy/U06
rm -r QMCdatacopy/U07
rm -r QMCdatacopy/U08
rm -r QMCdatacopy/U09

mv  QMCdatacopy/U1 QMCdatacopy/U01 
mv  QMCdatacopy/U2 QMCdatacopy/U02 
mv  QMCdatacopy/U4 QMCdatacopy/U04 
mv  QMCdatacopy/U6 QMCdatacopy/U06 
mv  QMCdatacopy/U7 QMCdatacopy/U07 
mv  QMCdatacopy/U8 QMCdatacopy/U08 
mv  QMCdatacopy/U9 QMCdatacopy/U09

 
