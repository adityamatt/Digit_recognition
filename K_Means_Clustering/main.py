from numpy import genfromtxt
from sklearn.cluster import KMeans
import numpy as np
import sys
from Utility import *
import matplotlib.pyplot as plt

label = "./label.txt"
data  = "./data.txt"

#Read data from csv files
X = genfromtxt(data, delimiter=',')
Y = genfromtxt(label, delimiter=',')

exp = int(sys.argv[1])

if exp==1:
    num_cluster = int(sys.argv[2])
    to_print = str(sys.argv[3])
    acc , mapping= implementing_kmeans(X,Y,num_cluster,to_print)
    print "For ",num_cluster," Clusters, Accuracy is ",acc
    print "Label in Cluster\tLabel Assigned"
    for k in mapping:
        print k,"\t\t\t",mapping[k]
    
elif exp==2:
    clusters = range(5,100,5)
    accuracy = list()

    print "Num Clusters\t\tAccuracy"
    for k in clusters:
        acc,mapping = implementing_kmeans(X,Y,k)
        print k,"\t\t\t",acc
        accuracy.append(acc)
        
    plt.plot(clusters,accuracy,color='green',marker='X')
    plt.xlabel("Number of Clusters")
    plt.ylabel("Accuracy")
    plt.show()

