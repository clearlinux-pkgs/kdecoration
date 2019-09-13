#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kdecoration
Version  : 5.16.5
Release  : 23
URL      : https://github.com/KDE/kdecoration/archive/v5.16.5/kdecoration-5.16.5.tar.gz
Source0  : https://github.com/KDE/kdecoration/archive/v5.16.5/kdecoration-5.16.5.tar.gz
Summary  : Plugin based library to create window decorations
Group    : Development/Tools
License  : LGPL-2.1
Requires: kdecoration-lib = %{version}-%{release}
Requires: kdecoration-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
# KDecoration2
Plugin based library to create window decorations.
## Introduction

%package dev
Summary: dev components for the kdecoration package.
Group: Development
Requires: kdecoration-lib = %{version}-%{release}
Provides: kdecoration-devel = %{version}-%{release}
Requires: kdecoration = %{version}-%{release}
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


%prep
%setup -q -n kdecoration-5.16.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568382195
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1568382195
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdecoration
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kdecoration/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KDecoration2/KDecoration2/DecoratedClient
/usr/include/KDecoration2/KDecoration2/Decoration
/usr/include/KDecoration2/KDecoration2/DecorationButton
/usr/include/KDecoration2/KDecoration2/DecorationButtonGroup
/usr/include/KDecoration2/KDecoration2/DecorationSettings
/usr/include/KDecoration2/KDecoration2/DecorationShadow
/usr/include/KDecoration2/KDecoration2/Private/DecoratedClientPrivate
/usr/include/KDecoration2/KDecoration2/Private/DecorationBridge
/usr/include/KDecoration2/KDecoration2/Private/DecorationSettingsPrivate
/usr/include/KDecoration2/kdecoration2/decoratedclient.h
/usr/include/KDecoration2/kdecoration2/decoration.h
/usr/include/KDecoration2/kdecoration2/decorationbutton.h
/usr/include/KDecoration2/kdecoration2/decorationbuttongroup.h
/usr/include/KDecoration2/kdecoration2/decorationdefines.h
/usr/include/KDecoration2/kdecoration2/decorationsettings.h
/usr/include/KDecoration2/kdecoration2/decorationshadow.h
/usr/include/KDecoration2/kdecoration2/kdecoration2_export.h
/usr/include/KDecoration2/kdecoration2/private/decoratedclientprivate.h
/usr/include/KDecoration2/kdecoration2/private/decorationbridge.h
/usr/include/KDecoration2/kdecoration2/private/decorationsettingsprivate.h
/usr/include/KDecoration2/kdecoration2/private/kdecoration2_private_export.h
/usr/include/KF5/kdecoration2_version.h
/usr/lib64/cmake/KDecoration2/KDecoration2Config.cmake
/usr/lib64/cmake/KDecoration2/KDecoration2ConfigVersion.cmake
/usr/lib64/cmake/KDecoration2/KDecoration2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KDecoration2/KDecoration2Targets.cmake
/usr/lib64/libkdecorations2.so
/usr/lib64/libkdecorations2private.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdecorations2.so.5
/usr/lib64/libkdecorations2.so.5.16.5
/usr/lib64/libkdecorations2private.so.5.16.5
/usr/lib64/libkdecorations2private.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdecoration/COPYING.LIB
