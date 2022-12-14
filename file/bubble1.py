import csv
#import matplotlib.pyplot as plt

def main ():
    birds = [1.61, 1.644, 1.67, 1.679, 1.809, 1.824, 1.905, 1.951, 1.959, 1.971, 2.009, 2.026, 2.044, 2.049, 2.054, 2.057, 2.085, 2.102, 2.125, 2.135, 2.141, 2.159, 2.168, 
2.172, 2.204, 2.206, 2.21, 2.213, 2.246, 2.253, 2.256, 2.258, 2.289, 2.289, 2.297, 2.299, 2.302, 2.322, 2.33, 2.331, 2.367, 2.371, 2.377, 2.387, 2.389, 2.393, 2.398, 2.411, 2.414, 2.418, 2.432, 2.454, 2.455, 2.457, 2.461, 2.462, 2.47, 2.48, 2.5, 2.505, 2.506, 2.542, 2.549, 2.563, 2.572, 2.586, 2.612, 2.612, 2.633, 2.643, 2.662, 2.675, 2.686, 2.691, 2.7, 2.713, 2.739, 2.745, 2.758, 2.787, 2.794, 2.799, 2.817, 2.834, 2.835, 2.848, 2.853, 2.89, 2.894, 2.896, 2.908, 2.914, 2.927, 2.929, 2.933, 2.994, 3.017, 3.033, 3.101, 3.101, 3.116, 3.138, 3.142, 3.167, 3.222, 3.26, 3.27, 3.294, 3.313, 3.397, 3.436, 3.445, 3.453, 3.471, 3.668, 3.719, 
3.822]
    bubblesort(birds)
    
def import_data():
    with open('data.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        birds = list(reader)
        birds.pop(0)
        return(birds)

def bubblesort(birds):
        for i in range(len(birds)):
            min_idx = i
            for j in range(i+1, len(birds)):
                if birds[min_idx] > birds[j]:
                    min_idx = j
                birds[i], birds[min_idx] = birds[min_idx], birds[i]
                
        print (birds) 
        #plt.plot([1.61, 1.644, 1.67, 1.679, 1.809, 1.824, 1.905, 1.951, 1.959, 1.971, 2.009, 2.026, 2.044, 2.049, 2.054, 2.057, 2.085, 2.102, 2.125, 2.135, 2.141, 2.159, 2.168, 
#2.172, 2.204, 2.206, 2.21, 2.213, 2.246, 2.253, 2.256, 2.258, 2.289, 2.289, 2.297, 2.299, 2.302, 2.322, 2.33, 2.331, 2.367, 2.371, 2.377, 2.387, 2.389, 2.393, 2.398, 2.411, 2.414, 2.418, 2.432, 2.454, 2.455, 2.457, 2.461, 2.462, 2.47, 2.48, 2.5, 2.505, 2.506, 2.542, 2.549, 2.563, 2.572, 2.586, 2.612, 2.612, 2.633, 2.643, 2.662, 2.675, 2.686, 2.691, 2.7, 2.713, 2.739, 2.745, 2.758, 2.787, 2.794, 2.799, 2.817, 2.834, 2.835, 2.848, 2.853, 2.89, 2.894, 2.896, 2.908, 2.914, 2.927, 2.929, 2.933, 2.994, 3.017, 3.033, 3.101, 3.101, 3.116, 3.138, 3.142, 3.167, 3.222, 3.26, 3.27, 3.294, 3.313, 3.397, 3.436, 3.445, 3.453, 3.471, 3.668, 3.719, 
#3.822])
        #plt.ylabel('some numbers')
        #plt.show()
        return(birds)

main()