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

## How to Run
Click on the link to the Google Colab to run the Jupyter Notebook. Google Colab lets you run the machine learning Tensorflow library on its GPUs. 
You can run each step individually (as most of it is non-essential) by clicking the play button on the left or run all the steps by clicking Runtime > Run all.
Keep in mind that the program takes quite a while to load the dataset as well as learn from it.
It will ask you for an input text file after the model is done loading, download the input.txt file from the GitHub repo.

## Development Story/Context
I didn't know anything about Natural Language Processing or Sentiment Analysis before this project, so I looked up how to approach it. 
There were two options available to me: create the rules of what constitutes positive and negative speech, which is time consuming at best and a black hole of time at worst,
or use machine learning libraries to learn what is positive and negative speech. I chose the second approach as a learning opportunity.

I chose the Tensorflow machine learning library because it had extensive amounts of tutorials/documentation and used Python. However Tensorflow only works on PCs with NVidia GPUs because they have CUDA architecture.
To compensate, I used Google Colab + Jupyter since it could run Tensorflow for free and could run step by step for easier learning.

I started with a tutorial that I planned on adapting to fit my chosen dataset: IMDB_reviews. I chose this dataset because of the extended vocabulary of the input text given, so I figured that a movie review website would exhibit higher level vocabulary than the other review/social media based datasets. 
Luckily I found a tutorial on the Tensorflow website that did exactly what I was trying to do whilst going through their documentation from the previous tutorial. Most of the code in this project comes from this tutorial, however I tried to explore, take notes, nd read documentation wherever I could.

## Approach
The machine learning algorithm is structured into 5 major parts to predict the text: 
*  Setup
   *  Involves importing the necessary libraries and loading the data into a Tensorflow dataset object 
*  Encoding the Text
   *  Involves transforming the large quantities of text into numerical vectors that goes through several layers to create a model
*  Training/Validating the Model
   *  Takes the processed dataset and tries to use the model to predict sentiment. If it guesses wrong, then the model is adjusted.
*  Testing the Model
   *  Tests the quality of the model using a completely new dataset to avoid the model getting too used to the training set.
*  Predicting New Text
   *  Insert the desired text to be read and given a Sentiment Analysis rating based on what the model has learned

## Sources used for development/code:
These sources were used in my development.

[Load Text](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/load_data/text.ipynb)
   Started off the project using this tutorial and used it to gain a better understanding of how tensorflow works.

[IMDB reviews](https://www.tensorflow.org/datasets/catalog/imdb_reviews)
   Chosen due to reviewer's greater vocabulary, which I feel gives the AI a better chance of analyzing these blocks of text.
   The dataset is split into training and test folders.
   Training data contains 12.5k positive and negative reviews each, as well as 50k unsupervised data. The unsupervised data is not used.
   Testing data contains 12.5k positive and negative reviews each.

[Recurrent Neural Network Text Tutorial](https://www.tensorflow.org/text/tutorials/text_classification_rnn)
   This tutorial happened to feature the dataset (imdb reviews) I wanted to use.
   As such this is the primary basis for my code.

Honorable Mention:

[Rotten Tomatoes Reviews](https://nlp.stanford.edu/sentiment/code.html)
   This dataset uses a scale of 1-25, however it was made with CoreNLP in mind, which uses Java.
