# Sudoku Solver





<img src="readme-lib\sudoku-logo.png" alt="Logo" width="30%"/>





Sudoku is described as a 9-by-9 grid problem with 3-by-3 boxes. There must be no duplicates in each row, column, and box. In this project, a sudoku solver is designed that employs computer vision to recognise a sudoku puzzle, image processing to retrieve the puzzle's cells, machine learning to determine the number of the cell, and finally tries to solve it. The objective of this research is to detect a sudoku puzzle in a given image using image processing and recognise the digits of the puzzle using machine learning, resulting in a 9-by-9 grid of digits that represents the puzzle. Finally, to solve the identified puzzle and generate a solution



Let's solve a sudoku puzzle: [Sudoku Solver](https://sudoku.shohrab.com)





**Table of content**

---

[TOC]





# 1. Architecture

A computer vision-based sudoku solver is developed in this project, which takes a puzzle image as input and processes it to detect the actual puzzle in the image. The identified puzzle is then cropped to 9 rows and 9 columns in each row, for a total of 81 cells. These cells are then sent into a Convolutional Neural Network, which predicts the digit the cell contains. Following prediction, the puzzle's 81 digits are recognized and split into a 9-by-9 grid that represents the puzzle.This grid is then fed to a sudoku solver, which attempts to solve the puzzle and eventually generates the solution.

The [Image Processing Unit](#1.1.-image-processing-unit) , [Digit Recognition Unit](#1.2.-digit-recognition-unit), and [Puzzle Solver Unit](#1.3.-puzzle-solver-unit) are the three fundamental units of the chatbot system's architecture. The chatbot's architecture is depicted in the figure.





<img src="readme-lib\architecture\Architecture.png" alt="Logo" width="80%"/>





> Figure: Architecture







## 1.1. Image Processing Unit

The image processing unit's objective is to detect the actual problem in the image, crop the puzzle, then split the cropped image into 9 rows and 9 columns in each row, for a total of 81 cells. The cells were then further cropped for better prediction, and the list of cells was supplied to a digit recognition unit.





<img src="readme-lib\architecture\Image-Processing-Unit.png" alt="Logo" width="70%"/>





> Figure: Block Diagram of Image Processing Unit







### 1.1.1. Resizing the Image

The puzzle image will be scaled to 450-by-450 form in this section so that the following section may crop the appropriate portion of the image properly.





### 1.1.2. Detecting the Contours of the Image

The contours of the scaled image are detected in this section. With contour detection, you can simply determine the edges of objects and localise them in an image. Many intriguing applications, such as image-foreground extraction, simple-image segmentation, detection, and recognition, use it as the first step.



 

<img src="readme-lib\architecture\contourDetection.png" alt="Logo" width="90%"/>





> Figure: Contour Detection of Image Processing Unit





### 1.1.3. Cropping the Image and Making Well-Aligned

In this step, the largest detected contour is chosen using maximum area, and the largest contour is cropped to obtain the actual puzzle and remove all other objects from the image. After cropping the largest contour, the cropped image is reframed so that it has a specific dimension, and then further image processing is performed.

 



<img src="readme-lib\architecture\croppedImage.png" alt="Logo" width="90%"/>





> Figure: Cropping and Reframing the puzzle from image





### 1.1.4. Splitting the Image into 81 Cells

In this stage, the cropped and reframed puzzle image is divided into 9 rows with 9 columns in each row. This results in 81 images, which are the cells of the sudoku puzzle. These 81 cells will then be fed into a digit recognition system, which will predict their numbers.









## 1.2. Digit Recognition Unit

A Convolution Neural Network (CNN) is designed to recognise the digits of cells. The digit recognition unit will loop through the 81 cells and feed the image to the CNN, where the ml model will predict the digit on the image. The parameters of the designed CNN are provided in the tables below.





**Table: Compiling parameters of the Deep Neural Network**

|  Parameter  Name  |  Value  |
| :---------------: | :-----: |
|     Optimizer     | RMSprop |
|  Learning  Rate   |  0.001  |
|        rho        |   0.9   |
|      epsilon      |  1e-08  |
|       decay       |   0.0   |
| Number  of Epochs |   200   |





**Table: Design parameters of the Deep Neural Network**

|      **Layer**       | **Attribute** | **Value** | **Activation** |
| :------------------: | :-----------: | :-------: | :------------: |
| Convolution Layer 01 |     shape     | (32, 32)  |      relu      |
| Convolution Layer 02 |     shape     | (32, 32)  |      relu      |
| Max-Pooling Layer 01 |   pool_size   |  (2, 2)   |     **--**     |
| Convolution Layer 03 |     shape     | (16, 16)  |      relu      |
| Convolution Layer 04 |     shape     | (16, 16)  |      relu      |
| Max-Pooling Layer 01 |   pool_size   |  (2, 2)   |     **--**     |
|     Dense  Layer     |    neuron     |    500    |      relu      |
|  Output Dense Layer  |    neuron     |    10     |    softmax     |







### 1.2.1. Learning Curve Evaluation

The learning curve of the training cycle is illustrated below.





<img src="readme-lib\results\lossCurve.png" alt="Logo" width="70%"/>



> Figure: Learning Curve of Training Cycle 







The learning curve is flat across all epochs, and the curves do not divide into any gaps. Despite the fact that the curve shows that the model is not well-fit, it can forecast with reasonable accuracy. On rare occasions, the model will predict the incorrect class.







### 1.2.2. Confusion Matrix Evaluation

The Confusion Matrix of the training cycle is illustrated in the below figure.



<img src="readme-lib\results\ConfusionMatrix.png" alt="Logo" width="80%"/>





> Figure: Confusion Matrix of the Training Cycle 





Only the True Positive and True Negative values are present in the entire class. None of the classes have any False values recorded. The classification report shows that the model is accurate and error-free in its classification





### 1.2.3. Classification Report Evaluation

The Classification Report includes details on the F1-Score, Accuracy, Precision, and Recall. These metrics give an indication of the model's categorization performance. The classification report's conclusions are depicted in the table below.



**Table: Findings of the Classification Report Analysis**

| Evaluation Metric | Value (%) | Decision |
| :---------------: | :-------: | :------: |
|     Accuracy      |    100    |  Ideal   |
|     Precision     |    100    |  Ideal   |
|      Recall       |    100    |  Ideal   |
|     F1-Score      |    100    |  Ideal   |











## 1.3. Puzzle Solver Unit

This section takes the puzzle's predicted digits, which are essentially a 9-by-9 grid of 81 cells in 2D array format. This solver part will then attempt to solve the puzzle in accordance with the puzzle's rules, eventually generating the solution.











---

Let's solve a sudoku puzzle: [Sudoku Solver](https://sudoku.shohrab.com)