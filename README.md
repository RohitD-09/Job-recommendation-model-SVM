# SVM-Model
This model is for a job Recommendation system that uses SVM on a dataset containing 30k records.
This model provides top 5 recommendations of Job Titles depending upon the input parameters provided to the model.

It is recommended to use chi2 test in order to provided weighted features to the model.
This version does not use weighted parameters for training the model.

The .pkl file is provided which contains a trained exported model.
The model can be loaded by using the pickle.load() method.

For additional insight on how SVM works visit this link : 
https://www.analyticsvidhya.com/blog/2021/03/beginners-guide-to-support-vector-machine-svm/

Install the following requirements on your system:

!pip install numpy

!pip install pandas

!pip install -U scikit-learn

