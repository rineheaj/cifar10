import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image






#GRPAH COLOR
selected_graph_color = st.color_picker(
    'Pick a color for the graph:', '#00f900'
)

def main():
    st.title('Cifar10 Web Model')
    st.write(
        'Upload any image that fits ' 
        'into one of the classes ' 
        'to see if prediction is correct.'
    )

    file = st.file_uploader(
        'Please upload an image', type=['jpg', 'png']
    )
    if file:
        image = Image.open(file)
        st.image(image=image, use_column_width=True)

        #PROCESS IMAGE TO CORRECT SIZE
        resized_image = image.resize((32, 32))

        #CREATE ARAY WITH RESIZED IMAGE
        img_array = np.array(resized_image) / 255

        #VARS=BATCH SIZE, PIXELS, PIXELS, RGB
        img_array = img_array.reshape((1, 32, 32, 3))
        
        #LOAD & RUN MODEL(CIFAR10)
        model = tf.keras.models.load_model(
            'cifar10_model1.keras'
        )

        predictions = model.predict(img_array)
        cifar10_classes = [
            'airplane',
            'automobile',
            'bird',
            'cat',
            'deer',
            'dog',
            'frog',
            'horse',
            'ship',
            'truck'
        ]

        #GRAPH THE RESULTS
        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))

        ax.barh(
            y_pos, predictions[0], align='center',
            color=selected_graph_color
        )

        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel('Probability')
        ax.set_title('CIFAR10 Predictions: ')
        

        st.pyplot(fig=fig)
    else:
        st.text('You have not uploaded an image yet.')

    




if __name__ =='__main__':
    main()

























