%define name surfraw
%define version 1.0.7
%define release %mkrel 9

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


