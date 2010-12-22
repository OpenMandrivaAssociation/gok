Summary: GNOME On-screen Keyboard 
Name: gok
Version: 2.30.1
Release: %mkrel 2
License: LGPLv2+
Group: Accessibility
URL: http://www.gok.ca/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.11.12-1mdk use www-browser as web browser (Fedora)
Patch0:	gok-0.10.2-launcher.patch
Patch1: gok-2.28.0-fix-linking.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libORBit2-devel
BuildRequires:	libx11-devel
BuildRequires:	libxi-devel
BuildRequires:	atk-devel
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libGConf2-devel
BuildRequires:	at-spi-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gnome-speech-devel
BuildRequires:	libwnck-devel
BuildRequires:	libxml2-devel
BuildRequires:	usb0.1-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	gnome-common
Requires: scrollkeeper
Requires: %{_lib}gail-gnome
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description 
The GNOME On-screen Keyboard (GOK) is a dynamic on-screen keyboard for
UNIX and UNIX-like operating systems.  It features Direct Selection,
Dwell Selection, Automatic Scanning and Inverse Scanning access
methods and includes word completion.

%prep
%setup -q
%patch0 -p1 -b .launcher
%patch1 -p1
autoreconf -fi

%build

%configure2_5x --enable-gtk-doc --enable-libusb-input
%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name} --with-gnome

#remove unpackaged files
rm -rf $RPM_BUILD_ROOT/var/lib/scrollkeeper

%if %mdkversion < 200900
%post
%update_scrollkeeper
%post_install_gconf_schemas gok
%{update_menus}
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas gok

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/*
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gok
%_datadir/icons/hicolor/*/apps/*.*
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
%{_libdir}/pkgconfig/*
%{_datadir}/pixmaps/gok.png
%_datadir/sounds/freedesktop/stereo/goksound*
