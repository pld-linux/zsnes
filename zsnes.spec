%define fversion %(echo %{version} |tr -d .)
Summary:	Nintendo Super NES / Super Famicom Emulator
Summary(pl.UTF-8):	Emulator Nintendo Super NES / Super Famicom
Name:		zsnes
Version:	1.36
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/%{name}/%{name}%{fversion}src.tar.gz
# Source0-md5:	576f6f5cc50c7c6f7877aca220ee99b3
URL:		http://zsnes.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	nasm >= 0.98
BuildRequires:	zlib-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an emulator for Nintendo's 16 bit console, called Super
Nintendo Entertainment System or Super Famicom. It features a pretty
accurate emulation of that system's graphic and sound capabilities.
The GUI enables the user to select games, change options, enable cheat
codes and to save the game state, even network play is possible.

%description -l pl.UTF-8
Jest to emulator 16 bitowej konsoli, zwanej Super Nintendo
Enterainment System lub Superfamicom. Cechuje się niezłym
przyspieszeniem emulacji systemowej grafiki i możliwości dźwiękowych.
GUI umożliwia wybranie gry, zmianę opcji, włączenie kodów ułatwień i
zachowanie stanu gry, jest także możliwa gra sieciowa.

%prep
%setup -q

%build
cd src
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D src/linux/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc authors.txt install.txt opengl.txt readme.txt srcinfo.txt todo.txt whatsnew.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
