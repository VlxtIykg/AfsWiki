import random
from tensorflow.keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras.models import load_model
from keras.models import Sequential
import numpy as np
import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

lemmatizer = WordNetLemmatizer()
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")


words = []
classes = []
documents = []
ignore_words = ["?", "!"]
data_file = open("intents.json").read()
intents = json.loads(data_file)


for intent in intents["intents"]:
	for pattern in intent["questions"]:

		# take each word and tokenize it
		w = nltk.word_tokenize(pattern)
		words.extend(w)
		# adding documents
		documents.append((w, intent["tag"]))

		# adding classes to our class list
		if intent["tag"] not in classes:
			classes.append(intent["tag"])


words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), "unique lemmatized words", words)


pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

training = []
output_empty = [0] * len(classes)
for doc in documents:
		# initializing bag of words
		bag = []
		# list of tokenized words for the pattern
		pattern_words = doc[0]
		# lemmatize each word - create base word, in attempt to represent related words
		pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
		# create our bag of words array with 1, if word match found in current pattern
		for w in words:
			print(w)
			bag.append(1) if w in pattern_words else bag.append(0)

		# output is a '0' for each tag and '1' for current tag (for each pattern)
		output_row = list(output_empty)
		output_row[classes.index(doc[1])] = 1

		training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)

# Separate bag-of-words representations and output labels
train_x = [item[0] for item in training]
train_y = [item[1] for item in training]

# # Convert to NumPy arrays
# train_x = np.array(train_x)
# train_y = np.array(train_y)
# print("Training data created")


# model = Sequential()
# model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation="relu"))
# model.add(Dropout(0.5))
# model.add(Dense(len(train_y[0]), activation="softmax"))
# model.summary()

# sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
# model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])


# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save("chatbot_model.h5", hist)
# print("model created")
