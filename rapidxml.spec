Summary:	RapidXML - fast XML parser written in C++
Summary(pl.UTF-8):	RapidXML - szybki parser XML napisany w C++
Name:		rapidxml
Version:	1.13
Release:	2
License:	Boost Software License v1.0 or MIT
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/rapidxml/%{name}-%{version}.zip
# Source0-md5:	7b4b42c9331c90aded23bb55dc725d6a
URL:		http://rapidxml.sourceforge.net/
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RapidXml is an attempt to create the fastest XML parser possible,
while retaining useability, portability and reasonable W3C
compatibility. It is an in-situ parser written in modern C++, with
parsing speed approaching that of strlen function executed on the same
data.

%description -l pl.UTF-8
RapidXml to próba stworzenia możliwie najszybszego parsera XML przy
zachowaniu użyteczności, przenośności i rozsądnej zgodności z W3C.
Jest to parser napisany w nowoczesnym C++ z szybkością analizowania
zbliżającą się do szybkości funkcji strlen wywołanej na tych samych
danych.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/rapidxml

install rapidxml*.hpp $RPM_BUILD_ROOT%{_includedir}/rapidxml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt manual.html
%{_includedir}/rapidxml
