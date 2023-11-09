### Part 1: Plain Aggregates and Privacy
#### Question 1
Kinan is a PhD student and has obtained a master's degree, so he is very likely be over 25. Among those who are over 25, they chose Country (25), Rock (25, 26), Pop (26), and Metal (29, 30). Therefore, those 4 are likely to be Kinan's musical tastes. 

#### Question 2
In Kinan's twitter, I found a post of his top artists of the year. All of them are metal bands, which is one of our findings in question one. He also includes " Heavy Metal and Beer" in his Twitter bio. Therefore, I could narrow Kinan's age to 29 or 30 since only those two ages above 25 have people who like metal. In facebook, I found his birth year to be 1994, so he could be either 28 or 29. Combined with his music taste, his exact age should be 29.

#### Question 3
Kinan is 29 years old, and there are only 2 answers from age 29: Black and Yellow. It is obvious to narrow the answer to those 2 colors. However, I could not infer the exact color he likes. I could only speculate that he likes black best because he likes metal music. 

#### Question 4
I could know that his favourite sport should be either Baseball, Basketball, E-Sports, or Soccer since those are the answers from age group 25 or more. 

#### Question 5
Since Kinan is 29, last year he was still above 25, so his answer should also be in the age group of 25 or more. Comparing last year's answers with this year's, only Soccer exists in both years. Therefore, Kinan's favourite sport should be Soccer.

### Part 2: Implementing Differential Privacy
#### Question 6
When the privacy parameter grows larger, the noised value is closer to the original value, so the data is more useful but with less privacy. When the privacy parameter grows smaller, the noised value is less useful but with more privacy.

#### Question 7
The most likely value is 1. The average value is 0.98. It is similar to the actual value 1. When privacy parameter is smaller, the plot will become smaller, with each value have closer frequencies. When the privacy parameter becomes larger, the plot will also become larger, with each value have more diverse frequencies. 

### Part 3: Differential Privacy and Composition
#### Question 8
Kinan is very likely to have coding experience with more than 10 years. 
However, I am not confident with my deduction. 
Though his age is 29 and is close to the average age of the group with more than 10 years of coding experience, we don't know the number of people in each group. If there are many young people (freshman, sophomores), Kinan can definitely lie in other groups where the average age is only around 22 years old. 

#### Question 9
Kinan is 29 years old. He likes metal music most. He has more than 10 years of coding experience. 

#### Question 10
No, it doesn't because developers can intentionally or unintentionally over-use the dataset.
1. Intentionally: the developers can add set method in the class to expose the private attribute budget so that they could intentionally modify the budgets.
2. Unintentionally: when the class is used in multi-thread environment, the check_and_update_budget() method might be violated. Certain locking techniques must be applied to make sure this method is atomic. 