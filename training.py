print('Model Training Process')

from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier

log_clf = LogisticRegression()

adb_clf = AdaBoostClassifier()
