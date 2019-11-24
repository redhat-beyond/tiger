Vagrant.configure("2") do |config|
  config.vm.box = "dummy"
  config.vm.provider :aws do |aws, override|
  config.vm.synced_folder ".", "/vagrant", disabled: true
    aws.access_key_id = ""
    aws.secret_access_key = ""
    aws.keypair_name = "vagrant_aws"

    aws.ami = "ami-007d7bab5073aaddb"
    aws.instance_type = 't1.micro'
    aws.security_groups = [ 'aws-ssh' ]
    override.ssh.username = "fedora"
    override.ssh.private_key_path = "/Users/daniel/.ssh/id_rsa"
  end
end
