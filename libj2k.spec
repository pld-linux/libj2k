Summary:	J2000 library
Summary(pl.UTF-8):   Biblioteka J2000
Name:		libj2k
Version:	0.0.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gaim-vv/%{name}-%{version}.tar.gz
# Source0-md5:	8daf9fd215fe00eb1c9c6af1b0aa61ee
URL:		http://gaim-vv.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
J2000 library.

%description -l pl.UTF-8
Biblioteka J2000.

%package devel
Summary:	The J2000 library - development files
Summary(pl.UTF-8):   Pliki dla programistów używających J2000
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the J2000 library.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki J2000.

%package static
Summary:	The J2000 library - static version
Summary(pl.UTF-8):   Statyczna biblioteka J2000
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the J2000 library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki J2000.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
