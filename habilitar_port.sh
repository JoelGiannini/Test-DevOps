#!/bin/bash
/usr/bin/firewall-cmd --zone=public --add-port=10050/tcp
sleep 5
/usr/bin/firewall-cmd --reload
