import torch
print(torch.cuda.is_available())
# True 
import torch
print(torch.cuda.get_device_name(0))
# 'GeForce GTX 1080 Ti'
import torch
print(torch.cuda.device_count())
# 2
