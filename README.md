# linux-networking-recipes
Administration scripts for configuring routers,switches,firewalls, nics, dhcp, dns etc' running on vagrant


When you change python code - you'll need to run vagrant reload in order for it to be changed in the VM. 
Run vagrant reload --provision in order to also run the provisioners again

https://www.vagrantup.com/docs/cli/reload.html

See also this link in order to understand how the files are arranged inside the vagrant VM:
https://stackoverflow.com/questions/36909407/run-a-python-script-in-vagrant
