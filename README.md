# ODPi sandbox automation

An open framework for building ODPi compliant sandboxes.

Quickstart
----------

````shell
# Building the sandbox
cd packer
./make.sh
````

````shell
# Running the sandbox
cd vagrant
vagrant up
````

Prerequisites
-----------
* packer - https://www.packer.io/
* vagrant - https://www.vagrantup.com/


Code in this repository was heavily referenced from:
* https://github.com/geerlingguy/packer-centos-7
* http://www.tecmint.com/multiple-centos-installations-using-kickstart/
* https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Installation_Guide/sect-kickstart-syntax.html
* http://serverascode.com/2014/03/29/squid-cache-yum.html


