#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kdecoration
Version  : 6.3.4
Release  : 116
URL      : https://download.kde.org/stable/plasma/6.3.4/kdecoration-6.3.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.4/kdecoration-6.3.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.4/kdecoration-6.3.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: kdecoration-lib = %{version}-%{release}
Requires: kdecoration-license = %{version}-%{release}
Requires: kdecoration-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDecoration3
Plugin based library to create window decorations.
## Introduction

%package dev
Summary: dev components for the kdecoration package.
Group: Development
Requires: kdecoration-lib = %{version}-%{release}
Provides: kdecoration-devel = %{version}-%{release}
Requires: kdecoration = %{version}-%{release}

%description dev
dev components for the kdecoration package.


%package lib
Summary: lib components for the kdecoration package.
Group: Libraries
Requires: kdecoration-license = %{version}-%{release}

%description lib
lib components for the kdecoration package.


%package license
Summary: license components for the kdecoration package.
Group: Default

%description license
license components for the kdecoration package.


%package locales
Summary: locales components for the kdecoration package.
Group: Default

%description locales
locales components for the kdecoration package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kdecoration-6.3.4
cd %{_builddir}/kdecoration-6.3.4
pushd ..
cp -a kdecoration-6.3.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744136253
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744136253
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdecoration
cp %{_builddir}/kdecoration-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdecoration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdecoration-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdecoration/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kdecoration-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdecoration/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdecoration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdecoration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kdecoration
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KDecoration3/KDecoration3/DecoratedWindow
/usr/include/KDecoration3/KDecoration3/Decoration
/usr/include/KDecoration3/KDecoration3/DecorationButton
/usr/include/KDecoration3/KDecoration3/DecorationButtonGroup
/usr/include/KDecoration3/KDecoration3/DecorationSettings
/usr/include/KDecoration3/KDecoration3/DecorationShadow
/usr/include/KDecoration3/KDecoration3/DecorationThemeProvider
/usr/include/KDecoration3/KDecoration3/Private/DecoratedWindowPrivate
/usr/include/KDecoration3/KDecoration3/Private/DecorationBridge
/usr/include/KDecoration3/KDecoration3/Private/DecorationSettingsPrivate
/usr/include/KDecoration3/KDecoration3/ScaleHelpers
/usr/include/KDecoration3/kdecoration3/decoratedwindow.h
/usr/include/KDecoration3/kdecoration3/decoration.h
/usr/include/KDecoration3/kdecoration3/decorationbutton.h
/usr/include/KDecoration3/kdecoration3/decorationbuttongroup.h
/usr/include/KDecoration3/kdecoration3/decorationdefines.h
/usr/include/KDecoration3/kdecoration3/decorationsettings.h
/usr/include/KDecoration3/kdecoration3/decorationshadow.h
/usr/include/KDecoration3/kdecoration3/decorationthemeprovider.h
/usr/include/KDecoration3/kdecoration3/kdecoration3_export.h
/usr/include/KDecoration3/kdecoration3/private/decoratedwindowprivate.h
/usr/include/KDecoration3/kdecoration3/private/decorationbridge.h
/usr/include/KDecoration3/kdecoration3/private/decorationsettingsprivate.h
/usr/include/KDecoration3/kdecoration3/private/kdecoration3_private_export.h
/usr/include/KDecoration3/kdecoration3/scalehelpers.h
/usr/include/KF6/kdecoration3_version.h
/usr/lib64/cmake/KDecoration3/KDecoration3Config.cmake
/usr/lib64/cmake/KDecoration3/KDecoration3ConfigVersion.cmake
/usr/lib64/cmake/KDecoration3/KDecoration3Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KDecoration3/KDecoration3Targets.cmake
/usr/lib64/libkdecorations3.so
/usr/lib64/libkdecorations3private.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkdecorations3.so.6.3.4
/V3/usr/lib64/libkdecorations3private.so.6.3.4
/usr/lib64/libkdecorations3.so.6
/usr/lib64/libkdecorations3.so.6.3.4
/usr/lib64/libkdecorations3private.so.2
/usr/lib64/libkdecorations3private.so.6.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdecoration/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdecoration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdecoration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kdecoration.lang
%defattr(-,root,root,-)

