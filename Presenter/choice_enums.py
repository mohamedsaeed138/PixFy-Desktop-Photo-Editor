from enum import Enum


class GrayTabChoice(Enum):
    Empty = -1
    Threshold = 0
    Negative = 1
    Stretching = 2
    Equalization = 3
    LogTransform = 4
    PowerLaw = 5


class SharpeningChoice(Enum):
    Empty = -1
    Laplacian = 0
    CompositeLaplacian1 = 1
    CompositeLaplacian2 = 2


class SmoothingChoice(Enum):
    Empty = -1
    Gaussian = 0
    Box = 1
    Mean = 2
    Median = 3
    Max = 4
    Min = 5


class NoiseChoice(Enum):
    Empty = -1
    Gaussian = 0
    SP = 1


class EdgeDetectionChoice(Enum):
    Empty = -1
    Canny = 0
    SobelXY = 1
    SobelX = 2
    SobelY = 3
