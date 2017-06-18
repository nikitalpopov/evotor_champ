import time
import pandas
from sklearn.externals import joblib

from products.text_edit import *

csv_train_input_file = r"evo_train.csv"
csv_test_input_file = r"evo_test.csv"
csv_train_file = r"train_file.csv"
csv_test_file = r"test_file.csv"

print('Cleaning training text...')
train = clean_text(csv_train_input_file)
print(train)
print('')

print('Tokenization training file...')
start = time.clock()
tokenization(train, csv_train_file)
stop = time.clock()
print('Time of tokenization: ', stop - start, ' s')
train = read_csv(csv_train_file, encoding='utf-8')
# print(train)
print('')

print('Vectorizing training text...')
from sklearn.feature_extraction.text import HashingVectorizer
coder = HashingVectorizer()
start = time.clock()
trn = coder.fit_transform(train.NAME.values.astype('U'))
stop = time.clock()
print('Time of vectorization: ', stop - start, ' s')
print('')

print('Creating model...')
from sklearn.svm import LinearSVC
start = time.clock()
clf = LinearSVC().fit(trn, train.GROUP_ID)
stop = time.clock()
joblib.dump(clf, 'model.pkl')
print('Time of model creation: ', stop - start, ' s')
print('')

print('Cleaning testing text...')
test = clean_text(csv_test_input_file)
print('')

print('Tokenization testing file...')
start = time.clock()
tokenization_test(test, csv_test_file)
stop = time.clock()
print('Time of tokenization: ', stop - start, ' s')
test = read_csv(csv_test_file, encoding='utf-8')
# print(test)
print('')

print('Vectorizing testing text...')
start = time.clock()
tst = coder.transform(test.NAME.values.astype('U'))
stop = time.clock()
print('Time of vectorization: ', stop - start, ' s')
print('')

print('Predicting rubric for each test news...')
clf = joblib.load('model.pkl')
result = clf.predict(tst)
print('')
predicted = pandas.Series(result)
test['GROUP_ID'] = predicted.values
print(test)

print('Outputting result...')
test.drop('NAME', axis=1, inplace=True)
test.to_csv('result.csv', sep=',', encoding='utf-8', index=False)
print("That's all!")
