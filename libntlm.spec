Summary:	Library for NTLM authentication
Summary(pl.UTF-8):	Biblioteka do uwierzytelniania NTLM
Name:		libntlm
Version:	1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://josefsson.org/libntlm/releases/%{name}-%{version}.tar.gz
# Source0-md5:	13b40af721b29005652fb429a3ae9582
URL:		http://josefsson.org/libntlm/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libntlm library provides routines to manipulate the structures used
for the client end of Microsoft NTLM authentication.

This code was taken mostly from the Samba project and was initially
intended for use with Microsoft Exchange Server when it is configured
to require NTLM authentication for clients of its IMAP server.

%description -l pl.UTF-8
Biblioteka libntlm dostarcza procedury do obróbki struktur używanych
po stronie klienta mechanizmu uwierzytelniania Microsoft NTLM.

Ten kod pochodzi w większości z projektu Samba i początkowo miał być
używany z serwerem Microsoft Exchange w przypadku, gdy został
skonfigurowany aby wymagać uwierzytelnienia NTLM od klientów swojego
serwera IMAP.

%package devel
Summary:	Header files for libntlm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libntlm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libntlm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libntlm.

%package static
Summary:	Static libntlm library
Summary(pl.UTF-8):	Statyczna biblioteka libntlm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libntlm library.

%description static -l pl.UTF-8
Statyczna biblioteka libntlm.

%prep
%setup -q

%{__rm} m4/{libtool.m4,lt*}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/libntlm.la
%{_includedir}/ntlm.h
%{_pkgconfigdir}/libntlm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libntlm.a
