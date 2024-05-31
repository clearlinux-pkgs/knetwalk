#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : knetwalk
Version  : 24.05.0
Release  : 67
URL      : https://download.kde.org/stable/release-service/24.05.0/src/knetwalk-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/knetwalk-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/knetwalk-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: knetwalk-bin = %{version}-%{release}
Requires: knetwalk-data = %{version}-%{release}
Requires: knetwalk-license = %{version}-%{release}
Requires: knetwalk-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the knetwalk package.
Group: Binaries
Requires: knetwalk-data = %{version}-%{release}
Requires: knetwalk-license = %{version}-%{release}

%description bin
bin components for the knetwalk package.


%package data
Summary: data components for the knetwalk package.
Group: Data

%description data
data components for the knetwalk package.


%package doc
Summary: doc components for the knetwalk package.
Group: Documentation

%description doc
doc components for the knetwalk package.


%package license
Summary: license components for the knetwalk package.
Group: Default

%description license
license components for the knetwalk package.


%package locales
Summary: locales components for the knetwalk package.
Group: Default

%description locales
locales components for the knetwalk package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n knetwalk-24.05.0
cd %{_builddir}/knetwalk-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716519961
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
%cmake ..
make  %{?_smp_mflags}
popd
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
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1716519961
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knetwalk
cp %{_builddir}/knetwalk-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/knetwalk/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/knetwalk-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/knetwalk/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/knetwalk-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/knetwalk/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang knetwalk
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/knetwalk
/usr/bin/knetwalk

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.knetwalk.desktop
/usr/share/icons/hicolor/128x128/apps/knetwalk.png
/usr/share/icons/hicolor/16x16/apps/knetwalk.png
/usr/share/icons/hicolor/22x22/apps/knetwalk.png
/usr/share/icons/hicolor/32x32/apps/knetwalk.png
/usr/share/icons/hicolor/48x48/apps/knetwalk.png
/usr/share/icons/hicolor/64x64/apps/knetwalk.png
/usr/share/icons/hicolor/scalable/apps/knetwalk.svgz
/usr/share/knetwalk/qml/Cable.qml
/usr/share/knetwalk/qml/CanvasItem.qml
/usr/share/knetwalk/qml/Cell.qml
/usr/share/knetwalk/qml/logic.js
/usr/share/knetwalk/qml/main.qml
/usr/share/knetwalk/sounds/click.wav
/usr/share/knetwalk/sounds/connect.wav
/usr/share/knetwalk/sounds/start.wav
/usr/share/knetwalk/sounds/turn.wav
/usr/share/knetwalk/sounds/win.wav
/usr/share/knetwalk/themes/default.desktop
/usr/share/knetwalk/themes/default.svgz
/usr/share/knetwalk/themes/default_preview.png
/usr/share/knetwalk/themes/electronic.desktop
/usr/share/knetwalk/themes/electronic.svgz
/usr/share/knetwalk/themes/electronic_preview.png
/usr/share/metainfo/org.kde.knetwalk.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/knetwalk/index.cache.bz2
/usr/share/doc/HTML/ca/knetwalk/index.docbook
/usr/share/doc/HTML/cs/knetwalk/index.cache.bz2
/usr/share/doc/HTML/cs/knetwalk/index.docbook
/usr/share/doc/HTML/de/knetwalk/index.cache.bz2
/usr/share/doc/HTML/de/knetwalk/index.docbook
/usr/share/doc/HTML/en/knetwalk/gameboard.png
/usr/share/doc/HTML/en/knetwalk/index.cache.bz2
/usr/share/doc/HTML/en/knetwalk/index.docbook
/usr/share/doc/HTML/es/knetwalk/index.cache.bz2
/usr/share/doc/HTML/es/knetwalk/index.docbook
/usr/share/doc/HTML/et/knetwalk/index.cache.bz2
/usr/share/doc/HTML/et/knetwalk/index.docbook
/usr/share/doc/HTML/fr/knetwalk/index.cache.bz2
/usr/share/doc/HTML/fr/knetwalk/index.docbook
/usr/share/doc/HTML/id/knetwalk/gameboard.png
/usr/share/doc/HTML/id/knetwalk/index.cache.bz2
/usr/share/doc/HTML/id/knetwalk/index.docbook
/usr/share/doc/HTML/it/knetwalk/index.cache.bz2
/usr/share/doc/HTML/it/knetwalk/index.docbook
/usr/share/doc/HTML/ja/knetwalk/index.cache.bz2
/usr/share/doc/HTML/ja/knetwalk/index.docbook
/usr/share/doc/HTML/nl/knetwalk/index.cache.bz2
/usr/share/doc/HTML/nl/knetwalk/index.docbook
/usr/share/doc/HTML/pl/knetwalk/index.cache.bz2
/usr/share/doc/HTML/pl/knetwalk/index.docbook
/usr/share/doc/HTML/pt/knetwalk/index.cache.bz2
/usr/share/doc/HTML/pt/knetwalk/index.docbook
/usr/share/doc/HTML/pt_BR/knetwalk/index.cache.bz2
/usr/share/doc/HTML/pt_BR/knetwalk/index.docbook
/usr/share/doc/HTML/ru/knetwalk/index.cache.bz2
/usr/share/doc/HTML/ru/knetwalk/index.docbook
/usr/share/doc/HTML/sv/knetwalk/index.cache.bz2
/usr/share/doc/HTML/sv/knetwalk/index.docbook
/usr/share/doc/HTML/uk/knetwalk/gameboard.png
/usr/share/doc/HTML/uk/knetwalk/index.cache.bz2
/usr/share/doc/HTML/uk/knetwalk/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knetwalk/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/knetwalk/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/knetwalk/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f knetwalk.lang
%defattr(-,root,root,-)

