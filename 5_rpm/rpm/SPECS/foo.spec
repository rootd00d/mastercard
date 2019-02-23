Name:           foo
Version:        1.0
Release:        1%{?dist}
Summary:        bazzerific

Group:          Mastercard
BuildArch:      x86_64
License:        Unlicense
Source0:        foo-1.0.tar.gz

%description
Foobity doo baz bar

%prep
rm -rf $RPM_BUILD_DIR/foo-1.0
zcat $RPM_SOURCE_DIR/foo-1.0.tar.gz | tar -xvf -

%build
cd foo-1.0 && make PREFIX=/usr %{?_smp_mflags}

%install
cd foo-1.0 && make PREFIX=/usr DESTDIR=%{?buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/foo