import tensorflow as tf

from object_detection.utils import dataset_util

flags = tf.app.flags
flags.DEFINE_string('trained_data', '', '')
FLAGS = flags.FLAGS

def create_dataset(indata):
