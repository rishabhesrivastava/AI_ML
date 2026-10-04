During the COVID-19 pandemic, identifying whether individuals are wearing face masks has become a critical task. In this assignment, your objective is to develop a Convolutional Neural Network (CNN) model to classify face images as either "masked" or "unmasked."

Note:

To simplify the task, the dataset provided primarily includes images with a single face and minimal background interference. However, in real-world scenarios, challenges such as multiple faces, varied backgrounds, and different types of masks (e.g., patterned masks, skin-tone masks) may arise.

Dataset Description:

The dataset includes face images categorized into "masked" and "unmasked" folders. These images are further divided into training, validation, and testing sets, as shown below:

dataset/

+ train_validate/

unmasked/ (840 images)

 masked/ (840 images)

 test/

 unmasked/ (160 images)

 masked/ (160 images)

Task

You may use Python libraries to solve the tasks outlined below:

1. Prepare the Dataset

Load the dataset into appropriate data structures, ensuring images are resized to 64x64x3 to be fed as input to the CNN. [1 mark]

2. Build the CNN Model

Using TensorFlow and Keras, create a CNN model with the following indicative architecture:

Convolution Layer → Activation Function (ReLU) → Pooling Layer

(Convolution Layer → Activation Function) × 2 → Pooling Layer

Fully Connected Layer → Activation Function

Softmax Classifier

Use a pool size of 2x2, filter size of 3x3, and any other standard parameters as needed. [2 marks]

3. Train the Model

Train the model for 70 epochs (E=70). Log and plot the following metrics for each epoch:

Training Loss

Training Accuracy

Validation Loss

Validation Accuracy

Save these metrics and present them as a graph after training is complete. [4 marks]

4. Evaluate the Model

Test the trained CNN on the testing dataset and print the classification metrics, including precision, recall, and F1-score. [2 marks]

5. Model Improvement

Modify the default CNN model to improve its performance. For example, you may change hyperparameters, add layers, or use techniques like data augmentation. Compare the performance of the original ("default") and modified ("improved") models by plotting precision and recall side-by-side in a bar chart. [2 marks]

Visualize Predictions

Display 5 sample images from the test set predicted as "masked" and 5 predicted as "unmasked." Include the predicted labels for each image. [1 mark]

Submission Guidelines:

Consolidate the code, plots, and results in a single Jupyter Notebook file.

Submit both the .ipynb file and an HTML export of the notebook.

Ensure the notebook includes all required outputs, such as the model architecture, training graphs, evaluation metrics, and sample predictions.