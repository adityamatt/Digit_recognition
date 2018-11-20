Name : Aditya Tiwari
Entry: 2016csb1029
###########################
K-Means Clustering

    Library Used: sklearn
    To install in Ubuntu 16.04 using pip ,Enter in terminal : pip install sklearn
    
    I have created two experiments
    
    To run first experiment:
        
        python main.py 1 <NUMBER OF CLUSTERS> <TO_PRINT>
        e.g 
            main.py 1 10 FALSE
        
        where:
              <NUMBER OF CLUSTERS> is the number of clusters
              <TO_PRINT> is a BOOLEAN VALUE TRUE/FALSE whether to print the assigned label and actual label for each instance
              Note Setting <TO_PRINT> to TRUE would print 5000 lines of assigned and actual label for each instance

    Output is Accuracy and The mapping between random label given by k means and actual assigned label where actual assigned label is the max frequency label in that random label.
    See Report for more information
    
    To run Second experiment:
        
        python main.py 2
        
        This would run the k-means for varying number of clusters in k=5 to 100.
        (You may Change this in Line 27 of main.py if you wish to)
        
        This would print the accuracy for each varying cluster and show a graph as well
