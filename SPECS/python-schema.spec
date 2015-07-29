Name:		python-schema
Version:	0.3.1
Release:	1%{?dist}
Summary:	Simple data validation library

Group:		Development/Libraries
License:	MIT
URL:		https://github.com/halst/schema
Source0:	https://pypi.python.org/packages/source/s/schema/schema-%{version}.tar.gz
BuildArch:	noarch
Requires:	python

%description
schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python
data-types.

%prep
%setup -n schema-%{version}

%build
python setup.py build

%install
python setup.py install --optimize=1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT
%files -f INSTALLED_FILES
%defattr(-,root,root)

