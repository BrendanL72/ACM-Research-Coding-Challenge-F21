# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Sources used for development/code:
"How to Get Started with Deep Learning for Natural Language Processing"

https://machinelearningmastery.com/crash-course-deep-learning-natural-language-processing/

"Bag of Words Model for Beginners"

https://www.kaggle.com/vipulgandhi/bag-of-words-model-for-beginners

Load Text

https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/load_data/text.ipynb

   Used this to gain a better understanding of how tensorflow works.

imdb reviews

https://www.tensorflow.org/datasets/catalog/imdb_reviews

   Chosen due to reviewer's greater vocabulary, which I feel gives the AI a better chance of analyzing these blocks of text
   Dataset split into training and test
   Training data contains 12.5k positive and negative reviews, as well as 50k unsupervised data. The unsupervised data will not be used.

Recurrent Neural Network Text Tutorial

https://www.tensorflow.org/text/tutorials/text_classification_rnn
   This tutorial happened to feature the dataset (imdb reviews) I wanted to use.
   As such this is the primary basis for my code.

Rotten Tomatoes Reviews

https://nlp.stanford.edu/sentiment/code.html

   This dataset uses a scale of 1-25, however it was made with CoreNLP in mind, which uses Java.
