FROM centos:centos7

RUN yum clean all && \
    yum -y install rpm-build make gcc

#RUN yum -y install "perl(Error)" "perl(ExtUtils::MakeMaker)"

RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

ADD ./rpm/SOURCES/foo-1.0 /root/rpmbuild/SOURCES/foo-1.0
ADD ./rpm/SPECS/foo.spec /root/rpmbuild/SPECS/foo.spec

VOLUME ["/rpms"]

WORKDIR /root/rpmbuild/SOURCES
RUN tar czf foo-1.0.tar.gz foo-1.0/

WORKDIR /root/rpmbuild
CMD rpmbuild -ba SPECS/foo.spec
