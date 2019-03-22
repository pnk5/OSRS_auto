import tensorflow as tf
import os
import sys
import json
from object_detection.utils import dataset_util

flags = tf.app.flags
flags.DEFINE_string('trained_data', '', '')
FLAGS = flags.FLAGS

json_file = open('json1')
json_str = json_file.read()
data = json.loads(json_str)[0]
print(data)

def create_dataset(image, payload):
    height = 1040
    width = 1920
    filename = "images/" + image
    encoded_image_data = tf.gfile.FastGFile(filename, 'r').read()
    image_format = 'png'

    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []

    classes_text = []
    classes = []

    for box in payload:
        xmins.append(box[0][0])
        xmaxs.append(box[1][0])
        ymins.append(box[0][1])
        ymaxs.append(box[1][1])
        classes_text.append("iron")
        classes.append(0)

    tf_set = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image_data),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))

    return tf_set


# def main(_):
#     writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
#
#     # TODO(user): Write code to read in your dataset to examples variable
#
#     for example in examples:
#         tf_example = create_tf_example(example)
#         writer.write(tf_example.SerializeToString())
#
#     writer.close()
#
#
if __name__ == '__main__':
    tf.app.run()

