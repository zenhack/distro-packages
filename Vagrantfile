# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # We use fedora because it has a recent enough version of Go to support Go
  # modules, which RHEL/CentOS 7 does not. the final executables are statically
  # linked, so should still work on RHEL/CentOS 7.
  config.vm.box = "fedora/29-cloud-base"


  config.vm.provider "virtualbox" do |vb|
    # The default, 512, is little enough that sometimes the linker runs out
    # of memory:
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    dnf install -y \
      wget \
      rpm-build \
      go
    cd /home/vagrant
    ln -s /vagrant rpmbuild
  SHELL
end
