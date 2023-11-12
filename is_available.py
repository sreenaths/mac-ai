import torch

print("GPU acceleration is available: ", torch.backends.mps.is_available())
