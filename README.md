# cifar10
Initial commit

# CIFAR10 Web Model

This is a Streamlit web application that allows users to upload an image and get predictions based on the CIFAR10 model. The app processes the uploaded image, resizes it, and uses a pre-trained TensorFlow model to predict the class of the image.

## Features

- Upload an image (jpg or png) to get predictions.
- Choose a custom color for the prediction graph.
- Displays the probability of each class in the CIFAR10 dataset.

## Installation

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

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the web application in your browser.
2. Upload an image that fits into one of the CIFAR10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).
3. Choose a color for the prediction graph.
4. View the predictions and the probability graph.

## Files

- `app.py`: The main Streamlit application file.
- `cifar10_model1.keras`: The pre-trained TensorFlow model file.
- `requirements.txt`: List of required packages.

## Dependencies

- numpy
- matplotlib
- streamlit
- tensorflow
- Pillow

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- The CIFAR10 dataset is provided by the Canadian Institute For Advanced Research.
- The pre-trained model is based on TensorFlow.

## Contact

For any questions or suggestions, please contact joshtrineheart@gmail.com



## Contact

For any questions or suggestions, please contact your-email@example.com.

