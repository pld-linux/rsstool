Summary:	Read, parse, merge and write RSS (and Atom) feeds
Summary(pl.UTF-8):	Narzędzie do manipulowania kanałami RSS (oraz ATOM)
Name:		rsstool
Version:	0.9.10
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	5bc2fa5634d92ba2edc679255e52156a
URL:		http://rsstool.berlios.de/
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
%doc changes.html faq.html
%attr(755,root,root) %{_bindir}/*
