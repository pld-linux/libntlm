Summary:	Library for NTLM authentication
Summary(pl):	Biblioteka do uwierzytelniania NTLM
Name:		libntlm
Version:	0.3.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://josefsson.org/libntlm/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d639f72df9ba9aa7f9da2882693118e1
URL:		http://josefsson.org/libntlm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libntlm library provides routines to manipulate the structures used
for the client end of Microsoft NTLM authentication.

This code was taken mostly from the Samba project and was initially
intended for use with Microsoft Exchange Server when it is configured
to require NTLM authentication for clients of its IMAP server.

%description -l pl
Biblioteka libntlm dostarcza procedury do obróbki struktur u¿ywanych
po stronie klienta mechanizmu uwierzytelniania Microsoft NTLM.

Ten kod pochodzi w wiêkszo¶ci z projektu Samba i pocz±tkowo mia³ byæ
u¿ywany z serwerem Microsoft Exchange w przypadku, gdy zosta³
skonfigurowany aby wymagaæ uwierzytelnienia NTLM od klientów swojego
serwera IMAP.

%package devel
Summary:	Header files for libntlm library
Summary(pl):	Pliki nag³ówkowe biblioteki libntlm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libntlm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libntlm.

%package static
Summary:	Static libntlm library
Summary(pl):	Statyczna biblioteka libntlm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libntlm library.

%description static -l pl
Statyczna biblioteka libntlm.

%prep
%setup -q

%build
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntlm.so
%{_libdir}/libntlm.la
%{_includedir}/ntlm.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libntlm.a
