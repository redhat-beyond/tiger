Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"

  config.vm.synced_folder ".","/home/vagrant/tiger.sync"

  config.vm.provision "shell",
  path:"scripts/ProvisionScripts.sh"

end
