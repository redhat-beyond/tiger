# tiger

Instruction for spin VM and destroy:

1. Install vagrant
2. Install virtualbox
3. Run 'vagrant up'
4. Run 'vagrant ssh'
5. In the end of work, logout from the machine
6. Run 'vagrant destroy -f'

# Our best practices:

- Ask questions in the Slack group.
- Scroll any command at the Git Guide and learn how to use it.

# How to add tables to the Database

- Edit the 'MYSQL_SCRIPT' section in the 'bootstrap.sh' file using your favorite editor.
- Add the corresponding SQL command after the 'USE tiger' command.
- Don't forget to save your changes with :wq!

# Spin VM on AWS (stge)

- Go to your AWS console -> EC2 -> Key pairs -> Create key pair
- Name: tiger + File format: pem
- Move the file from Downloads to ~/.ssh

# Additional steps for Windows users

- Move to the tiger folder
- run those commands-
  vagrant plugin install --plugin-version 1.0.1 fog-ovirt
  vagrant plugin install vagrant-aws

# Run vagrant

- vagrant up
- stage
