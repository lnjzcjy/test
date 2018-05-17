# you must import tensorflow numpy  and matplotlib.pyplot as basic lib and version must be right tensorflow with 2.7 python ..you
#may need new python or tensorflow 

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#there are  TWO parts first  define you need many tf.class to orgniaze together to define a GRAPH
#                     second USE tf.session() to use the  GRAPH
# THIS PART DEFINE THE GRAPH also means the function you computer....so easy
# tensor is a nod  and flow as it flow into so in tensorflow everyone is a tf.class() su as placeholder add subtract ..you
#OUTPUT = SIGMA (z = xw + b )  W weight ,b bias , sigma  active function
# w ,b in holder  x in various
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.add(a,b)
# tf.sub() tf.mul()  must look for the right function name!!!
# 
