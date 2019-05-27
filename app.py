from functions.Functions import *
import pandas as pd
from sklearn.externals import joblib

def main():
    user_input = input("Enter your sentence : ")

    clean_input = [' '.join(stem_lem_words(tokenize(user_input)))]
    print('Pre-processing ...')
    # Load vectorizer
    c_vectorizer = joblib.load('vectorizers/count_vectorizer.pkl')
    tfidf_vectorizer = joblib.load('vectorizers/tfidf_vectorizer.pkl')

    texts_count_vectorized = pd.DataFrame(c_vectorizer.transform(clean_input).toarray())
    texts_tfidf_vectorized = pd.DataFrame(tfidf_vectorizer.transform(clean_input).toarray())

    # combine both
    df = pd.concat([texts_count_vectorized, texts_tfidf_vectorized], axis=1)
    print('Done')

    model_selection = input("Please enter a model: (MLP, DT, SVM, KNN) ")

    while model_selection != 'MLP':
        print('Sorry that model isn\'t ready yet')
        model_selection = input("Please choose an available model: (MLP) ")

    # Load MLP model
    if model_selection == 'MLP':
        mlp_model = joblib.load('models/mlp_model.pkl')
        results = mlp_model.predict(df)
        print('The author is:', results[0])
    

if __name__ == '__main__':
    main()
