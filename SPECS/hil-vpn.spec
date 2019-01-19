Name:		hil-vpn
Version:	0.1
Release:	1%{?dist}
Summary:	VPN management micro service for use with HIL

License:	ASL 2.0
URL:		https://github.com/CCI-MOC/hil-vpn
#Source0:	https://github.com/CCI-MOC/hil-vpn/archive/v%%{version}.tar.gz
Source0:	https://github.com/zenhack/hil-vpn/archive/destdir.tar.gz
BuildRequires:	go >= 1.11

Requires: openvpn
Requires: bridge-utils
Requires: vconfig
Requires: net-tools
# For semanage; see https://fedoraproject.org/wiki/PackagingDrafts/SELinux#File_contexts
Requires(post): policycoreutils-python
Requires(postun): policycoreutils-python

# Without this, rpmbuild tries to scrape executables for debug info, and when
# it encounters the static executable we built, it complains that it can't find
# the symbols it needs (because it's not linked against libc). This directive
# simply disables building debuginfo packages.
%define debug_package %{nil}

%description
'hil-vpn' is a microservice for managing vpns, for use with HIL.

%prep
%setup -n hil-vpn-destdir

%build
# CGO_ENABLED=0 makes sure we don't link against libc, which is important for
# installing the package on older systems.
CGO_ENABLED=0 make PREFIX=/usr SYSCONFDIR=/etc

%check
go test ./...

%install
CGO_ENABLED=0 make PREFIX=/usr SYSCONFDIR=/etc DESTDIR=$RPM_BUILD_ROOT install

%post
semanage fcontext -a -t openvpn_exec_t /usr/libexec/hil-vpn-hook-up

%postun
if [ $1 -eq 0 ]; then
	semanage fcontext -d -t openvpn_exec_t /usr/libexec/hil-vpn-hook-up
fi

%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/sbin/hil-vpnd
/usr/libexec/hil-vpn-privop
/usr/libexec/hil-vpn-hook-up
%defattr(-,root,root)

