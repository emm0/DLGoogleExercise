'''
Created on Apr 17, 2018

@author: rr606770
'''


import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()

print(sess.run(hello).decode())
