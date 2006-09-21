Summary:	Read, parse, merge and write RSS (and Atom) feeds
Summary(pl):	Narzêdzie do manipulowania kana³ami RSS (oraz ATOM)
Name:		rsstool
Version:	0.9.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	ed803d66598eae4c5f74cf2d9361a31b
URL:		http://rsstool.berlios.de
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read, parse, merge and write RSS (and Atom) feeds. It has some other
functions build-in like text, html, property file output or templates
with custom tags to insert RSS feeds into pages that could be uploaded
to a server that supports only static html

%description -l pl
rsstool czyta, parsuje, ³±czy i zapisuje kana³y RSS (i ATOM). Pozwala
na generowanie wyj¶cia w postaci RSS, html i txt. Mo¿liwe jest te¿
tworzenie szablonów do wstawienia rss na stronê www w przypadku gdy
serwer obs³uguje jedynie statyczny html.

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
%attr(755,root,root) %{_bindir}/*
%doc changes.html
