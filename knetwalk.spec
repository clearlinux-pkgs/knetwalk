#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : knetwalk
Version  : 18.12.2
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.2/src/knetwalk-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/knetwalk-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/knetwalk-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: knetwalk-bin = %{version}-%{release}
Requires: knetwalk-data = %{version}-%{release}
Requires: knetwalk-license = %{version}-%{release}
Requires: knetwalk-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n knetwalk-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549871455
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549871455
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knetwalk
cp COPYING %{buildroot}/usr/share/package-licenses/knetwalk/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/knetwalk/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang knetwalk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/doc/HTML/sv/knetwalk/index.cache.bz2
/usr/share/doc/HTML/sv/knetwalk/index.docbook
/usr/share/doc/HTML/uk/knetwalk/gameboard.png
/usr/share/doc/HTML/uk/knetwalk/index.cache.bz2
/usr/share/doc/HTML/uk/knetwalk/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knetwalk/COPYING
/usr/share/package-licenses/knetwalk/COPYING.DOC

%files locales -f knetwalk.lang
%defattr(-,root,root,-)

