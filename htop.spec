#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : htop
Version  : 3.2.2
Release  : 43
URL      : https://github.com/htop-dev/htop/archive/3.2.2/htop-3.2.2.tar.gz
Source0  : https://github.com/htop-dev/htop/archive/3.2.2/htop-3.2.2.tar.gz
Summary  : Interactive process viewer
Group    : Development/Tools
License  : GPL-2.0
Requires: htop-bin = %{version}-%{release}
Requires: htop-data = %{version}-%{release}
Requires: htop-license = %{version}-%{release}
Requires: htop-man = %{version}-%{release}
BuildRequires : libcap-dev
BuildRequires : lm-sensors-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(hwloc)
BuildRequires : pkgconfig(libnl-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
%setup -q -n htop-3.2.2
cd %{_builddir}/htop-3.2.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689792712
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static --enable-linux-affinity \
--enable-taskstats \
--enable-unicode \
--enable-delayacct \
--enable-sensors
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689792712
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/htop
cp %{_builddir}/htop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/htop/4cc77b90af91e615a64ae04893fdffa7939db84c || :
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
/usr/share/icons/hicolor/scalable/apps/htop.svg
/usr/share/pixmaps/htop.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/htop/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htop.1
