'''
Predicts midi chlorian counts based on data from Star Wars EU (https://www.quora.com/What-is-Luke-Skywalkers-midichlorian-count-How-does-his-count-compare-to-other-Jedis)
Opposite of Midichlorian_Predictor
Predicts parentage given child's midichlorian count
@author: Rohan Koodli
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

rey = 13000 # a (wild) guess

from sklearn import tree, svm
import random

noiseX, noiseY = [],[]
for i in range(2): # data augmentation
    multiplier = random.uniform(500,3000) # multiplied by number between -1 and 1
    r1 = random.uniform(-1, 1)
    k_noise = kylo + r1 * multiplier
    r2 = random.uniform(-1,1)
    l_noise = leia + r2 * multiplier
    r3 = random.uniform(-1,1)
    a_noise = anakin + r3 * multiplier

    noiseX.append([k_noise])
    noiseY.append(l_noise)
    noiseX.append([l_noise])
    noiseY.append(a_noise)


X = [[leia], [kylo]] + noiseX
Y = [anakin, leia] + noiseY

print X
print Y

clf = svm.SVR()
clf = clf.fit(X, Y)
print clf.predict([[rey]]) # input your midichlorian count here!


#computing accuracy
from sklearn import cross_validation
print ('Accuracy',cross_validation.cross_val_score(clf,X,Y))
