# HemingwayOrDickens

In this project my main goal was to understand whether the sentence was belong to Ernest Hemingway or Charles Dickens.

To create train data I have used "A Tale of Two Cities", "Great Expectations" by Charles Dickens and "For Whom The Bell Tolls", "A Farewell To Arms" by Ernest Hemingway.

I have used Naive Bayes to classify the sentences. P(Hemingway|"ring") which means probality of sentence is written by Hemingway, given that it contains word "ring". After creating
frequencies table for words I used Laplace Smoothing to fix the words that have 0 frequencies.

Laplace Smoothing: P(word|writer) = (freq(word, writer)+1)/(N+V)                                                                                                  
N: Freqcuency of all words in class                                                                                                                             
V: Number of unique words in class

"A Christmas Carol" by Dickens and "Old Man And The Sea" by Hemingway were my test books.
  
Accuracy for Hemingway: 0.77                                                                                            
Accuracy for Dickens: 0.80
