Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"

  config.vm.provision "shell", 
    path:"scripts/bootstrap.sh"

  config.vm.provision "shell",
  path:"scripts/ProvisionScripts.sh"

  config.vm.provision "shell", 
    path:"scripts/f_hw.py"

end
