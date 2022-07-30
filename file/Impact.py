import csv


def main ():
    birds = import_data()
    sort_mode = input("Please enter \"1\" for bubble sort or \"2\" for selection sort: ")
    sort_by = input("Please enter \"1\" for sorting by weight or \"2\" for sorting by height: ")
    if sort_mode == "1":
        output_list = bubblesort(birds, sort_by)
    elif sort_mode == "2":
        output_list = selectionsort(birds, sort_by)
    #exportfile(output_list)
    
def import_data():
    with open('data.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        birds = list(reader)
        birds.pop(0)
        return(birds)

def bubblesort(birds, sort_by):
    
    if sort_by == "1":
        for i in range(len(birds)):
            for j in range(len(birds) - 1):
                if birds[j][2] > birds[j+1][2]:
                    birds[j], birds[j+1] = birds[j+1], birds[j]
                    
    elif sort_by == "2":
        for i in range(len(birds)):
            for j in range(len(birds) - 1):
                if birds[j][3] > birds[j+1][3]:
                    birds[j], birds[j+1] = birds[j+1], birds[j]      
    print (birds)     
    return(birds)

def selectionsort(birds, sort_by):
    
    if sort_by == "1":
        for i in range(len(birds)):
            min_idx = i
            for j in range(i+1, len(birds)):
                if birds[min_idx][2] > birds[j][2]:
                    min_idx = j
            birds[i], birds[min_idx] = birds[min_idx], birds[i]
    
    elif sort_by == "2":
        for i in range(len(birds)):
            min_idx = i
            for j in range(i+1, len(birds)):
                if birds[min_idx][3] > birds[j][3]:
                    min_idx = j
            birds[i], birds[min_idx] = birds[min_idx], birds[i]
    print (birds) 
    return(birds)
    
"""
def exportfile(output_list):
    fields = ["Species","Gender","Weight(kg)","Height(cm)","Location"]
    rows = output_list
    with open("output_file.csv", "w", newline="") as out_file:
        write = csv.writer(out_file)
        write.writerow(fields)
        write.writerows(rows)
    
            """
main()