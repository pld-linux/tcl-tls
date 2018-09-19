Summary:	OpenSSL Tcl extension
Summary(pl.UTF-8):	Rozszerzenie OpenSSL dla Tcl
Name:		tcl-tls
Version:	1.7.16
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	https://core.tcl.tk/tcltls/uv/tcltls-1.7.16.tar.gz
# Source0-md5:	4887ac4c5e2a003f3d63e2f30d33ba1e
URL:		https://core.tcl.tk/tcltls/index
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
%setup -qn tcltls-%{version}

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
%dir %{_libdir}/tcltls%{version}
%attr(755,root,root) %{_libdir}/tcltls%{version}/tcltls*.so
%{_libdir}/tcltls%{version}/*.tcl
