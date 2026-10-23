
import torch
import torch.nn as nn


class DeepfakeClassifier(nn.Module):
    """
    Baseline classifier for audio features.

    Input shape: (batch_size, 1, feature_count)
    Output: two logits — genuine and synthetic.
    """

    def __init__(self, input_features: int = 40):
        super().__init__()

        self.network = nn.Sequential(
            nn.Conv1d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1,
            ),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(16, 2),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        if features.ndim != 3:
            raise ValueError(
                "Expected input shape (batch, 1, features)"
            )

        return self.network(features)
