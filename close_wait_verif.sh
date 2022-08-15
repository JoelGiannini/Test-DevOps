#!/bin/bash

#########################################
# Desarrollado por Joel Matias Giannini #
#########################################

v_log="/home/ibmunx/JOEL/close_wait.log"

for i in at3k2vc102 dbacumcompt01 dbacumcompt02 bahq93-11v serve125; do
echo "Server $i" 
comando=`ping -c 3 $i 2> /dev/null`
nofunciona=$?
if [ $nofunciona -eq 0 ] ; then
echo "####### server #######" | tee --append $v_log
v_uname=`ssh -q $i "uname -a"`
echo "$v_uname"|awk '{print $1" "$2}' | tee --append $v_log
echo "####### Fecha #######" | tee --append $v_log
v_date=`ssh -q $i "date"`
echo "$v_date" | tee --append $v_log
echo "####### Verificacion CLOSE_WAIT #######" | tee --append $v_log
ssh -q $i "netstat -an | grep CLOSE_WAIT | grep '8.8.8.8:443'" | awk '{print $1" "$4" "$5" "$6}'| column -t | tee --append $v_log
#ssh -q $i "netstat -an | grep CLOSE_WAIT" | awk '{print $1" "$4" "$5" "$6}'| column -t | tee --append $v_log
echo ""
echo ""

fi



done
