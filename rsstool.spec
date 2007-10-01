%define 	_rc rc4
Summary:	Read, parse, merge and write RSS (and Atom) feeds
Summary(pl.UTF-8):	Narzędzie do manipulowania kanałami RSS (oraz ATOM)
Name:		rsstool
Version:	1.0.0
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}%{_rc}-src.tar.gz
# Source0-md5:	d164eb5e04ffdc2fa2ffb2c8599a05dd
URL:		http://rsstool.y7.ath.cx/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read, parse, merge and write RSS (and Atom) feeds. It has some other
functions build-in like text, HTML, property file output or templates
with custom tags to insert RSS feeds into pages that could be uploaded
to a server that supports only static HTML.

%description -l pl.UTF-8
rsstool czyta, analizuje, łączy i zapisuje kanały RSS (i ATOM). Ma też
wbudowane funkcje do tworzenia plików tekstowych, HTML i właściwości
lub szablonów z własnymi znacznikami do wstawiania RSS na strony WWW w
przypadku, gdy serwer obsługuje jedynie statyczny HTML.

%prep
%setup -q -n %{name}-%{version}%{_rc}-src

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/rsstool $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.html faq.html contrib/
%attr(755,root,root) %{_bindir}/*
