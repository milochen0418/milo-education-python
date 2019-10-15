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

# Install tensorflow 2.0 by conda  
## Create 
$ conda create -n tensorflow2.0 python=3.6 cudnn cupti cudatoolkit=10.0    
You will see that the tensorflow2.0 conda environment is in list by the following command   
$ conda env list   
...  
tensorflow2.0  
...  
  
## Jump in tensorflow2.0 conda environment 
$ conda activate tensorflow2.0  
   
## install tensowflow2.0 with GPU in your current conda environment  
$ pip install tensorflow-gpu  

### Check it exists in environment 
$ python   
>>> import tensorflow  
>>> tensorflow.__version__  
2.0.0  
  
When you see this information, it mean your tensorflow2.0 is ready in this conda environemnt 'tensorflow2.0'  
