import os

NUM_FILTERS = 32
IMAGE_HEIGHT = 96
IMAGE_WIDTH = 128
NUM_CHANNELS = 3
INPUT_SHAPE = (96, 128, 3)
BATCH_SIZE = 32
BUFFER_SIZE = 1000
EPOCHS = 20
EPOCH_NUM = 40

path = ''
image_dir = os.path.join(path, "../data/image/")
mask_dir = os.path.join(path, "../data/mask/")