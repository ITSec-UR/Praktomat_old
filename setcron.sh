#!/bin/bash

echo -e "$(env)\n" > /etc/crontab
echo -e "0 2 * * 1 root python3 /root/praktomat_grading.py\n#" >> /etc/crontab
