#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_score(clf,x_train,x_test,y_train,y_test,train=True):
    if train:
        y_pred=clf.predict(x_train)
        
        print('\n-------Train Result--------')
        
        print(f'Accurancy score:{accuracy_score(y_train,y_pred)*100:.2f}%')
        
    elif train==False:
        pred=clf.predict(x_test)
        
          
        print('\n-------Train Result--------')
        
        print(f'Accurancy score:{accuracy_score(y_test,pred)*100:.2f}%')
        
        print(classification_report(y_test,pred,digits=2))
        

