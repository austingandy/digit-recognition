import csv
training_labels = []
training_vectors = []
def main():
	global training_labels, training_vectors
	with open('train.csv') as training_csv:
		training_reader = csv.reader(training_csv, delimiter=' ', quotechar='|')
		next(training_reader, None)
		for row in training_reader:
			row = [int(i) for i in row[0].split(',')]
			training_labels.append(row[0])
			training_vectors.append(row[1:])
	print training_labels



if __name__ == "__main__":
	main()
