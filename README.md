# Hermon Asmelash

## Cherry Leaves Mildew Detection

Farmy & Foods' prize product - their cherry planntation - has a growing powdery mildew problem. The symptoms of powdery mildew in cherry leaves typically begin as small, circular, white spots on the upper surfaces of leaves. As the disease progresses, the spots may coalesce and form a powdery white or grayish film that covers the entire leaf surface. Infected leaves may also become distorted, curl, and eventually fall off the tree. 

The process of visually detecting this fungul infection and applying compounds to kill it is time consuming and untenable, especially as the business continues to grow. This project aims to create a dashboard app that plots differences between healthy and mildew-containing cherry leaves as well as develop a ML model that can predict whether a given image is a healthy cherry leaf or contains powdery mildew. 

[Link to the deployed application.](https://cherry-leaves-mildew-detection.herokuapp.com/)

## Table of Contents

[Planning](#planning)
- [Business Requirements](#business-requirements)
- [Hypothesis](#hypothesis-and-how-to-validate)
- [Map Business Requirements](#map-business-requirements)
- [ML Business Case](#ml-business-case)
- [User Stories](#user-stories)
- [Dashboard Design](#dashboard-design)

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

How to validate? - By training and validating a model using a Convolutional Neural Network (CNN) until it reaches that accuracy. Plotting accuracy and loss plots to ensure there is no underfitting (the model failing to learn) or overfitting (the model fails to predict on unseen data). Finally, the test set will be evaluated using the saved model. 

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
* * Probability text, probability graph and analysis report when image is uploaded

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

## Testing

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Technologies Used
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements 
* Thank the people that provided support throughout this project.
