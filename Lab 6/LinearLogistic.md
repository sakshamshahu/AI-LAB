# Linear and Logistic Regrassion: A summary
Let’s start by talking about Machine learning, machine learning can be defined as the subset of Artificial Intelligence and it also is a technique through which we provide the machine the ability to learn patterns about a particular problem-based analysis done by it on a given set of data. In this day and age data is termed as the king as various algorithms exist which enable us to extract valuable predictions/information from it and at the core of implementing these algorithms is Machine learning. 

Machine Learning can be classified into broadly 3 types: - 
    • Supervised Learning 
    • Unsupervised Learning 
    • Reinforcement Learning 

This summary won’t dive much into these types but as the algorithms, we are discussing belong to the category of Supervised Learning, thus we have to talk a little bit about this. Both linear and logistic regression come under the umbrella of supervised learning. In supervised learning, we provide our machine with sample data that is already labeled/categorized. So, in short, it is easier for the machine and the researcher to pinpoint the predictions they are looking for, as class labels for data points already exist. In contrast, unsupervised learning is the opposite as class labels don’t exist in the initial sample data. So, in an unambiguous way, we can say that in unsupervised learning the machine learns without any kind of supervision provided by class labels instead it finds hidden patterns on its own.

Linear and logistic regression, though both are a part of supervised learning but possess different characteristics. Supervised learning can further be categorized as:
    • Classification 
    • Regression 

Logistic regression is a classification problem despite having ‘regression’ suffixed in its name, and Linear regression is a regression type of problem. 

Logistic regression works on the basis of a sigmoid curve, which is an S-shaped curve if visualized on a graph. The range for the plot varies from 0 to 1. The values considered are reduced using a function which is:

![Formula](imgs/ff.png "Formula")

Logistic Regression is a significant machine learning algorithm because it has the ability to provide probabilities and classify new data using continuous and discrete datasets. Logistic regression predicts the probability of an occurrence and then classifies it. The classification revolves around two states. 

![Graph of logistic regression](imgs/logistic.png "Logistic Regression")

Whereas, Linear regression is a linear model, e.g., a model that assumes a linear relationship between the input variables (x) and the single output variable (y). More specifically, that y can be calculated from a linear combination of the input variables (x). When working with linear regression, our main goal is to find the best fit line which means the error between predicted values and actual values should be minimized. The best fit line will have the least error. Thus, linear regression doesn’t provide us with a definite 2-state classification, instead, it will provide me the prediction based on the best fit line. So, the response variable generated tends to be continuous.

![Linear Regression](https://github.com/Saksham-Shahu/AI-LAB/blob/e77d23d3bf51e0175931a592372fe3ec3874351a/imgs/LinearRegression.png "Linear Regression")