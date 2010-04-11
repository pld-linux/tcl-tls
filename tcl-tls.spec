Summary:	OpenSSL Tcl extension
Summary(pl.UTF-8):	Rozszerzenie OpenSSL dla Tcl
Name:		tcl-tls
Version:	1.6
Release:	2
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tls/tls%{version}-src.tar.gz
# Source0-md5:	eb326ff9e6fc3b9885aa5c72fb8df3bf
Patch0:		%{name}-load-ssl-config.patch
URL:		http://tls.sourceforge.net/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TLS is an OpenSSL / RSA-bsafe Tcl extension that provides secure
connections on top of the Tcl socket mechanism. Within a few lines of
code, users can query HTTPS servers.

%description -l pl.UTF-8
TLS to rozszerzenie Tcl OpenSSL / RSA-bsafe, udostępniające bezpieczne
połączenia w oparciu o mechanizm gniazd Tcl. W kilku liniach kodu
można zmieścić zapytanie serwera HTTPS.

%prep
%setup -qn tls%{version}
%patch0 -p1

%build
%configure \
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
%dir %{_libdir}/tls%{version}
%attr(755,root,root) %{_libdir}/tls%{version}/lib*.so
%{_libdir}/tls%{version}/*.tcl
