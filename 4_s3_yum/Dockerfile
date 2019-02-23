FROM centos:centos7

RUN yum install -y https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm

RUN yum install -y \
    salt-master \
    salt-minion \
    salt-ssh \
    salt-syndic \
    salt-cloud \
    salt-api

ADD minion.conf /etc/salt/minion.d/minion.conf

RUN mkdir -p /srv/salt/foo
