# -*- coding: utf-8 -*-
"""Ass3 yt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B9OTbiU-dCEslwnXsDsPEc-zJbod3Y7L
"""

# Importing required packages
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np

# a) Loading and Pre-processing the Image Data
# Loading the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # Splitting into training and testing data

# Reshaping the data to add a single channel (28, 28, 1) as input shape
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# Ensuring the values are float type for normalization
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizing the pixel values to the range [0, 1]
x_train /= 255
x_test /= 255

# Printing shapes for verification
print("Shape of training data:", x_train.shape)
print("Shape of testing data:", x_test.shape)

# b) Defining the Model's Architecture
model = Sequential()
model.add(Conv2D(28, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='softmax'))

# Displaying the model summary
model.summary()

# c) Training the Model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history=model.fit(x_train, y_train, epochs=2,validation_data=(x_test, y_test))

# d) Estimating the Model's Performance
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Loss: %.3f" % test_loss)
print("Accuracy: %.3f" % test_acc)

# Displaying an image from the dataset
image = x_train[3]
plt.imshow(np.squeeze(image), cmap='gray')
plt.show()

# Predicting the class of the image
image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
predict_model = model.predict(image)
print("Predicted class: {}".format(np.argmax(predict_model)))

plt.figure(figsize = (12,4))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.subplot(1,2,2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

