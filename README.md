# Hermon Asmelash

## Cherry Leaves Mildew Detection

Farmy & Foods' prize product - their cherry planntation - has a growing powdery mildew problem. The symptoms of powdery mildew in cherry leaves typically begin as small, circular, white spots on the upper surfaces of leaves. As the disease progresses, the spots may coalesce and form a powdery white or grayish film that covers the entire leaf surface. Infected leaves may also become distorted, curl, and eventually fall off the tree. 

The process of visually detecting this fungul infection and applying compounds to kill it is time consuming and untenable, especially as the business continues to grow. This project aims to create a dashboard app that plots differences between healthy and mildew-containing cherry leaves as well as develop a ML model that can predict whether a given image is a healthy cherry leaf or contains powdery mildew. 

[Link to the deployed application.](https://cherry-leaves-mildew-detection.herokuapp.com/)

![Screenshot 2023-04-07 at 09 13 17](https://user-images.githubusercontent.com/103432143/230570486-227a3e79-c4ee-4158-9885-10c89acc49d4.png)

## Table of Contents

[Planning](#planning)
- [Business Requirements](#business-requirements)
- [Hypothesis](#hypothesis-and-how-to-validate)
- [Map Business Requirements](#map-business-requirements)
- [ML Business Case](#ml-business-case)
- [User Stories](#user-stories)
- [Dashboard Design](#dashboard-design)

[Screenshots](#screenshots)

[Future Features](#future-features)

[Testing](#testing)

[Unfixed Bugs](#unfixed-bugs)

[Technologies Used](#technologies-used)

[Deployment](#deployment)
- [Heroku](#heroku)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

## Planning 

### Business Requirements

The IT team of Farmy & Foods have proposed training a model using thousands of images depicting both healthy and powdery mildew-containing cherry leaves to enable the prediction of whether a given cherry leaf is healthy or not. If successful, this could be extended to detecting pests for other crops and provide a practical solution to the problem that has been plaguing them. In addition the average image pattern and image variability will be plot to determine the differences between healthy cherry leaves and those containing powdery mildew.

To summarise, the business requirements are as follows:

1. The client is interested in visualising the differences between healthy cherry leaves and those containing powdery mildew. 

2. The client is interested in predicting whether a given cherry leaf is healthy or contains powdery mildew.


### Hypothesis and how to validate?

Hypothesis 1 - We believe that mildew containing cherry leaves can be detected by the white specks covering the leaf's surface.

How to validate? - By using average image and image variability plots. Average image plots will determine patterns across images belonging to a particular label so the client can see the most dominant features of the images. Image variabilty plots will allow the client to determine the variation between images belonging to the same label - with parts that are darker indicating the least variation. The differences between average images of both labels will also be plotted.

Hypothesis 2 - We believe a model can be trained to determine whether a given cherry leaf is healthy or contains powdery mildew with a degree of 97% accuracy.

How to validate? - By training and validating a model using a Convolutional Neural Network (CNN) until it reaches that accuracy. Plotting accuracy and loss plots to ensure there is no underfitting (the model failing to learn) or overfitting (the model fails to predict on unseen data). Finally, the test set will be evaluated using the saved model to ensure the accuracy is above 97%. 

### Map Business Requirements

The CRoss Industry Standard Process for Data Mining (CRISP-DM) is used as a rationale to map business requirements to the Data Visualisations and ML tasks. It has six phases:

![](https://www.datascience-pm.com/wp-content/uploads/2021/02/CRISP-DM.png)

1. Business Understanding 
* This addresses what Farmy & Foods needs from this project. The problem the project solves for the company. 
* Farmy & Foods needs a less time consuming method of detecting whether a cherry leaf is infected with mildew. 
* Farmy & Foods also wishes to visualise the differences between healthy and powdery mildew-containing cherry leaves.

2. Data Understanding
* This addresses whether we have the data that we need. For this project a dataset with 4208 images of labelled cherry leaves from [kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) will be downloaded using Jupyter Notebooks.
* The dataset will then be checked for non-image files (those that didn't end with image file extensions) and if any are found, they'll be deleted. 

3. Data Preparation 
* This addresses organising the data for modelling. 
* The dataset will be split into train, validation and test sets (70%, 15%, 15% split respectively). For training the model, optimising the model and testing the model.
* The dataset distribution will be plotted to ensure label balance so the model isn't biased toward one label and fail to predict the other as well.
* Image Augmentation will be used to increase the number of training images by creating variations of the existing ones. This will reduce overfitting.

4. Modelling
* This addresses what modelling techniques will be used.
* As the goal is to predict the label of an image - this is a Classification task. Binary as there are only two labels.
* Deep learning models are used for image classification. This project will use a Convolutional Neural Network (CNN).
* Layers will be stacked and arranged to form a neural network using a sequential model. 
* Layers that will be used are - convolution, pooling, flatten, dense and dropout layers. The latter is to prevent overfitting.
* The layers will generally use a ReLu activation function while the output layer will use a Sigmoid activation function (as it is binary classification).
* Optimisers and Loss Function will be used to monitor the performance (Adam and Binary Crossentropy respectively).

5. Evaluation 
* This addresses the ML performance and whether the accuracy of the model is above 97% (and therefore business requirements have been met).
* Loss and Accuracy plots for train and validation sets will help determine whether the model has fit normally (i.e. it is not underfitting or overfitting).
* The test set will be evaluated to determine its accuracy and loss values.

6. Deployment
* This addresses how the client can view and assess the model.
* Streamlit will be use to display the visualisation plots and the image montage on the dashboard
* The client will also be able to upload images of cherry leaves to predict which labels they belong to in real time.
* The ML performance will be displayed on the dashboard.

### ML Business Case

1. What are the business requirements?
* 1. The client is interested in visualising the differences between healthy cherry leaves and those containing powdery mildew. 
* 2. The client is interested in predicting whether a given cherry leaf is healthy or contains powdery mildew.

2. Is there any business requirement that can be answered with conventional data analysis?
* Yes, the first business requirements, data visualisation can be answered with conventional data analysis. Calculating the mean and standard deviation of the images to plot them.

3. Does the client need a dashboard or an API endpoint?
* Dahboard.

4. What does the client consider as a successful project outcome?
* Visual display of the differences between healthy cherry leaves and those containing powdery mildew.
* The training of a model that can accurately predict what class a given cherry leaf image belongs to.

5. Can you break down the project into Epics and User Stories?
* Yes, see User Stories section. 

6. Ethical or Privacy concerns?
* The client provided the data under an NDA (non-disclosure agreement).

7. Does the data suggest a particular model?
* Yes, a binary classifier.

8. What are the model's inputs and intended outputs?
* Inputs - Cherry leaf image.
* Outputs - Predicted label - healthy or powdery mildew.

9. What are the criteria for the performance goal of the predictions?
* 97% accuracy (or higher) was agreed upon with the client. 

10. How will the client benefit?
* Powdery mildew containing cherry leaves will not be released to the market, compromising the company. 

### User Stories

[User Stories](https://github.com/Hasmelash95/cherry-leaves-mildew-detection/blob/main/USERSTORY.md)

Acceptance Criteria are defined under the Issues tab. 

[Link to kanban board](https://github.com/users/Hasmelash95/projects/5)

### Dashboard Design

The client can navigate between the pages using radio buttons on the left. 

* Summary Page
* * Introduction text
* * Image of cherries on a cherry tree
* * Solution text
* * Business requirements
* * Link to README

* Visualisation Page
* * Buttons to reveal each graph 
* * Business requirement 1 at the top of the page
* * Image dimensions scatter plot (height vs width)
* * Image dimensions distrubiton graphs
* * Average healthy image plot
* * Average powdery mildew image plot
* * Plot of differences between average healthy image and average powdery mildew 
* * Image Montage with a selector tool for each label

* Mildew Detector
* * Business requirement 2 at the top of the page
* * Link to download dataset from kaggle
* * File uploader to upload cherry leaf image
* * Prediction text, probability graph and analysis report when image is uploaded

* Hypothesis Page
* * Hypothesis 1 - We believe that mildew containing cherry leaves can be detected by the white specks covering the leaf's surface.
* * Validation of hypothesis 1
* * Hypothesis 2  - We believe a model can be trained to determine whether a given cherry leaf is healthy or contains powdery mildew with a degree of 97% accuracy.
* * Validation of hypothesis 2

* ML Performance Page
* * Bar plot of label distribution 
* * Pie chart of label distribution
* * Accuracy plot for train and validation set
* * Loss plot for train and validation set
* * Generalised performance on test set

## Screenshots

Summary Page

![Screenshot 2023-04-06 at 16 56 58](https://user-images.githubusercontent.com/103432143/230435459-c5d0f81a-3701-4bc9-9aba-f11ed962cfab.png)

![Screenshot 2023-04-06 at 16 57 08](https://user-images.githubusercontent.com/103432143/230435495-70f59a49-4202-43eb-92a4-6cbf49ef427d.png)

Visualisation Page

![Screenshot 2023-04-06 at 16 57 15](https://user-images.githubusercontent.com/103432143/230435533-b0130416-ce3f-441f-8ef1-db38657cd2b5.png)

![Screenshot 2023-04-07 at 11 41 34](https://user-images.githubusercontent.com/103432143/230595649-90ea53f7-156e-4039-a4c0-b7b1b1a0c299.png)

![Screenshot 2023-04-06 at 16 57 34](https://user-images.githubusercontent.com/103432143/230435609-8a1a77e7-3c51-470b-8366-011507946a21.png)

Mildew Detector

![Screenshot 2023-04-06 at 16 53 45](https://user-images.githubusercontent.com/103432143/230435657-39c5e833-465b-4379-872c-521aae8cd9be.png)

Hypothesis Page

![Screenshot 2023-04-07 at 11 40 08](https://user-images.githubusercontent.com/103432143/230595573-c43c1d03-7de4-4fd1-be79-0ad8d50b595e.png)

ML Performance Page

![Screenshot 2023-04-06 at 16 57 52](https://user-images.githubusercontent.com/103432143/230435843-9f7bb68b-0c47-4a96-8b5f-e8295b2762a7.png)

![Screenshot 2023-04-06 at 16 58 00](https://user-images.githubusercontent.com/103432143/230435868-e8ad811e-1129-43e6-b5e3-da187cf78631.png)

![Screenshot 2023-04-06 at 16 58 08](https://user-images.githubusercontent.com/103432143/230435926-a3a49306-2b96-4d6a-82a6-adb91a049933.png)

![Screenshot 2023-04-07 at 11 41 16](https://user-images.githubusercontent.com/103432143/230595618-8158d4f8-dc9e-4b4f-b454-98779a80d9c9.png)

## Future Features

* Include images of half a cherry leaf during model training for a more accurate model.
* Apply this model and project to other crops that are dealing with a pest problem.
* Add user authentication to allow client only access.

## Testing

![Screenshot 2023-04-07 at 05 13 13](https://user-images.githubusercontent.com/103432143/230539553-3a4d51b6-1597-4609-82a7-cdf5933efc2c.png)

The tests were carried out on macOS and Windows devices. The browsers tested were: Google Chrome, Microsoft Edge, Safari and Firefox. All passed.

Acceptance Criteria for the user stories [seen here](https://github.com/Hasmelash95/cherry-leaves-mildew-detection/issues) were fulfilled. 

## Unfixed Bugs
* There are no unfixed bugs present. 

## Deployment

### Heroku

* The App live link is: https://cherry-leaves-mildew-detection.herokuapp.com/

* The project was deployed to Heroku using the following steps.

1. Ensure there is a setup.sh file that contains streamlit configuration and a runtime.txt file that has set the python environment to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
2. Push the code using "git push" on the command line of the IDE. (i.e. gitpod). 
3. Create a Heroku account or log in if you have one.
4. Click on the "Create new app" button on the dashboard.
5. Give the app a unique name.
6. Select your region.
7. Connect to Github under deployment method, search the repository you wish to link to and click 'connect'.
8. Choose the branch you wish to deploy.
9. Select either automatic or manual deploy. The former rebuilds the app everytime you git push.
10. If the slug size is too large then add large files not required for the app to the .slugignore file. 
11. Is a Heroku error states the python version is unavailable, logon to the Heroku CLI and enter this in the terminal: heroku stack:set heroku-20
12. You will see an "App was successfully deployed" message.
13. The application can be run by clicking 'Open App'.

### Cloning the Repository
1. Log on to your Github account and head to the main page of the repository you wish to clone.
2. Click on the 'Code' button above the list of files and choose from HTTPS, SSH or Github CLI, to copy the URL provided.
3. Open terminal and ensure you are in the correct location.
4. Type in 'git clone' and paste the URL you'd copied in step 2 and press enter.

## Technologies Used

* Python 3.8.12
* Jupyter Notebooks
* GitHub
* Git
* Gitpod
* Heroku

### Libraries Used

* NumPy 1.19.2
* Pandas 1.1.2
* Matplotlib 3.3.1
* Seaborn 0.11.0
* Plotly 4.12.0
* Tensorflow 2.6.0
* Streamlit 0.85.0


## Credits 

* Source for the cherry tree image on the Summary Page - Photo by Irina Iriser: https://www.pexels.com/photo/red-cherries-3220347/
* Cherry leaves dataset taken from Kaggle - https://www.kaggle.com/datasets/codeinstitute/cherry-leaves
* Information on cherry leaves and powdery mildew from [Washington State University](https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/) and [ChatGPT](https://openai.com/blog/chatgpt).
* Code Institute was the source of the template and the information from the fictional company - Farmy & Foods.
* CRISP-DM diagram taken from https://www.datascience-pm.com/crisp-dm-2/


## Acknowledgements 
* I would like to thank my mentor Rohit Sharma for his guidance during this project. 
* Code Institue for the learning material that helped me during the project.
* My friend, Daniel Jones for his typo checks. 
