#!/bin/bash
query_fasta=/iobio/fqq/Database_3/Test_Fasta
query_hhm=/iobio/fqq/Database_3/Test_hhm
echo "=============Start running========="

for i in 1A40_A\
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
	sync
		cd /iobio/fqq/Database_3/Test_Fasta
		
	echo "---------------------" $i "---------------------"

	hhblits -i $i.fasta -d /iobio/public/databases/uniclust30_2018_08_hhsuite/uniclust30_2018_08/uniclust30_2018_08 -oa3m $i.a3m -n 3 -cpu 1 -v 0
	echo "=============hhblits over  ==========="
	rm -rf $i.hhr
	mv -f $query_fasta/$i.a3m $query_hhm
	hhmake -i $query_hhm/$i.a3m 
	cd /iobio/fqq/Test_Database/divided_hhm
	# mkdir -p $i/frag_hhm
		
done
	