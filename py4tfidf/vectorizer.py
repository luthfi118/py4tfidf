import numpy as np
class tfidf:
    def __init__(self):
        pass
    def __diction(self,x):
        diction=set()
        for i in range(len(x)):
            temp=set(x[i])
            diction.update(temp)
        diction=list(diction)
        diction.sort()
        self.__dictionary=diction
        return diction
    def __get_df(self,x,diction):
        df=np.zeros(len(diction))
        for i in range(len(x)):
            for j in range(len(diction)):
                for word in set(x[i]):
                    if word in diction[j]:
                        df[j]=df[j]+1
        return df
    def __get_idf(self,x,df):
        idf=np.log10(len(x)/df)
        self.__idf=idf
        return idf
    def __get_tf(self,x,diction):
        tf=np.zeros([len(x),len(diction)])
        for i in range(len(x)):
            for j in range(len(diction)):
                tf[i][j]=x[i].count(diction[j])
        return tf
    def vectorize_train(self,x):
        diction=self.__diction(x)
        df=self.__get_df(x,diction)
        idf=self.__get_idf(x,df)
        tf=self.__get_tf(x,diction)
        return tf*idf
    def vectorize_test(self,x):
        tf=self.__get_tf(x,self.__dictionary)
        return tf*self.__idf
