Vagrant.configure("2") do |config|

  config.vm.define "fedora", primary: true do |fedora|
   fedora.vm.box = "fedora/30-cloud-base"
   fedora.vm.provision "shell", path:"scripts/bootstrap.sh"
   fedora.vm.network "forwarded_port", guest: 5000, host: 5000
   fedora.vm.provider "virtualbox" do |v|
     v.memory = 1024
  end
end

  config.vm.define "ubuntu" do |ubuntu|
   ubuntu.vm.box = "ubuntu/bionic64"
   ubuntu.vm.provision "shell", path:"scripts/bootstrap.sh"
   ubuntu.vm.network "forwarded_port", guest: 5000, host: 5000
   ubuntu.vm.provider "virtualbox" do |v|
     v.memory = 1024
  end
end

  config.vm.define "stage" do |stage|
    stage.vagrant.plugins = "libxml2-dev"
    stage.vagrant.plugins = "vagrant-aws"
    stage.vm.box = "dummy"
    stage.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    stage.vm.provider :aws do |aws, override|
    stage.vm.synced_folder ".", "/vagrant", 
      disabled: false

        stage.vm.provider :aws do |aws,override|
          aws.keypair_name = "tiger"
          aws.ami = "ami-0987ee37af7792903"
          aws.instance_type = "t2.micro"
          aws.region = "eu-west-1"
          aws.subnet_id = "subnet-ea3010a2"
          aws.security_groups = "sg-0f39480a6f4adf517"
          aws.associate_public_ip = true
          
          override.ssh.username = "ubuntu"
          override.ssh.private_key_path = "~/.ssh/tiger.pem"
      end
    end
end
end