# TensorFlow na viacrozmernych poliach (tenzoroch)
# prezentovanych ako objekty
import tensorflow as tf
# dvojrozmerny tenzor
x = tf.constant ([[1.,2.,2.],
                 [4.,5.,6.]])
print (x)
print (x.shape) # informuje o velkosti tenzora po kazdej z jeho osi
print (x.dtype) # informuje o type vsetkych prvkov v tenzore
# TensorFlow implementuje standardne matematicke operacie na tenzoroch
print (x+x) # scitanie 
print (5*x) # nasobenie

