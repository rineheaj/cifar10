# cifar10
Initial commit

# 🌟 CIFAR10 Web Model

This is a Streamlit web application that allows users to upload an image and get predictions based on the CIFAR10 model. The app processes the uploaded image, resizes it, and uses a pre-trained TensorFlow model to predict the class of the image.

## ✨ Features

- Upload an image (jpg or png) to get predictions.
- Choose a custom color for the prediction graph.
- Displays the probability of each class in the CIFAR10 dataset.
- Train a new model with your own dataset.

## 🚀 Installation

To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/rineheaj/cifar10.git
    cd cifar10
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

## 🛠️ Model Training

Before running the application, you need to train the model with your dataset. Follow these steps:

1. Prepare your dataset and place it in the appropriate directory.
2. Run the model training script:
    ```bash
    python model_trainer.py
    ```
3. The trained model will be saved as `cifar10_model1.keras`.

## 📊 Usage

1. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

2. Open the web application in your browser.
3. Upload an image that fits into one of the CIFAR10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).
4. Choose a color for the prediction graph.
5. View the predictions and the probability graph.

## 📁 Files

- `main.py`: The main Streamlit application file.
- `model_trainer.py`: The script to train the model with sample dataset. Script will create the cifar10_model1.keras file.
- `cifar10_model1.keras`: The pre-trained TensorFlow model file.
- `requirements.txt`: List of required packages.

## 📦 Dependencies

- numpy
- matplotlib
- streamlit
- tensorflow
- Pillow

## 📜 License

This project is currently not licensed under any agencies.

## 🙏 Acknowledgements

- The CIFAR10 dataset is provided by the Canadian Institute For Advanced Research.
- The pre-trained model is based on TensorFlow.

## 📧 Contact

For any questions or suggestions, please contact joshtrineheart@gmail.com.





