class Classification():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.externals import joblib
    from sklearn import svm
    from sklearn.linear_model import LogisticRegression
    
    def __init__(self):
        pass
    
    dataDir ='../mCardiac_GUI/'
    
    def train_algorithm(self):  
        Train = self.pd.read_csv(self.dataDir+'TrainData1.csv')
        X = Train.iloc[:,:28].values
        Y = Train.iloc[:,28].values
        seed =0
        clf = self.LogisticRegression(C=6)
        #clf =self.svm.SVC(kernel='linear', C=5.0, gamma='scale')
        #clf =self.RandomForestClassifier(n_estimators=100, random_state=seed)
        model = clf.fit(X,Y)
        return self.joblib.dump(model, self.dataDir+"model.pkl")
    
    def classify(self):
        # Load model from file
        classifer=self.joblib.load(self.dataDir+"model.pkl")
        Test = self.pd.read_csv(self.dataDir+'TestData.csv')
        X_test = Test.iloc[:,1:29].values
        y_pred = classifer.predict(X_test)
        Test['Activity'] = y_pred
        Test = Test[['Activity', 'timestamp' ]]
        return Test.to_csv(self.dataDir+'ActivityData.csv')
    
    def view_activity(self):
        #spacing = 4
        dataset = self.pd.read_csv(self.dataDir+'ActivityData.csv')
        ax= self.sns.scatterplot(x='timestamp', y='Activity', hue='Activity', data=dataset, legend=False)
        ax.xaxis.set_minor_formatter(self.mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
        ax.xaxis.set_minor_locator(self.mdates.MinuteLocator())
        ax.xaxis.set_major_locator(self.plt.MaxNLocator(20))
        #for label in ax.xaxis.get_ticklabels()[::spacing]:
         #   label.set_visible(True)
        self.plt.gcf().autofmt_xdate()
        self.plt.show() 
                 
    def search_activity(self,start_date,end_date):
        dataset = self.pd.read_csv(self.dataDir+'ActivityData.csv')
        df = dataset[(dataset['timestamp'] >start_date) & (dataset['timestamp'] <= end_date)]
        ax = self.plt.axes()
        ax =self.sns.scatterplot(x='timestamp', y='Activity', hue='Activity', data=df, legend=False)
        ax.xaxis.set_minor_formatter(self.mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
        ax.xaxis.set_minor_locator(self.mdates.MinuteLocator())
        ax.xaxis.set_major_locator(self.plt.MaxNLocator(20))
        self.plt.gcf().autofmt_xdate()
        self.plt.show()
        
    