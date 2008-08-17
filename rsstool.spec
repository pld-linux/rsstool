Summary:	Read, parse, merge and write RSS (and Atom) feeds
Summary(hu.UTF-8):	RSS (és Atom) források olvasása, feldolgozása, írása
Summary(pl.UTF-8):	Narzędzie do manipulowania kanałami RSS (oraz ATOM)
Name:		rsstool
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	a3e003045d051491150385f556467a42
URL:		http://rsstool.y7.ath.cx/
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read, parse, merge and write RSS (and Atom) feeds. It has some other
functions build-in like text, HTML, property file output or templates
with custom tags to insert RSS feeds into pages that could be uploaded
to a server that supports only static HTML.

%description -l hu.UTF-8
RSS (és Atom) források olvasása, feldolgozása és írása. Beépített
funkcióival képes egyszerű szövegbe, HTML-be, stb. exportálni, ill.
tetszőleges kimeneti formátumot produkálni tag-ekkel.

%description -l pl.UTF-8
rsstool czyta, analizuje, łączy i zapisuje kanały RSS (i ATOM). Ma też
wbudowane funkcje do tworzenia plików tekstowych, HTML i właściwości
lub szablonów z własnymi znacznikami do wstawiania RSS na strony WWW w
przypadku, gdy serwer obsługuje jedynie statyczny HTML.

%prep
%setup -q -n %{name}-%{version}-src

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
