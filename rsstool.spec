Summary:	Read, parse, merge and write RSS (and Atom) feeds
Summary(pl):	Narz�dzie do manipulowania kana�ami RSS (oraz ATOM)
Name:		rsstool
Version:	0.9.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	ed803d66598eae4c5f74cf2d9361a31b
URL:		http://rsstool.berlios.de/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read, parse, merge and write RSS (and Atom) feeds. It has some other
functions build-in like text, HTML, property file output or templates
with custom tags to insert RSS feeds into pages that could be uploaded
to a server that supports only static HTML.

%description -l pl
rsstool czyta, analizuje, ��czy i zapisuje kana�y RSS (i ATOM). Ma te�
wbudowane funkcje do tworzenia plik�w tekstowych, HTML i w�a�ciwo�ci
lub szablon�w z w�asnymi znacznikami do wstawiania RSS na strony WWW w
przypadku, gdy serwer obs�uguje jedynie statyczny HTML.

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
%doc changes.html
%attr(755,root,root) %{_bindir}/*
