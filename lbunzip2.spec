Summary:	A multi-threaded bunzip2 filter
Name:		lbunzip2
Version:	0.03
Release:	%mkrel 2
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
