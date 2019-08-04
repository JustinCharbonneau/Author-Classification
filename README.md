# Author-Classification

## Introduction

This is the repo for my Author classification project. The data used in this task is provided by the glutenberg repository.

1. [Environment Setup](#environment-setup)
2. [Run Application](#run-application)


## Environment Setup

This project already contains trained models for classifying authors from 5 different texts/authors. To run the application, it is assumed you have already installed Python 3. 

If not, depending if you are using a mac or not, I suggest downloading Anaconda.

You can also download directly from the Python website here: https://www.python.org/downloads/

## Run Application

Download the code.

In the terminal navigate to the project folder and run:

```
$ python3 app.py
```

Enter the text you want to classify.

```
Enter your sentence: I, if I be aliue, and your minde hold, and your\nDinner worth the eating\n\n   Cassi.
```

Next, the application will clean the input by tokenizing the text, removing stopwords, lemmatizing them and then vectorizing them using a the fitted TF-IDF and Count vectorizers. 

Now, you can choose between four different classification algorithms by entering the abbreviation of the algorithm. This will upload the pickle file containing the serialized model.

- Decision Tree (DT)
- K-Nearest Neighbor (KNN)
- Support Vector Machine (SVM)
- Multi Layer Perceptron (MLP)

```
Please enter a model (MLP, DT, SVM, KNN): MLP
```

```
The author is: shakespeare
```

Voilà!
