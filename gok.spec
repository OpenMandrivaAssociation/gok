Summary: GNOME On-screen Keyboard 
Name: gok
Version: 2.30.1
Release: 4
License: LGPLv2+
Group: Accessibility
URL: http://www.gok.ca/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.11.12-1mdk use www-browser as web browser (Fedora)
Patch0:	gok-0.10.2-launcher.patch
Patch1: gok-2.28.0-fix-linking.patch
BuildRequires:	pkgconfig(ORBit-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(gconf-2.0) GConf2
BuildRequires:	pkgconfig(libspi-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gnome-speech-1.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(popt)
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
rm -rf $RPM_BUILD_ROOT/var/lib/scrollkeeper $RPM_BUILD_ROOT%_libdir/pkgconfig

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

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/*
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gok
%_datadir/icons/hicolor/*/apps/*.*
%{_datadir}/pixmaps/gok.png
%_datadir/sounds/freedesktop/stereo/goksound*


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.30.1-3mdv2011.0
+ Revision: 672453
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Wed Dec 22 2010 Funda Wang <fwang@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 623779
- pkgconfig file is not needed for now
- tighten BR

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Wed Sep 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2011.0
+ Revision: 581966
- update to new version 2.30.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528957
- update to new version 2.30.0

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 475375
- update to new version 2.29.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458785
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446885
- update build deps
- new version
- fix linking

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437479
- update to new version 2.27.92

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420499
- update to new version 2.27.91

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414468
- new version
- drop patch 2

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 401432
- new version
- drop patch 1
- fix another build failure

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395621
- new version
- fix build

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386077
- update to new version 2.27.3

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379679
- update to new version 2.27.2

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374235
- update build deps
- new version
- update file list

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355929
- update to new version 2.26.0

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340925
- update to new version 2.25.91

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336647
- new version
- drop patch 1

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 331374
- update to new version 2.25.3

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309011
- update to new version 2.25.2

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299793
- update to new version 2.25.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287356
- new version

* Fri Aug 29 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277478
- new version

* Mon Jul 14 2008 Götz Waschk <waschk@mandriva.org> 1.4.0-1mdv2009.0
+ Revision: 235375
- fix buildrequires
- new version

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.3.7-2mdv2009.0
+ Revision: 218421
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 1.3.7-2mdv2008.1
+ Revision: 163536
- New license policy
- drop old menu

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 1.3.7-1mdv2008.1
+ Revision: 98360
- new version
- drop patch 2

* Sun Oct 14 2007 Götz Waschk <waschk@mandriva.org> 1.3.6-1mdv2008.1
+ Revision: 98339
- new version
- fix build with a patch from svn

* Sat Oct 13 2007 Götz Waschk <waschk@mandriva.org> 1.3.5-1mdv2008.1
+ Revision: 97935
- new version

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 1.3.4-1mdv2008.0
+ Revision: 89333
- new version

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 1.3.3-1mdv2008.0
+ Revision: 80325
- new version
- fix icon in desktop file

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 1.3.2-1mdv2008.0
+ Revision: 72027
- new version

* Mon Jul 09 2007 Götz Waschk <waschk@mandriva.org> 1.3.1-1mdv2008.0
+ Revision: 50728
- new version

* Sat May 26 2007 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2008.0
+ Revision: 31362
- new version
- add new icon


* Thu Mar 08 2007 Frederic Crozat <fcrozat@mandriva.com> 1.2.3-2mdv2007.1
+ Revision: 137649
- Prevent pkgconfig auto dependencies

* Wed Feb 28 2007 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.1
+ Revision: 127278
- new version
- unpack patch

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.1
+ Revision: 126212
- new version

* Sat Jan 20 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-2mdv2007.1
+ Revision: 110996
- really enable usb

* Sat Jan 20 2007 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdv2007.1
+ Revision: 110995
- new version
- enable libusb support

* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 1.2.0-2mdv2007.1
+ Revision: 102494
- Fix libgail-gnome dependency for biarch
- Import gok

* Sat Aug 26 2006 Götz Waschk <waschk@mandriva.org> 1.2.0-1mdv2007.0
- New release 1.2.0

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.1-5mdv2007.0
- Rebuild with latest dbus

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 1.1.1-3mdv2007.1
- rebuild for new gail

* Sun Jul 16 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.1.1-3mdv2007.0
- Fix XDG menu

* Fri Jul 14 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.1-2mdv2007.0
- Rebuild with latest libgail

* Fri Jul 14 2006 G�tz Waschk <waschk@mandriva.org> 1.1.1-1mdv2007.0
- new macros
- xdg menu
- New release 1.1.1

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 1.0.10-1mdk
- New release 1.0.10

* Thu Apr 27 2006 Götz Waschk <waschk@mandriva.org> 1.0.8-1mdk
- New release 1.0.8

* Wed Apr 19 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.7-1mdk
- Release 1.0.7

* Mon Feb 27 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-5mdk
- Add schema uninstallation

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-4mdk
- Use mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0.5-3mdk
- Rebuild

* Thu Oct 13 2005 Götz Waschk <waschk@mandriva.org> 1.0.5-2mdk
- rebuild for new libwnck

* Fri May 13 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.5-1mdk
- New release 1.0.5

* Wed May 04 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0.4-1mdk 
- Release 1.0.4
- Fix buildrequires for x86-64

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.11.16-3mdk 
- Rebuild with latest howl

* Sun Nov 14 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.11.16-2mdk
- add BuildRequires: libgnomespeech-devel libglade2.0-devel

* Wed Nov 10 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.11.16-1mdk
- New release 0.11.16

* Wed Nov 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.11.12-1mdk
- New release 0.11.12
- Patch0 (Fedora): use www-browser as web browser

* Fri Aug 27 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.2-3mdk
- Fix menu

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.2-2mdk
- Fix BuildRequires

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.2-1mdk
- New release 0.10.2

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.0-1mdk
- New release 0.10.0
- Remove patch0 (merged upstream)

* Fri Mar 26 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.3-6mdk
- Enforce libgail-gnome dependency

