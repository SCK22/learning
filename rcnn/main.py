import os
import cv2
import json
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import keras 
import tensorflow as tf

# read config
with open("config.json", "r") as f:
    config = json.load(f)


images_path = config["images_path"]
annotations_path = config["annotations_path"]



