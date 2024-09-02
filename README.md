# cifar10
Initial commit

# <span style="color: #1E90FF;">CIFAR10 Web Model</span>

This is a Streamlit web application that allows users to upload an image and get predictions based on the CIFAR10 model. The app processes the uploaded image, resizes it, and uses a pre-trained TensorFlow model to predict the class of the image.

## <span style="color: #32CD32;">Features</span>

- Upload an image (jpg or png) to get predictions.
- Choose a custom color for the prediction graph.
- Displays the probability of each class in the CIFAR10 dataset.
- Train a new model with your own dataset.

## <span style="color: #FF4500;">Installation</span>

To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/my-streamlit-app.git
    cd my-streamlit-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## <span style="color: #8A2BE2;">Model Training</span>

Before running the application, you need to train the model with your dataset. Follow these steps:

1. Prepare your dataset and place it in the appropriate directory.
2. Run the model training script:
    ```bash
    python model_trainer.py
    ```
3. The trained model will be saved as `cifar10_model1.keras`.

## <span style="color: #FFD700;">Usage</span>

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the web application in your browser.
3. Upload an image that fits into one of the CIFAR10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).
4. Choose a color for the prediction graph.
5. View the predictions and the probability graph.

## <span style="color: #FF69B4;">Files</span>

- `app.py`: The main Streamlit application file.
- `model_trainer.py`: The script to train the model with your dataset.
- `cifar10_model1.keras`: The pre-trained TensorFlow model file.
- `requirements.txt`: List of required packages.

## <span style="color: #00CED1;">Dependencies</span>

- numpy
- matplotlib
- streamlit
- tensorflow
- Pillow

## <span style="color: #DC143C;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.

## <span style="color: #7FFF00;">Acknowledgements</span>

- The CIFAR10 dataset is provided by the Canadian Institute For Advanced Research.
- The pre-trained model is based on TensorFlow.

## <span style="color: #FF6347;">Contact</span>

For any questions or suggestions, please contact joshtrineheart@gmail.com



