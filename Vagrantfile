Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"
  config.vm.provision "shell", path:"scripts/bootstrap.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5000 
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end
end
