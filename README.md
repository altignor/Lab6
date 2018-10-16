# Lab6
Tignor and Filiault
Lab 6
40 points
Due: Before Next Lab
Problem:
You need to refactor the mobile phone cost application so that it has proper error checking.
Purpose:
This lab gives you practice with: * Designing and programming functions * Re-using many of the other aspects of Python we've learned so far * Testing code * Using loops for error checking
Details:
You need to refactor some example code from Lab 4 so that the following is true: * It is now organized in functions * If the user enters an invalid package name they are prompted again, and this continues until they give a valid package * If the user enters a negative number of GB used, they are asked again, and this continues until they give a valid value * You may assume that the GB used is a float, and the cost is prorated (i.e., if I go over my limit by 0.5GB, I am charged 50% of the cost of an extra GB).
Steps:
We are going to practice "iterative development": focusing on one aspect of the problem first, then once that works, focusing on the rest of it.
Understand the problem
Look over the Lab6 version of the Lab4 code in your repository.
Determine the functions that might make sense in the code. Take at most 10 minutes planning.
Re-arrange the code into functions without adding the new error checking.
Test that your code still works using the test cases you developed for Lab 4.
Design your error checking functions. Put these designs in algorithm.txt.
Write your code for the new error checking functions following your algorithm and using good usability principles. Incorporate them into your previously working code.
Properly comment your code with intro comments, function comments, and line comments
Write a set of testcases in testcases.xlsx to test your new functionality (your error checking). Your test cases from Lab 4 should be sufficient for testing in general, so focus on the new ones.
Extra Credit:
If you have a fully working program, you may do the extra credit. Create a copy of your program in Lab6EC.py. Modify the program so that after it runs the user is asked if they want to run again. If they enter "yes" they can go through all of the original steps all over again. The user should be able to repeat these steps as many times as they'd like.
Submit:
To GitHub: 
Your Python file (Lab6.py)
Your algorithm (algorithm.txt)
Your extra credit Python file, if attempted (Lab6EC.py)
On Moodle:
Reflection (1 per partner): Discuss what you learned in lab, what it was like working with your partner, and what it was like refactoring code like the code you wrote a few weeks ago? (.pdf, .docx, or .txt)
Your test cases based on your flowchart (testcases.xlsx, 1 per pair)
