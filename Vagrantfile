flag = true
while flag
 puts "Input environments ['dev' or 'stage']: "
 chosen_environment = STDIN.gets.chomp
 if chosen_environment == "dev" or chosen_environment == "stage"
   flag = false
 end
end

Vagrant.configure("2") do |config|


if chosen_environment == "dev"
puts "I'm in dev"
  config.vm.define "dev" do |dev|
   config.vm.box = "fedora/30-cloud-base"
   config.vm.provision "shell", path:"scripts/bootstrap.sh"
   config.vm.network "forwarded_port", guest: 5000, host: 5000
   config.vm.provider "virtualbox" do |v|
     v.memory = 1024
  end
end
else
puts "I'm in stage"

  config.vm.define "stage" do |stage|
    config.vagrant.plugins = "libxml2-dev"
    config.vagrant.plugins = "vagrant-aws"
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    config.vm.provider :aws do |aws, override|
    config.vm.synced_folder ".", "/vagrant", 
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
end
