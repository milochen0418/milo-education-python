
# Mac OS usage for blender 2.77 with anaconda environment  

## Download and install to Mac 
Goto https://download.blender.org/release/Blender2.77/    
I use blender-2.77-OSX_10.6-x86_64.zip   
Uncompress and copy it into /Applications/  

## Hack blender 2.77  to support anaconda
### query python version of your blender
import platform    
platform.python_version()    
Then you can find out it use python 3.5.1  
  
## set alias for blender, so that you can call blender in command-line directly
$ alias blender=/Applications/blender-2.77-OSX_10.6-x86_64/blender.app/Contents/MacOS/blender    
So you can call blender to invoke blender application in any folder  
  
## set conda environment for download blender app  
$ conda create -n python -c conda-forge python=3.5.1   
  
## Replace python sdk in blender application  
$ conda env list  
\# conda environments:  
\#  
base                  *  /Users/milochen/anaconda3  
audio-research           /Users/milochen/anaconda3/envs/audio-research  
linux-blockchain         /Users/milochen/anaconda3/envs/linux-blockchain  
python                   /Users/milochen/anaconda3/envs/python  
...  

You can find out that your created python environement is in ~/anaconda3/envs/python  
    
$ cd /Applications/blender-2.77-OSX_10.6-x86_64/blender.app/Contents/Resources/2.77  
$ mv python \_python    
$ ln -s ~/anaconda3/envs/python python    
  
Thus, you can use the following command to go to python environment
$ conda activate python   
You can install any package for your blender now, like tensorflow, python, or anything else    
  
  



