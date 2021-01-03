%global php_libname          tfpdf
Name:      php-%{php_libname}
Version:   1.32
Release:   1%{?dist}
License:   LGPL
Summary:   a modified version of FPDF that adds UTF-8 support in generated PDF documents
Group:     Development/Libraries
URL:       https://fpdf.org/en/script/script92.php

# Upstream uses a troublesome URL for source.  Grab it from the Github reference below.
Source:    https://github.com/Setasign/tFPDF/archive/v%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:  php-zlib
BuildRequires:  dos2unix
BuildArch: noarch

%description
This class is a modified version of FPDF that adds UTF-8 support. Moreover, 
it embeds only the necessary parts of the fonts that are used in the document, 
making the file size much smaller than if the whole fonts were embedded.


%prep
%setup -qn tFPDF-%{version}
dos2unix *.txt
find -type f | xargs chmod -x 
find . -name \*.php -exec dos2unix \{\} \;
find . -name \*.htm -exec dos2unix \{\} \;


%build
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/php/%{php_libname}
cp -a ./*  %{buildroot}%{_datadir}/php/%{php_libname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/php/%{php_libname}
%doc *.txt *.md


%changelog
* Mon Oct 12 2020 Bishop <bishopolis@gmail.com> - 2.3.4-1
- Initial Packaging
