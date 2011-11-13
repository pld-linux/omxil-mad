Summary:	MAD decoder component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent dekodujący MAD dla implementacji Bellagio OpenMAX IL
Name:		omxil-mad
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxmad-%{version}.tar.gz
# Source0-md5:	b2e398ef611b628ffc7c38a0accff2a6
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
MAD component is a audio decoder component for Bellagio OpenMAX IL
that uses MAD and id3tag libraries for MP3 audio decoding.

%description -l pl.UTF-8
Komponent MAD to komponent dekodujący dźwięk dla implementacji
Bellagio OpenMAX IL, wykorzystujący biblioteki MAD i id3tag do
dekodowania dźwięku MP3.

%prep
%setup -q -n libomxmad-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxmad.so*
