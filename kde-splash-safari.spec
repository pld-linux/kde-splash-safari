
%define		_splash		safari

Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=12824&id=1
Source0:	http://www.kde-look.org/content/files/12824-safari.02.tar.gz
# Source0-md5:	e969ec23aaeb71f8660f2497ff236288
Source1:	%{name}-Theme.rc
Source2:	%{name}-Preview.png
URL:		http://www.kde-look.org/content/show.php?content=12824
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you are dreaming of safari, you will surely like this splash screen.

%description -l pl.UTF-8
Jeżeli marzysz o safari, z pewnością polubisz ten ekran startowy.

%prep
%setup -q -c %{_splash} -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install pics/*.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc
install %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Preview.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
