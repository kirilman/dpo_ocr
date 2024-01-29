import sys
# sys.path.append("../")
sys.path.append("./")
from app.main import sum, letterxyxy2org
import cv2
import numpy as np
import pandas as pd
def test_sum():
    assert sum(5, 5) == 10

def test_letterxyxy2org():
    assert letterxyxy2org(538, 512, 614, 711, 2339, 1653, 736, 520, 0, 108, 0.314664386489953) == (1366, 1627, 1608, 2259)
