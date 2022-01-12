from sklearn.feature_extraction.text import CountVectorizer #import class to find the frquency of words, 
from sklearn.metrics.pairwise import cosine_similarity #cosine-similary is a directly a method. No need to initialize the object.

text = ["London Paris London","Paris Paris London"]
 #initialize an object because CounVectorizer is a class 

count_matrix = cv.fit_transform(text) #method to count the number of words
#print(count_matrix)

print (count_matrix.toarray()) #Matrix represenatation of the frquency of the word London, Paris

similarity_scores = cosine_similarity(count_matrix)

print (similarity_scores)
#[1. 0.8] 
#First sentence is similar to the first one by 100%
#First senetence is similar to the second one by 80%