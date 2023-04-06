## Cherry Leaves Mildew Detection 

### User Stories

Epic - Data Collection
* Download image datasets from Kaggle and ensure they are properly labelled.
* * User Story - Data Collection: As a Developer I can access the dataset I need from Kaggle so that I can use it for analysis and ML.

Epic - Data Cleaning and Preparation
* Prepare Dataset for ML by removing non image files, splitting into train, validation and set folders and augmenting the data.
* * User Story - Data Cleaning: As a Developer I can remove non-image files so that the data is cleaned for ML.
* * User Story - Split Datasets: As a Developer I can divide the datasets so that I can train and evaluate a model's performance.

Epic - Data Visualisation
* Calculate the mean and standard deviation of the images. Display an image montage to the dashboard.
* * User Story - Average Image and Variability: As a Developer I can display the variations in the image dataset so that I can see the differences between images belonging to the two classes.
* * User Story - Image Montage: As a Client/Developer I can see an image montage so that I can view a number of images belonging to a given label.

Epic - Model Training, Optimization and Validation 
* Train the model using the data in the training set and use the validation set for optimum accuracy of the prediction.
* * User Story - As a Developer I can use the training dataset so that I can train a model to accurately predict the class of an image dataset.
* * User Story - Hyperparameter Optimisation: As a Developer I can adjust hyperparameters so that the model's prediction accuracy increases and meets the business requirements.

Epic - Dashboard Planning, Designing and Development
* Create interactive pages for the summary, visualisation, detector, performance and hypothesis.
* * User Story: Summary Page: As a Client I can view the summary page on the dashboard so that I'm given an overview of the project with the business requirements.
* * User Story: Data Visualisation Page: As a Client I can view the data visualisation page so that I can see all of the image visualisation and dimension plots.
* * User Story: Powder Mildew Detector: As a Client I can upload cherry leaf images so that I can get the prediction results classifying the cherry leaf as healthy, or containing powdery mildew.
* * User Story: Hypothesis Page: As a Client I can view the hypothesis page so that I can see what the project hypotheses are and whether they were validated.
* * User Story: Performance Metrics Page: As a Client I can view the performance metrics so that I can view how well the model fits the data and how well it can be used to analyse unseen data.

Epic - Dashboard Deployment and Release 
* Deploy the app using Heroku and present the live link on the README.
* * User Story: Deployment: As a Developer/Client I can view the app on a cloud platform so that the app is easily accessed.
