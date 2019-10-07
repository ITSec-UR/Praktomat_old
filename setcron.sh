#!/bin/bash

echo "$(env)\n" > /etc/crontab
echo -e "0 2 * * 2 root python3 /root/praktomat_grading.py\n#" >> /etc/crontab
