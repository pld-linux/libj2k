Summary:	Some kind of lib
Summary(pl):	Siaka? biblioteka
Name:		libj2k
Version:	0.0.8
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gaim-vv/%{name}-%{version}.tar.gz
# Source0-md5:	1af47edb4395e8e1a2569f0d960c2908
URL:		http://gaim-vv.sf.net/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool >= 1:1.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blahblahblah

%description -l pl
blablabla

%package devel
Summary:	The GNU oSIP library - development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych GNU oSIP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the GNU oSIP library.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych biblioteki GNU oSIP.

%package static
Summary:	The GNU oSIP library - static version
Summary(pl):	Statyczna biblioteka GNU oSIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the GNU oSIP library.

%description static -l pl
Statyczna wersja biblioteki GNU oSIP.

%prep
%setup -q

rm -f acinclude.m4

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
#%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
