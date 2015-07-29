This repository contains scripts for packaging software which the MOC
uses, but is not otherwise packaged for our systems.

Right now there is just one package, `python-schema`, packaged for
RHEL/CentOS 7. The script `fetch.sh` takes care of downloading and
verifying the sources, since the RPM dev tools don't do this and we'd
rather not keep upstream source tarballs in git. To build the package:

	./fetch.sh
	rpmbuild -ba SPECS/python-schema.spec


To preform the above, you need `wget` installed, and need to set up an
environment for building packages on RHEL/CentOS 7 as described at:

<https://fedoraproject.org/wiki/How_to_create_an_RPM_package#Getting_ready_to_package_a_particular_program>

# License

The contents of this repository are licensed under the terms of the
ApacheLicense, version 2.0. A copy can be found in the file `LICENSE`.
The software packages each have their own licenses; see the individual
packages for details.
