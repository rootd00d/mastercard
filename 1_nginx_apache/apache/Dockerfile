FROM centos/httpd:latest

RUN yum install -y \
    crontabs \
    logrotate \
    openssl \
    mod_ssl \
    && cp /etc/cron.daily/logrotate /etc/cron.hourly/logrotate

ADD csr.txt /etc/ssl/certs
WORKDIR /etc/ssl/certs
RUN openssl req -new -sha256 -nodes -newkey rsa:2048 -keyout example.com.key -out example.com.csr -config csr.txt
RUN openssl x509 -req -days 365 -in example.com.csr -signkey example.com.key -sha256 -out example.com.crt
ADD httpd.logrotate /etc/logrotate.d/httpd
ADD virtualhost.conf /etc/httpd/conf.d/virtualhost.conf

EXPOSE 80 443

CMD crond && /run-httpd.sh
