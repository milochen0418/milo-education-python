# Install Anaconda3 in Ubuntu 8.04   
## Download Anaconda Bash Script
$ cd /tmp  
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh  
## Verify Data integrity of installer  
$ sha256sum Anaconda3-2019.03-Linux-x86_64.sh  
and the output will be   
45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a  Anaconda3-2019.03-Linux-x86_64.sh  
## Run installer
$ bash Anaconda3-2019.03-Linux-x86_64.sh    
## chocie yes for all  
Type yes for [yes|no] when you see it.  
## load new setting by load bashrc  
$ source ~/.bashrc  
## Check the exists of conda to make sure your system is ready 
$ which conda  




