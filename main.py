import torch 

class RMSNorm(torch.nn.Module):
    def __init__(self, dim:int, eps:float=1e-8):
        super().__init__()
        self.dim = dim
        self.eps = eps
        # 可以让模型学习自动更新权重
        self.weight = torch.nn.Parameter(torch.ones(dim))
    
    # 计算均方根
    def _norm(self, x):
        
        return torch.rsqrt(x.pow(2).mean(-1, keepdim=Ture)+ self.eps)

    # 前向传播
    def forward(self, x):
        rms = self._norm(x)
        return x * rms * self.weight
