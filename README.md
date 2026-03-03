# CTFd-jumpbox-plugin
A plugin to provide user provisioning on a dedicated jumpbox.

# Usage
A server should be setup with a provisioning user and an SSH private key authentication. This user will be used to provision user accounts on the server for CTF participants. 

Once the CTFd server is brought up, go to `Jumpbox Config` in plugins and configure the address of the server that will be the jumpbox, the provision user name, and the provision user password. 

You will also want to add a page for `/jumpbox` so that users can access the panel to retrieve their team credentials. 

# Installation
If you are utilizing a docker version of CTFd, run the `install.py` file pointing it to the directory containing the CTFd application. If you are not using the standard dockerfile name you will also want to provide the dockerfile name.

If you are not using docker, ensure that you copy the `jumpbox` folder into the plugins directory and install the required dependencies.

# AWS SSM Integration (Optional)

Instead of manually configuring the jumpbox via the admin UI after each deploy, you can load configuration from AWS SSM Parameter Store. Set one or more of the following environment variables to the name of an SSM parameter:

| Environment Variable | SSM Parameter Contains | Notes |
|---|---|---|
| `JUMPBOX_SSM_KEY_PARAMETER` | SSH private key (PEM) | Stored as SecureString; fetched with decryption |
| `JUMPBOX_SSM_HOSTNAME_PARAMETER` | Jumpbox hostname/IP | Plain String parameter |
| `JUMPBOX_SSM_USERNAME_PARAMETER` | Provision username | Plain String parameter |

Each variable is optional and independent — set any combination. Configuration is loaded once at startup; restart CTFd to pick up SSM changes.

When all three values (key, hostname, username) are present after applying SSM config, the jumpbox is automatically enabled.

The admin UI will show an info banner when SSM integration is active. Manual changes made via the UI will be overridden on the next restart.

**AWS Credentials:** Uses the standard boto3 credential chain (instance role, environment variables, or shared credentials file). No custom credential configuration is needed.