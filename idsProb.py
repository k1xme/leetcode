import random

ids = [1,2,3,4,5,6,7,8,9,10]
probabilities = [0.1, 0.1, 0.1, 0.2, 0.05, 0.05, 0.05, 0.1, 0.15, 0.1]

print sum(probabilities)

def choose_id(ids, probabilities):
	point = random.random(0, 1)