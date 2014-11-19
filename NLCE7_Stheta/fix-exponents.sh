#!/bin/bash

for U in 00 02 04 06 08 10 12 14 16 18 20 22 24 26 28 30;
do
	sed -i '/-10/d' ./3DHubb_U${U}_NLCE_Order7_AvgExtrp_Stheta.dat
	wc ./3DHubb_U${U}_NLCE_Order7_AvgExtrp_Stheta.dat
done
