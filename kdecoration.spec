#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kdecoration
Version  : 5.25.3
Release  : 66
URL      : https://download.kde.org/stable/plasma/5.25.3/kdecoration-5.25.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.3/kdecoration-5.25.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.3/kdecoration-5.25.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: kdecoration-lib = %{version}-%{release}
Requires: kdecoration-license = %{version}-%{release}
Requires: kdecoration-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev

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
%setup -q -n kdecoration-5.25.3
cd %{_builddir}/kdecoration-5.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657637653
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657637653
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdecoration
cp %{_builddir}/kdecoration-5.25.3/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdecoration/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kdecoration-5.25.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdecoration/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kdecoration-5.25.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kdecoration-5.25.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang kdecoration

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
/usr/include/KDecoration2/KDecoration2/DecorationThemeProvider
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
/usr/include/KDecoration2/kdecoration2/decorationthemeprovider.h
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
/usr/lib64/libkdecorations2.so.5.25.3
/usr/lib64/libkdecorations2private.so.5.25.3
/usr/lib64/libkdecorations2private.so.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdecoration/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdecoration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdecoration/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kdecoration.lang
%defattr(-,root,root,-)

