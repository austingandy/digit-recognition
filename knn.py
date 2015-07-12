import csv, math
training_labels = []
training_vectors = []
training_distances = [[]]
def main():
	global training_labels, training_vectors, training_distances
	with open('train.csv') as training_csv:
		training_reader = csv.reader(training_csv, delimiter=' ', quotechar='|')
		# get rid of header of csv
		next(training_reader, None)
		for row in training_reader:
			row = [int(i) for i in row[0].split(',')]
			training_labels.append(row[0])
			training_vectors.append(row[1:])
	training_distances = [[0] * len(training_vectors)] * len(training_vectors)
	for i in range(len(training_vectors)):
		for j in range(len(training_vectors)):
			training_distances[i][j] = dist(i,j,training_vectors)





def dist(i,j,vector):
	return math.sqrt(sum((p-q)**2 for p,q in zip(vector[i], vector[j])))

if __name__ == "__main__":
	main()
