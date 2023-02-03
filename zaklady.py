# TensorFlow na viacrozmernych poliach (tenzoroch)
# prezentovanych ako objekty
import tensorflow as tf
# dvojrozmerny tenzor
x = tf.constant ([[1.,2.,3.],
                 [4.,5.,6.]])
print (x)
print (x.shape) # informuje o velkosti tenzora po kazdej z jeho osi
print (x.dtype) # informuje o type vsetkych prvkov v tenzore
# TensorFlow implementuje standardne matematicke operacie na tenzoroch
# scitanie 
print (x+x) 
# nasobenie
print (5*x) 
# Vrateny rozmer tenzora, zodpoveda vstupnemu rozmeru
# Operacia vykonava standardne beznu maticovu transformaciu na 2-d vstupnych tenzoroch
print (x @ tf.transpose(x)) 

print (tf.nn.softmax(x, axis=-1))
