Summary:	PFS calibration package
Summary(pl.UTF-8):	Pakiet do kalibracji PFS
Name:		pfscalibration
Version:	1.5
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/pfstools/%{name}-%{version}.tar.gz
# Source0-md5:	532efe0a6bf563d36d4bdec8dbe3e5a8
Patch0:		%{name}-opt.patch
URL:		http://pfstools.sourceforge.net/pfscalibration.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pfstools-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	pfstools >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PFS calibration package provides an implementation of the Robertson et
al. 2003 and Mitsunaga and Nayar 1999 methods for the photometric
calibration of cameras and for the recovery of high dynamic range
(HDR) images from the set of low dynamic range (LDR) exposures.

%description -l pl.UTF-8
Pakiet do kalibracji PFS zawiera implementację metod Robertsona i in.
z 2003 oraz Mitsunagi i Nayara z 1999 roku do fotometrycznej
kalibracji aparatów oraz odtwarzania obrazów o wysokim zakresie
dynamiki (HDR) ze zbioru ekspozycji o niskim zakresie dynamiki (LDR).

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/dcraw2hdrgen
%attr(755,root,root) %{_bindir}/jpeg2hdrgen
%attr(755,root,root) %{_bindir}/pfshdrcalibrate
%attr(755,root,root) %{_bindir}/pfsinhdrgen
%attr(755,root,root) %{_bindir}/pfsinme
%attr(755,root,root) %{_bindir}/pfsmergehdr
%attr(755,root,root) %{_bindir}/pfsplotresponse
%{_mandir}/man1/dcraw2hdrgen.1*
%{_mandir}/man1/jpeg2hdrgen.1*
%{_mandir}/man1/pfshdrcalibrate.1*
%{_mandir}/man1/pfsinhdrgen.1*
%{_mandir}/man1/pfsinme.1*
%{_mandir}/man1/pfsplotresponse.1*
