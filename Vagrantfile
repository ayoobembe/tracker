# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  #fix no_tty_error:
  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = "false"
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end
  #Using hashicorp provided box: precise64
  config.vm.box = "hashicorp/precise64"

  #location from which to download box if not already on users computer
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  #formward a port from the guest to the host (localhost:8080)
  config.vm.network "forwarded_port", guest: 80, host: 8080

  #install and build essential packages
  config.vm.provision :shell, :inline => "sudo aptitude -y install build-essential"

  #update chef automatically
  config.vm.provision :shell, :inline => "gem install --no-ri --no-rdoc chef"

  #enable provisioning with chef_solo
  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path = %w{cookbooks site-cookbooks}
    chef.add_recipe "postgresql::server_debian"
    chef.add_recipe "postgresql::ruby"
    chef.add_recipe "redis::server"
    chef.add_recipe "git"
    chef.add_recipe "mercurial"
    chef.add_recipe "emacs"
    chef.add_recipe "vim"
    chef.add_recipe "tracker::database"
    chef.json = {
      :postgresql => {
        :listen_addresses => '*',
        :password => {:postgres => "tracker"}
      },
      :redis => {
        :config => {
          :listen_addr => '0.0.0.0'
        },
        :install_type => 'source',
        :source => {
          :version => '2.8',
        },
      },
    }
  end
  # Share an additional folder to the guest VM: "path_on_host","path_on_guest"
  # config.vm.synced_folder "../data", "/vagrant_data"
end
