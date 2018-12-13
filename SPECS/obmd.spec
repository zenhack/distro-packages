Name:		obmd
Version:	0.2
Release:	1%{?dist}
Summary:	OBM micro service for use with HIL

License:	ASL 2.0
URL:		https://github.com/CCI-MOC/obmd
Source0:	https://github.com/CCI-MOC/obmd/archive/v%{version}.tar.gz
BuildRequires:	go >= 1.11

%description
OBMd is a microservice for managing the OBMs of machines, built for use with HIL.

%prep
%setup -n obmd-%{version}

%build
go build

%check
go test ./...

%install
install -Dm755 obmd -t $RPM_BUILD_ROOT/usr/sbin/

%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/sbin/obmd
%defattr(-,root,root)

