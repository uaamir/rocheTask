# rocheTask
task for Junior DataScientist @ Roche
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




TASK # 4:

SELECT student_id, name, surname, birth_date, faculty 
FROM student
WHERE studen_id IN ( 
		SELECT student_id 
		FROM exam_results
		WHERE grade>4)
 
		
