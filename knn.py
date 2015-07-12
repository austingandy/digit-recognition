import csv, math, sys
training_labels = []
training_vectors = []
learning_labels = []
learning_vectors = []
header = []
#training_distances = [[]]
def main():
	train()
	learn()
	write()

def train():
	global training_labels, training_vectors
	with open('train.csv') as training_csv:
		training_reader = csv.reader(training_csv, delimiter=' ', quotechar='|')
		# get rid of header of csv
		next(training_reader, None)
		for row in training_reader:
			row = [int(i) for i in row[0].split(',')]
			training_labels.append(row[0])
			training_vectors.append(row[1:])
	print "Done training!"

def learn():
	global training_labels, training_vectors, learning_labels, learning_vectors, header
	with open('test.csv') as test_csv:
		learning_reader = csv.reader(test_csv, delimiter=' ', quotechar='|')
		next(learning_reader, None)
		i = 0
		for row in learning_reader:
			row = [int(i) for i in row[0].split(',')]
			min_dist = sys.maxint
			closest_num = -1
			for count, (vec, num) in enumerate(zip(training_vectors, training_labels)):
				if count % 100 == 0:
					print "Working on training vector number " + str(count) + "for learning reader " + str(i)
				d = dist(row, vec)
				if min_dist > d:
					min_dist = d
					closest_num = num
			learning_labels[i] = closest_num
			i += 1
	print "Done learning!"

def write():
	global training_labels, header
	with open('answers.csv', 'w', newline='') as csvfile:
		answer_writer = csvfile
		answer_writer.writerow(header)
		for label in training_labels:
			answer_writer.writerow(list(str(label)))

def dist(vector_one,vector_two):
	return math.sqrt(sum((p-q)**2 for p,q in zip(vector_one, vector_two)))

if __name__ == "__main__":
	main()
