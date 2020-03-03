Summary:	Tool to convert between any document format supported by OpenOffice
Name:		unoconv
Version:	0.8.2
Release:	1
License:	GPL
Group:		Applications
Source0:	https://github.com/unoconv/unoconv/archive/%{version}.tar.gz
# Source0-md5:	b53576ddfc63b441ef55998f2f97db8e
Patch0:		shebang.patch
URL:		http://dag.wieers.com/home-made/unoconv/
BuildRequires:	python3 >= 3.0
BuildRequires:	rpm-pythonprov
Requires:	pyuno
Requires:	python >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unoconv converts between any document format that OpenOffice
understands. It uses OpenOffice's UNO bindings for non-interactive
conversion of documents.

Supported document formats include: Open Document Text (.odt), Open
Document Draw (.odd), Open Document Presentation (.odp), Open Document
calc (.odc), MS Word (.doc), MS PowerPoint (.pps/.ppt), MS Excel
(.xls), MS Office Open/OOXML (.xml), Portable Document Format (.pdf),
DocBook (.xml), LaTeX (.ltx), HTML, XHTML, RTF, Docbook (.xml), GIF,
PNG, JPG, SVG, BMP, EPS and many more...

%prep
%setup -q
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/unoconv
%{_mandir}/man1/unoconv.1*
