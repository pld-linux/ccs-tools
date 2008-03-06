Summary:	TOMOYO Linux tools
Name:		ccs-tools
Version:	1.5.3
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://osdn.dl.sourceforge.jp/tomoyo/27220/%{name}-%{version}-20080131.tar.gz
# Source0-md5:	f6c0371ce5b413f8ce955630cd69f72a
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-Makefile.patch
URL:		http://tomoyo.sourceforge.jp/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is TOMOYO Linux tools.

%prep
%setup -q -n ccstools
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/ccs-init
%attr(755,root,root) /sbin/tomoyo-init
%attr(755,root,root) %{_libdir}/ccs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
%attr(4755,root,root) %{_libdir}/ccs/misc/proxy
