# Machine Learning Project : Iris-flower-classification
This program applies basic machine learning (classification) concepts on *Iris Data* to predict the species of a new sample of Iris flower.

**Introduction**  
The dataset for this project is taken from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Iris). The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.
- The data set consists of 50 samples from each of three species of Iris ('Setosa', 'Virginica' and 'Versicolor').
- Four features were measured from each sample (in centimetres): 
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width

**Working of the decision_tree_classifier**
- The program takes data from the `iris.csv` file loaded on the system.
- The program then creates a decision tree based on the dataset for classification.
- The user is then asked to enter the four parameters of his sample and prediction about the species of the flower is printed to the user.

**Working of the self_made_KNN**
- The program takes data from the `iris.csv` file loaded on the system.
- The program splits the dataset into two subsets: *Training Data* and *Testing Data* by `80:20` ratio using `train_test_split` function in `sklearn` module.
- The program calculates the accuracy for the classifier using `accuracy_score` function in `sklearn.metrics` module by predicting *Test Data* and matching the calculated result with the actual result.
- The classifier is based on the `KNearestNeighbor` classifier in `sklearn` module, which finds the closest data point of the given sample and assign the species of that point to the sample. 
