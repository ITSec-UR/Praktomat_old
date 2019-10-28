FROM python:3.6.8


LABEL maintainer="Christoph Schreyer <christoph.schreyer@stud.uni-regensburg.de>"


# Install required packages
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install \
 cron \
 python3-pip
RUN pip3 install psycopg2


# Add required scripts
COPY praktomat_grading.py /root/praktomat_grading.py
COPY setcron.sh /root/setcron.sh
RUN chmod +x /root/setcron.sh


# CMD ["sh", "-c", "/tmp/setcron.sh && /usr/sbin/cron && /bin/cat"]
