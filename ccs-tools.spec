Summary:	TOMOYO Linux tools
Summary(pl.UTF-8):	Narzędzia TOMOYO Linux
Name:		ccs-tools
Version:	1.6.6
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://osdn.dl.sourceforge.jp/tomoyo/30298/%{name}-%{version}-20090202.tar.gz
# Source0-md5:	ee6900297b263bebe19156c32c652f36
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-Makefile.patch
URL:		http://tomoyo.sourceforge.jp/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains TOMOYO Linux tools.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia TOMOYO Linux.

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
%attr(755,root,root) /usr/lib/ccs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
