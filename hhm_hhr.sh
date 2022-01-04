#!/bin/bash
hhm=/iobio/fqq/Database_3/divided_hhm
cd /iobio/fqq/Database_3/divided_hhm
for file in 1A40_A\
		1A7D_A\
		1A91_A\
		1ABV_A\
		1AK6_A\
		1AOX_A\
		1AUU_A\
		1B4R_A\
		1BJX_A\
		1C9F_A\
		1CF7_B\
		1CTO_A\
		1D8B_A\
		1DL6_A\
		1DUN_A\
		1E3Y_A\
		1EKZ_A\
		1ELW_A\
		1F15_C\
		1F43_A\
		1F93_A\
		1FEX_A\
		1FJG_F\
		1FSU_A\
		1GPQ_B\
		1GXL_A\
		1GYH_A\
		1H9E_A
	
do
	cd /iobio/fqq/Database_3/divided_hhm/$file/frag_hhm
	for files in $(ls *)
	
	do
		j=${files%.*}
	echo "======================" $j"======================"
		hhsearch -i $hhm/$file/frag_hhm/$j.hhm -d /iobio/fqq/database/last_DataBase/pdb25 -z 50

	done
done
  