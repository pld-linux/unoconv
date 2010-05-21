Summary:	Tool to convert between any document format supported by OpenOffice
Name:		unoconv
Version:	0.3
Release:	1
License:	GPL
Group:		Base
Source0:	http://dag.wieers.com/home-made/unoconv/%{name}-%{version}.tar.bz2
# Source0-md5:	e6b33a2041137d8ebae1b71396ec0641
Patch0:		%{name}-ooopath.patch
URL:		http://dag.wieers.com/home-made/unoconv/
BuildRequires:	python >= 2.0
BuildRequires:	rpm-pythonprov
Requires:	openoffice.org-pyuno
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
%attr(755,root,root) %{_bindir}/unoconv
%doc AUTHORS ChangeLog COPYING README TODO WISHLIST docs/ tests/
%{_mandir}/man1/unoconv.1*
