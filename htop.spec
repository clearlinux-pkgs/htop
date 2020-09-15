#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : htop
Version  : 3.0.2
Release  : 29
URL      : https://github.com/htop-dev/htop/archive/3.0.2/htop-3.0.2.tar.gz
Source0  : https://github.com/htop-dev/htop/archive/3.0.2/htop-3.0.2.tar.gz
Summary  : Interactive process viewer
Group    : Development/Tools
License  : GPL-2.0
Requires: htop-bin = %{version}-%{release}
Requires: htop-data = %{version}-%{release}
Requires: htop-license = %{version}-%{release}
Requires: htop-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libnl-3.0)
Patch1: 0001-Settings.c-show-thread-names-by-default.patch

%description
htop is a cross-platform interactive process viewer. It requires ncurses.

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
%setup -q -n htop-3.0.2
cd %{_builddir}/htop-3.0.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600143755
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --enable-linux-affinity \
--enable-taskstats \
--enable-unicode \
--enable-delayacct
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600143755
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/htop
cp %{_builddir}/htop-3.0.2/COPYING %{buildroot}/usr/share/package-licenses/htop/044462b5c756fee77f267e633f57ce4acfa778e4
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
/usr/share/package-licenses/htop/044462b5c756fee77f267e633f57ce4acfa778e4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htop.1
