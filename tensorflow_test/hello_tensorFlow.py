#!/usr/bin/python3
# -*- coding:utf-8 -*-

import tensorflow as tf
import os

# 压制警告
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

tf.enable_eager_execution()
print(tf.add(1, 2))

hello = tf.constant('hello,tensorflow')
print(hello.numpy())
