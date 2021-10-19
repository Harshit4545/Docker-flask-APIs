
# Docker Flask APIs 

**Web Application to add , remove and update data in table**


# Get started

## Installation 

Install Docker Engine on Linux systems:

```bash
  sudo apt-get update
   
   sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
Add Docker’s official GPG key:

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

#### Install Docker Engine
Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:   
    
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io

To install a specific letest version of Docker Engine:

    sudo apt-get install docker-ce=5:18.09.1~3-0~ubuntu-xenial docker-ce-cli=5:18.09.1~3-0~ubuntu-xenial containerd.io

Verify that Docker Engine is installed correctly by running the hello-world image.

    sudo docker run hello-world


### Install Docker Compose on Linux systems


Run this command to download the current stable release of Docker Compose:
    
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

To install a different version of Compose, substitute 1.29.2 with the version of Compose you want to use.

Apply executable permissions to the binary:
    
    sudo chmod +x /usr/local/bin/docker-compose

Note: If the command docker-compose fails after installation, check your path. You can also create a symbolic link to /usr/bin or any other directory in your path.


For example:
   
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

Test the installation.

    docker-compose --version
 

### For winndows and mac user click on the link  for docker Engine  installation 
     
[ https://docs.docker.com/engine/install/ ]     

### For winndows and mac user click on the link  for docker Compose  installation 
[https://docs.docker.com/compose/install/]
   
     
## Usage
This Web application  running a service locally (localhost), using port 5000.

The application uses four routs:

1) ("/") route it is the defalut route  
2) ("/add") route it will use to add the data in table (when user click on add button it will take to add page )
3) ("/remove") route it is use to remove or delete the table data (when user click on remove button it will completely remove table data  )
4) ("/update") route it is use to update table data (when user click on update button it will take to update page)


## Running APIs

To run task file ,


1) Download file from  github [https://github.com/Harshit4545/Docker-flask-APIs]
2) Unzip the file  
3) Open the folder (task) 
4) In folder "right click" and select " open in teminal "
 Terminal look like

    harshit@harshit-SVE14116GNB:~/task$ 

5) Now run command:    

```bash
 sudo docker-compose up 

```

  