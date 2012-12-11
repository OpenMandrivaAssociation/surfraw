%define name surfraw
%define version 1.0.7
%define release %mkrel 10

Summary: Command line interface to various web search engines
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://surfraw.sf.net/
Source0: ftp://ftp.netbsd.org/pub/NetBSD/misc/proff/surfraw-%{version}.tar.bz2
License: GPL
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: links
Patch: surfraw-1.0.7-no-graphical-browser-by-default.patch

%description
Surfraw provides a fast unix command line interface to a variety
of popular WWW search engines and other artifacts of power.
Forsake GUI idolatry! Apostate return!

%prep
%setup -q
%patch -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm $RPM_BUILD_ROOT%{_bindir}/rhyme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS TODO
%config(noreplace) /etc/*
%{_bindir}/*




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.7-10mdv2010.0
+ Revision: 434195
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.7-9mdv2009.0
+ Revision: 242843
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 12 2007 Pixel <pixel@mandriva.com> 1.0.7-7mdv2008.0
+ Revision: 62344
- replace funny Summary with a normal one

* Fri Aug 10 2007 Pixel <pixel@mandriva.com> 1.0.7-6mdv2008.0
+ Revision: 61050
- rebuild


* Thu Oct 06 2005 Pixel <pixel@mandriva.com> 1.0.7-5mdk
- remove rhyme which conflicts with package rhyme 
  (and anyway Lycos Rhyme service is no more?)

* Fri Jun 04 2004 Pixel <pixel@mandrakesoft.com> 1.0.7-4mdk
- rebuild

* Mon May 05 2003 Pixel <pixel@mandrakesoft.com> 1.0.7-3mdk
- fix typo in description (thanks to Adam Williamson)

* Mon May 05 2003 Pixel <pixel@mandrakesoft.com> 1.0.7-2mdk
- rebuild for new rpm

* Sat Feb 02 2002 Pixel <pixel@mandrakesoft.com> 1.0.7-1mdk
- new release

* Fri Oct 26 2001 Pixel <pixel@mandrakesoft.com> 1.0.4-1mdk
- new version

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.0.3-4mdk
- s/Copyright/License/

* Mon Jul 02 2001 Pixel <pixel@mandrakesoft.com> 1.0.3-3mdk
- rebuild

* Mon Apr 16 2001 Pixel <pixel@mandrakesoft.com> 1.0.3-2mdk
- BuildArch: noarch (thanks to Daniel Serodio)

* Sat Feb 24 2001 Pixel <pixel@mandrakesoft.com> 1.0.3-1mdk
- new version

* Wed Sep 27 2000 Pixel <pixel@mandrakesoft.com> 1.0.2-1mdk
- initial spec

