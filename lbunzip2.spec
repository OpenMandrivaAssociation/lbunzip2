Summary:	A multi-threaded bunzip2 filter
Name:		lbunzip2
Version:	0.03
Release:	%mkrel 3
License:	GPLv2+
Group: 		Archiving/Compression
URL:		http://phptest11.atw.hu/
Source0:	lbunzip2.tar.gz
BuildRequires:	bzip2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A multi-threaded bunzip2 filter that doesn't depend on the lseek() system call
and so isn't restricted to regular files.

%prep

%setup -q -n %{name}

chmod 644 README

%build

%make CFLAGS="%{optflags} -D_XOPEN_SOURCE=500" LDFLAGS="-Wl,--as-needed -Wl,--no-undefined"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 %{name} %{buildroot}%{_bindir}/

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.03-3mdv2011.0
+ Revision: 620056
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2010.0
+ Revision: 429704
- rebuild

* Wed Aug 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2009.0
+ Revision: 274229
- 0.03

* Mon Aug 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2009.0
+ Revision: 273160
- 0.02

* Thu Aug 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2009.0
+ Revision: 271853
- import lbunzip2


* Thu Aug 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2009.0
- initial Mandriva package
