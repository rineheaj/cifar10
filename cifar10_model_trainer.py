import tensorflow as tf

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D

def main():
    (X_train, y_train), (X_val, y_val) = cifar10.load_data()
    X_train = X_train / 255.0
    X_val = X_val / 255.0

    y_train = to_categorical(y_train, 10)
    y_val = to_categorical(y_val, 10)

    model = Sequential([
        # Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        # MaxPooling2D((2, 2)),
        Flatten(),
        Dense(1000, activation='relu'),
        Dense(10, activation='softmax')
    ])



    model.compile(loss='categorical_crossentropy', 
                optimizer='adam',
                metrics=['accuracy'])

    model.fit(X_train, y_train, batch_size=64, 
            epochs=10, validation_data=(X_val, y_val))

    model.save('cifar10_model1.keras')

if __name__ =='__main__':
    main()

