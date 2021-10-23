# rocheTask
Task for Junior DataScientist @' Iris Classification

TASK # 1:

Iris Flower Classification:
There are many appraoches that can be applied to classify the Iris flower dataset such as using a classifier like decision trees. 
For this task I will have choosen Decision Trees as the classifier  as iris dataset classification problem is  
1. Supervised Learning problem ( the target labels are given) 
2. Balanced (meaning 50 records from each class so there is no class imblabance), 
3. Complete ( there are no values that are missing) 
 
Methodology
1. Load Iris dataset 
2. Segregate the data and the labels 
3. Divide data into train and test, I choose to have a test set of 33% adn a train of 77%.
   The train to test ratio has effect the accuracy in good and bad ways. The Good way is when the train test ratio let our classifier acchive higher generalization. The bad efect is overfitting when the classifier instead of learning the class concepts memorizes the patterns that belong to the class. 
4. The Performance of the classifier is evaluated usng 
	1. Accuracy and 
	2. Confusion matrix




TASK # 2:

Natral Language Processing Task:
The objective is to use a classifier to segregate the data into sarcastic and non-sarcastic headlines. It is a supervised problem as we know the target label but unlike IRIS flower dataset the data here is textual and not numbers. This makes the pre-processing more chanllenging as we need to use some library like the ntlk text classification which I have used for stop words only.
This solution is needs more refine feature extraction for a faster performance.

Methodology
1. Load the JSON file
2. Splitting into Train and Test
3. Filtering the Corpus of Text based on removing the words
4. Calculating features for each Token
5. training the Naive Bayes Classifier


This solution has a number of issues that can be improved
1. The feature extraction process can be optimized to have some feature reduction like a PCA and further represent the feature in a Bit Vector for faster access
2. The choice of classifier can be a neural network with back propagation that once trained may be incrementally up trained.




TASK # 3:

SELECT student_id, name, surname, birth_date, faculty 
FROM student
WHERE student_id IN ( 
		SELECT student_id 
		FROM exam_results
		WHERE grade>4)
 
		
