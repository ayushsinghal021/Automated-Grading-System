import torch
from torch import nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.lin_k = nn.Linear(768, 768)  # Assuming we flatten the input tensor
        self.lin_q = nn.Linear(768, 768)
        self.lin_v = nn.Linear(768, 768)

    def forward(self, x):
        x = x.view(-1, 768)  # Flatten input
        k = self.lin_k(x)
        q = self.lin_q(x)
        v = self.lin_v(x)
        return k, q, v
