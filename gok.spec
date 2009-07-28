%define _requires_exceptions pkgconfig\(.*\)

Summary: GNOME On-screen Keyboard 
Name: gok
Version: 2.27.5
Release: %mkrel 1
License: LGPLv2+
Group: Accessibility
URL: http://www.gok.ca/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.11.12-1mdk use www-browser as web browser (Fedora)
Patch0:	gok-0.10.2-launcher.patch
#gw http://bugzilla.gnome.org/show_bug.cgi?id=589967
Patch2: gok-2.27.5-fix-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel
BuildRequires:	at-spi-devel >= 1.5.0
BuildRequires:	gtk-doc
BuildRequires:	libgnomeui2-devel
BuildRequires:	libwnck-devel >= 2.13
BuildRequires:	libusb-devel
BuildRequires:	intltool
BuildRequires:	scrollkeeper
BuildRequires:  XFree86-static-devel
BuildRequires:	libgnomespeech-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libcanberra-devel
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
%patch2 -p1

%build

%configure2_5x --enable-gtk-doc --enable-libusb-input

#parallel build is broken
make LIBS=-lm

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
