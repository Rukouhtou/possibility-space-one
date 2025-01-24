import torch
import torch.nn as nn

class ConditionalFlowMatching(nn.Module):
    def __init__(self, model, q_sample, timesteps=1000):
        super().__init__()
        self.model = model
        self.timesteps = timesteps
        self.q_sample = q_sample

    def forward(self, x, condition):
        t = torch.randint(0, self.timesteps, (x.shape[0],), device=x.device)
        eps = torch.randn_like(x)
        x_t = self.q_sample(x, t, eps)
        eps_theta = self.model(x_t, t, condition)
        loss = nn.functional.mse_loss(eps, eps_theta)
        return loss