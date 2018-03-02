# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:55:49 2018

@author: Niko
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))