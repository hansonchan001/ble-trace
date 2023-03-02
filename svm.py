import pandas as pd
from sklearn import model_selection
from sklearn import svm
import random

inside = pd.DataFrame(pd.read_excel('processed_inside/03021011.xlsx')).values.tolist()
outside = pd.DataFrame(pd.read_excel('processed_outside/03021011.xlsx')).values.tolist()

y_inside = [1 for i in range(len(inside))]
y_outside = [0 for i in range(len(outside))]

Y = y_inside+ y_outside
X = inside + outside

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

# Build an SVC (Support Vector Classification) model using linear regression
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
clf_ob = svm.SVC(kernel='rbf', C=3).fit(X_train, Y_train)

print(clf_ob.score(X_test, Y_test))
scores_res = model_selection.cross_val_score(clf_ob, X, Y, cv=5)

# Print the accuracy of each fold (i.e. 5 as above we asked cv 5)
print(scores_res)

# And the mean accuracy of all 5 folds.
print(scores_res.mean())