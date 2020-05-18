#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3FD8F43C2BB3C478 (h@hisham.hm)
#
Name     : htop
Version  : 2.2.0
Release  : 26
URL      : http://hisham.hm/htop/releases/2.2.0/htop-2.2.0.tar.gz
Source0  : http://hisham.hm/htop/releases/2.2.0/htop-2.2.0.tar.gz
Source1  : http://hisham.hm/htop/releases/2.2.0/htop-2.2.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: htop-bin = %{version}-%{release}
Requires: htop-data = %{version}-%{release}
Requires: htop-license = %{version}-%{release}
Requires: htop-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libnl-3.0)
Patch1: 0001-Settings.c-show-thread-names-by-default.patch
Patch2: htop-2.2.0-gcc-10.patch

%description
[![Build Status](https://travis-ci.org/hishamhm/htop.svg?branch=master)](https://travis-ci.org/hishamhm/htop)
[![PayPal donate](https://img.shields.io/badge/paypal-donate-green.svg)](http://hisham.hm/htop/index.php?page=donate)

%package bin
Summary: bin components for the htop package.
Group: Binaries
Requires: htop-data = %{version}-%{release}
Requires: htop-license = %{version}-%{release}

%description bin
bin components for the htop package.


%package data
Summary: data components for the htop package.
Group: Data

%description data
data components for the htop package.


%package license
Summary: license components for the htop package.
Group: Default

%description license
license components for the htop package.


%package man
Summary: man components for the htop package.
Group: Default

%description man
man components for the htop package.


%prep
%setup -q -n htop-2.2.0
cd %{_builddir}/htop-2.2.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589823783
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-linux-affinity --enable-taskstats  --enable-unicode--enable-delayacct  PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1589823783
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/htop
cp %{_builddir}/htop-2.2.0/COPYING %{buildroot}/usr/share/package-licenses/htop/bee7bf7e50188590517119b54e95cfb46fc07ad5
%make_install
## install_append content
ln -s htop %{buildroot}/usr/bin/top
## install_append end

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/htop/bee7bf7e50188590517119b54e95cfb46fc07ad5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htop.1
