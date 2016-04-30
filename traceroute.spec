#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : traceroute
Version  : 2.1.0
Release  : 10
URL      : http://downloads.sourceforge.net/traceroute/traceroute-2.1.0.tar.gz
Source0  : http://downloads.sourceforge.net/traceroute/traceroute-2.1.0.tar.gz
Summary  : Traces the route taken by packets over an IPv4/IPv6 network
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: traceroute-bin
Requires: traceroute-doc
Patch1: 0000-fix-prefix.patch

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%package bin
Summary: bin components for the traceroute package.
Group: Binaries

%description bin
bin components for the traceroute package.


%package doc
Summary: doc components for the traceroute package.
Group: Documentation

%description doc
doc components for the traceroute package.


%prep
%setup -q -n traceroute-2.1.0
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/traceroute

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
