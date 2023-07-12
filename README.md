# Concrete Compressive Strength Prediction


## Problem Statement
The quality of concrete is determined by its compressive strength, which is measured using a conventional crushing test on a concrete cylinder. The strength of the concrete is also a vital aspect in achieving the requisite longevity. It will take 28 days to test strength, which is a long period.
Solved this problem using Data science and Machine learning technology, developed a web application which predicts the "Concrete compressive strength" based on the quantities of raw material, given as an input. Sounds like this saves a lot of time and effort right !

`Data source:-` https://www.kaggle.com/elikplim/concrete-compressive-strength-data-set

## Approach Used:
1. Loading the dataset using Pandas and performed checking the data type and any missing values.
2. Exploratory data analysis was carried out:
    - Observed the distribution of the target feature, "Concrete compressive strength," which was normal with very little right skewness, as part of exploratory data analysis.
    - When comparing each predictor or independent feature to the target feature, it was discovered that cement and the target feature have a direct proportionality, whereas water and the target feature have an inverse proportionality.
    - Plotted both Pearson and Spearman correlations to gain even more valuable insights, which revealed the same outcomes as above.
    - The column 'age' has the most outliers, according to a check of all the columns for the presence of outliers. By considering adding and excluding the lower and higher limits into two independent dataframes and merging both into one, I was able to remove outliers using the IQR technique. This has boosted the amount of data available, allowing for effective machine learning model training. 

3. Experimenting with various ML algorithms:
    - First, tried with Linear regression models and feature selection using Backward elimination, RFE and the LassoCV approaches. Stored the important features found by each model into "relevant_features_by_models.csv" file into the "results" directory. Performance metrics are calculated for all the three approaches and recorded in the "Performance of algorithms.csv" file in the "results" directory. Even though all the three approaches delivered similar performance, I chose RFE approach, as the test RMSE score is little bit lesser compared to other approaches. Then, performed a residual analysis and the model satisfied all the assumptions of linear regression. But the disadvantage is, model showed slight underfitting.
    - Next, tried with various tree based models, performed hyper parameter tuning using the Randomized SearchCV and found the best hyperparameters for each model. Then, picked the top most features as per the feature importance by an each model, recorded that info into a "relevant_features_by_models.csv" file into the "results" directory. Built models, evaluated on both the training and testing data and recorded the performance metrics in the "Performance of algorithms.csv" file in the "results" directory.
    - Based on the performance metrics of both the linear and the tree based models, XGBoost regressor performed the best, followed by the random forest regressor. Saved these two models into the "models" directory.
4. Deployment:
    Deployed the XGBoost regressor model on Streamlit Community Cloud and used Streamlit for UI.

At each step in both development and deployment parts, logging operation is performed which are stored in the development_logs.log and deployment_logs.log files respectively. 

As a result, we can now immediately determine the compressive strength of concrete by simply providing the web application with the raw material quantities. 
