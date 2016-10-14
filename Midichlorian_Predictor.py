'''
Predicts midi cholrian counts based on data from Star Wars EU (https://www.quora.com/What-is-Luke-Skywalkers-midichlorian-count-How-does-his-count-compare-to-other-Jedis)
Author: Rohan Koodli
'''


anakin = 27000
palpatine = 19000
yoda = 17000
luke = 15000
leia = 15000
kylo = 13500
dooku = 13500
kenobi = 13400
maul = 12000

from sklearn import tree

# real data # will update when Rey's MC count is known
X = [[anakin], [leia], [anakin]]
Y = [leia, kylo, luke]

#decision tree
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, Y)
print clf.predict([[16000]]) # input your midichlorian count here!

#computing accuracy
from sklearn import cross_validation
print ('Accuracy',cross_validation.cross_val_score(clf,X,Y))
