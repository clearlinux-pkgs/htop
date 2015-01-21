#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : htop
Version  : 1.0.3
Release  : 7
URL      : http://hisham.hm/htop/releases/1.0.3/htop-1.0.3.tar.gz
Source0  : http://hisham.hm/htop/releases/1.0.3/htop-1.0.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: htop-bin
Requires: htop-data
Requires: htop-doc
BuildRequires : ncurses-dev

%description
htop
====
by Hisham Muhammad <hisham@gobolinux.org>
May, 2004 - January, 2014
Note
----

%package bin
Summary: bin components for the htop package.
Group: Binaries
Requires: htop-data

%description bin
bin components for the htop package.


%package data
Summary: data components for the htop package.
Group: Data

%description data
data components for the htop package.


%package doc
Summary: doc components for the htop package.
Group: Documentation

%description doc
doc components for the htop package.


%prep
%setup -q -n htop-1.0.3

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
ln -s htop %{buildroot}/usr/bin/top
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/htop
/usr/bin/top

%files data
%defattr(-,root,root,-)
/usr/share/applications/htop.desktop
/usr/share/pixmaps/htop.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
