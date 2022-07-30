import csv

def main ():
    birds = import_data()
    selectionsort(birds)

def import_data():
    with open('file/data.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        birds = list(reader)
        birds.pop(0)
        return(birds)

def selectionsort(birds):
        for i in range(len(birds)):
            min_idx = i
            for j in range(i+1, len(birds)):
                if birds[min_idx] > birds[j]:
                    min_idx = j
            birds[i], birds[min_idx] = birds[min_idx], birds[i]
        #print (birds) 
        return(birds)


main()