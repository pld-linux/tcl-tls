Summary:	OpenSSL Tcl extension
Summary(pl):	Rozszerzenie OpenSSL dla Tcl
Name:		tcl-tls
Version:	1.4.1
Release:	3
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tls/tls%{version}-src.tar.gz
# Source0-md5:	358bc16e8fd5a335dbf2e855426885d2
Patch0:		%{name}-DESTDIR.patch
URL:		http://tls.sourceforge.net/
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TLS is an OpenSSL / RSA-bsafe Tcl extension that provides secure
connections on top of the Tcl socket mechanism. Within a few lines of
code, users can query https servers.

%description -l pl
TLS to rozszerzenie Tcl OpenSSL / RSA-bsafe, udostêpniaj±ce bezpieczne
po³±czenia w oparciu o mechanizm gniazd Tcl. W kilku liniach kodu
mo¿na zmie¶ciæ zapytanie serwera https.

%prep
%setup -qn tls1.4
%patch0 -p1

%build
%configure2_13 \
	--with-ssl-dir=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

rm -f $RPM_BUILD_ROOT%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt license.terms
%{_libdir}/*
