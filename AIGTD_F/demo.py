import tensorflow as tf

from keras import layers

new_model = tf.keras.models.load_model('C:/Users/91939/OneDrive/Desktop/AIGTD_F/models/my_model.h5')
new_model.summary()