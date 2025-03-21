# CTFd-jumpbox-plugin
A plugin to provide user provisioning on a dedicated jumpbox.

# Usage
A server should be setup with a provisioning user and an SSH private key authentication. This user will be used to provision user accounts on the server for CTF participants. 

Once the CTFd server is brought up, go to `Jumpbox Config` in plugins and configure the address of the server that will be the jumpbox, the provision user name, and the provision user password. 

You will also want to add a page for `/jumpbox` so that users can access the panel to retrieve their team credentials. 

# Installation
If you are utilizing a docker version of CTFd, run the `install.py` file pointing it to the directory containing the CTFd application. If you are not using the standard dockerfile name you will also want to provide the dockerfile name.

If you are not using docker, ensure that you copy the `jumpbox` folder into the plugins directory and install the required dependencies.