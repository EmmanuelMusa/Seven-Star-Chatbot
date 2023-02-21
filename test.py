# This is just a test page to check if pytorch is able to access Cuda with GPU
import torch

print(torch.cuda.is_available())
print(torch.__version__)
print(torch.version.cuda)