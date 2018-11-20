from sklearn.cluster import KMeans
import numpy as np

def implementing_kmeans(X,Y,class_num,to_print="FALSE"):
    #N -> number of instances = 5000
    #D -> dimenstion of each instance =400
    #k -> Actual Number of Clusters = 10 digits

    n,d = X.shape
    k = Y.shape[1]

    #Y dash is a new Column matrix that will have labels
    Ydash= list()
    for i in range(len(Y)):
        for j in range(10):
            if Y[i][j]==1:
                class_label = j
                break;
        Ydash.append([class_label])

    Y=np.asarray(Ydash)

    #Kmeans Implementaion using sklearn
    kmeans = KMeans(n_clusters=class_num) 
    kmeans.fit(X)

    #Matrix to find the maximum frequency actual label to given label
    #Because kmeans assigned some random label to a cluster in range 0 to class_num-1
    class_label = np.zeros((class_num,k))

    for i in range(n):
        given_class = kmeans.labels_[i]
        actual_class = Y[i]
        #Increasing ++
        class_label[given_class][actual_class]+=1
        

    #To store the matching of given label to actual label    
    matching = dict()

    #Filling in matching
    for i in range(class_num):
        #Finding maximum frequency actual label for given label
        max_class = class_label[i][0]
        label = 0
        for j in range(1,k):
            if class_label[i][j]>max_class:
                max_class = class_label[i][j]
                label = j
        #Filling in the matching
        matching[i]=label
    #For accuract ,correctly Identified
    correct =0
    for j in range(n):
        if to_print=="TRUE":
            print "Actual Label = ",Y[j][0]+1,"\t\tGiven Label = ",matching[kmeans.labels_[j]]+1
        if Y[j][0]==matching[kmeans.labels_[j]]:
            correct=correct+1

    acc = float(correct)/n
    return acc,matching
        
