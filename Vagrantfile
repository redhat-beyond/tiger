Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"
  config.vm.provider "virtualbox" do |v|
    v.name = "tiger_dev"
    v.memory = 2048

  config.vm.provision "shell",
  path:"scripts/bootstrap.sh"

end
