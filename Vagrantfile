Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provision "shell",
  path:"scripts/Bootstrap.sh"

end
