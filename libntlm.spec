Summary:	Library for NTLM authentication
Summary(pl.UTF-8):	Biblioteka do uwierzytelniania NTLM
Name:		libntlm
Version:	1.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.savannah.nongnu.org/releases/libntlm/%{name}-%{version}.tar.gz
# Source0-md5:	ecb7ffe83a97588e444eafa0d85c3c01
URL:		https://gitlab.com/gsasl/libntlm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libntlm library provides routines to manipulate the structures used
for the client end of Microsoft NTLM authentication.

This code was taken mostly from the Samba project and was initially
intended for use with Microsoft Exchange Server when it is configured
to require NTLM authentication for clients of its IMAP server.

%description -l pl.UTF-8
Biblioteka Libntlm dostarcza procedury do obróbki struktur używanych
po stronie klienta mechanizmu uwierzytelniania Microsoft NTLM.

Ten kod pochodzi w większości z projektu Samba i początkowo miał być
używany z serwerem Microsoft Exchange w przypadku, gdy został
skonfigurowany aby wymagać uwierzytelnienia NTLM od klientów swojego
serwera IMAP.

%package devel
Summary:	Header files for Libntlm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Libntlm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Libntlm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Libntlm.

%package static
Summary:	Static Libntlm library
Summary(pl.UTF-8):	Statyczna biblioteka Libntlm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Libntlm library.

%description static -l pl.UTF-8
Statyczna biblioteka Libntlm.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies, obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libntlm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/libntlm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntlm.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntlm.so
%{_includedir}/ntlm.h
%{_pkgconfigdir}/libntlm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libntlm.a
