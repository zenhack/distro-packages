This repository contains scripts for packaging software which the MOC:

1. Uses, but is not otherwise packaged for our systems, or
2. Maintains ourselves.

The script `fetch.sh` takes care of downloading and verifying the
sources, since the RPM dev tools don't do this and we'd rather not keep
upstream source tarballs in git.

Note that some of these are not "distro quality" packages, in that they
do not follow all of the guidelines for building packages. For example,
the Go packages rely on the standard Go tooling to fetch dependencies at
build time, rather than packaging each dependency individually and then
specifying them (redundantly) in the rpm spec.

To build a package:

	./fetch.sh
	rpmbuild -ba SPECS/python-schema.spec

To preform the above, you need `wget` installed, and need to set up an
environment for building packages on RedHat family distros.

<https://fedoraproject.org/wiki/How_to_create_an_RPM_package#Getting_ready_to_package_a_particular_program>

The Go packages require at least Go 1.11, which does not ship with
RHEL/CentOS 7. However, it is available in current versions of Fedora,
and because the executables are statically linked, the final packages
should work other systems just as well.

The 'Vagrantfile' sets up an environment suitable for packaging, based
on Fedora 29.

# License

The contents of this repository are licensed under the terms of the
Apache License, version 2.0. A copy can be found in the file `LICENSE`.
The software packages each have their own licenses; see the individual
packages for details.
