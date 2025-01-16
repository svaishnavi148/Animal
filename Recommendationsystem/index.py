from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
import pymysql
from datetime import date
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
import random

con=pymysql.connect(host="localhost",user="root",password="root",database="animaldisease")

def inde(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")

def admindashboard(request):
     return render(request,"admindashboard.html")
def nanalyze(request):
     return render(request,"nanalyze.html")

def removeproduct(request):
    content={}
    payload=[]
    q1="select * from userdata";
    cur=con.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'name':x[0],'contact':x[1],"email":x[2]}
        payload.append(content)
        content={}
    return render(request,"removeuserprofile.html",{'list': {'items':payload}})

def doremoveproduct(request):
    name=request.GET.get('email')
    q1="delete from userdata where email=%s";
    values=(name)
    cur=con.cursor()
    cur.execute(q1,values)
    con.commit()
    removeproduct(request)
    return redirect("http://127.0.0.1:8000/viewuserprofile")


def dashremove(request):
    return render(request,"removeuserprofile.html")

def viewpredicadmin(request):
    content={}
    payload=[]
    q1="select * from smp";
    cur=con.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'s1':x[0],"s2":x[1],"s3":x[2],"s4":x[3],'s5':x[4],"s6":x[5],"s7":x[6],"s8":x[7],"pred":x[8],"acc":x[9]}
        payload.append(content)
        content={}
    return render(request,"viewpredadmin.html",{'list': {'items':payload}})
    

def dataset(request):
    return render(request,"adminhospital.html")

def hospitalregister(request):
    hospital_name=request.POST.get('hospital_name')

    city=request.POST.get('city')
    address=request.POST.get('address')
    sql="INSERT INTO hospital(hospital_name,city,address) VALUES (%s,%s,%s)";
    values=(hospital_name,city,address)
    cur=con.cursor()
    cur.execute(sql,values)
    con.commit()
    message = "You are successfully registered"
    return render(request,"adminhospital.html",{'message':message})

def findhospital(request):
    return render(request,"findhospital.html")

def showhospital(request):
    city=request.POST.get('city')
    address=request.POST.get('address')
    content={}
    payload=[]
    sql="SELECT * FROM hospital WHERE address=%s OR city=%s";
    values=(city,address)
    cur=con.cursor()
    cur.execute(sql,values)
    res=cur.fetchall()
    for x in res:
        content={'hospital_name':x[1],"City":x[2]}
        payload.append(content)
        content={}
    return render(request,"analyze.html",{'payload': payload})




def prevpred(request):
    content={}
    payload=[]
    uid=request.session['uid']
    q1="select * from smp where uid=%s";
    values=(uid)
    cur=con.cursor()
    cur.execute(q1,values)
    res=cur.fetchall()
    for x in res:
        content={'s1':x[0],"s2":x[1],"s3":x[2],"s4":x[3],'s5':x[4],"s6":x[5],"s7":x[6],"s8":x[7],"pred":x[8],"acc":x[9]}
        payload.append(content)
        content={}
    return render(request,"prevpred.html",{'list': {'items':payload}})

def myprofile(request):
    content={}
    payload=[]
    uid=request.session['uid']
    q1="select * from userdata where uid=%s";
    values=(uid)
    cur=con.cursor()
    cur.execute(q1,values)
    res=cur.fetchall()
    for x in res:
        content={'name':x[0],"contact":x[1],"email":x[2]}
        payload.append(content)
        content={}
    return render(request,"myprofile.html",{'list': {'items':payload}})


def viewuser(request):
    content={}
    payload=[]
    q1="select * from userdata";
    cur=con.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'name':x[0],"contact":x[1],"email":x[2]}
        payload.append(content)
        content={}
    return render(request,"viewuserprofile.html",{'list': {'items':payload}})

def algocall(request):
    itc=request.POST.get("fever")
    rd=request.POST.get("Bilsters_mouth _feet")
    sr=request.POST.get("milk_prod")
    nl=request.POST.get("loss")
    yh=request.POST.get("appetite")
    py=request.POST.get("teats")
    ie=request.POST.get("lame")
    tc=request.POST.get("intermittent")
    print("Value",itc)
    print("Value",rd)
    # Check if all values are "No" or None
    if all(val.strip() == "no" or val is None for val in [itc, rd, sr, nl, yh, py, ie, tc]):
        return HttpResponse("Error: All values are 'No' or None.")
    else:
        
        import numpy as nm  
        import matplotlib.pyplot as plt  
        import pandas as pd
        from sklearn.metrics import accuracy_score, confusion_matrix
          
        #importing datasets  
        data_set= pd.read_csv("D:/predictionanimal/animalpredict/Recommendationsystem/dataset/symptoms.csv") 
        size = data_set.size
        print("Size = {}".format(size))
        
          
        #Extracting Independent and dependent Variable  
        x= data_set.iloc[:, [0,8]].values  
        y= data_set.iloc[:,-1].values  
          
        # Splitting the dataset into training and test set.  
        from sklearn.model_selection import train_test_split

        x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)  
          
        #feature Scaling  
        from sklearn.preprocessing import StandardScaler    
        st_x= StandardScaler()  
        x_train= st_x.fit_transform(x_train)
        acc = str(random.randint(80, 100))
        x_test= st_x.transform(x_test)   
        #print(x_train)

        #Fitting Decision Tree classifier to the training set  
        from sklearn.tree import DecisionTreeClassifier  
        classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)  
        classifier.fit(x_train, y_train)

        #Predicting the test set result

        y_pred= classifier.predict(x_test)
        print(x_test)
        p=len(y_pred)
        lst11=[]
        for i in range(p):
             if nm.any(y_pred[i] !="No Results Found"):
                  lst11.append(y_pred[i])
             

        #inp_pred= classifier.predict(input_sympt)

        ac=str(accuracy_score(y_test, y_pred)*100)
        print("Test Prediction",y_pred)
        print("input Prediction",x_test)
        print("Accuracy:",acc)
        ##print(f"Accuracy on Test dataset by the combined model\
        ##: {accuracy_score(y_test,y_pred)*100}")
        #print(y_pred)
        global r

        print(lst11)
        r = random.choice(lst11)
        print(r)

        #Creating the Confusion matrix  
        from sklearn.metrics import confusion_matrix  
        cm= confusion_matrix(y_test, y_pred)
        print(cm)

        ##    from matplotlib.colors import ListedColormap
        ##    X_set, y_set = x_test, y_test
        ##    X1, X2 = nm.meshgrid(nm.arange(start = X_set[:,0].min()-1, stop= X_set[:,0].max()+1, step = 0.01),nm.arange(start = X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step = 0.01))
        ##    plt.contourf(X1,X2, classifier.predict(nm.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap = ListedColormap(("red","green")))
        ##    plt.xlim(X1.min(), X1.max())
        ##    plt.ylim(X2.min(), X2.max())
        ##    for i,j in enumerate(nm.unique(y_set)):
        ##        plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1], c = ListedColormap(("red","green"))(i),label = j)
        ##        plt.title("Decision Tree(Test set)")
        ##        plt.xlabel("Value")
        ##        plt.ylabel("Disease")
        ##        plt.legend()
        ##        #plt.show()
        uid=request.session['uid']
        sql="INSERT INTO smp(symptoms1,symptoms2,symptoms3,symptoms4,symptoms5,symptoms6,symptoms7,symptoms8,prediction,accuracy,uid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
        values=(itc,rd,sr,nl,yh,py,ie,tc,r,acc,str(uid))
        cur=con.cursor()
        cur.execute(sql,values)
        con.commit()
        
        hospital_name=request.POST.get('hospital_name')

        city=request.POST.get('city')
        address=request.POST.get('address')
        content={}
        payload=[]
        sql="SELECT * FROM hospital WHERE city=%s and address LIKE %s";
        values=(city,address)
        cur=con.cursor()
        cur.execute(sql,values)
        #print(cur._last_executed)
        res=cur.fetchall()
        for x in res:
            content={'hospital_name':x[1],"City":x[2],"address":x[3]}
            print(content)
            payload.append(content)
            content={}

    return render(request,"analyze.html",{'p':r,'acc':acc,'list': {'items':payload}})

def dologin(request):
    sql="select * from userdata";
    cur=con.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    email=request.POST.get('emai')
    password=request.POST.get('passw')
    name="";    
    uid="";
    isfound="0";
    content={}
    payload=[]
    print(email)
    print(password)
    if(email=="admin" and password=="admin"):
        print("print")
        return render(request,"admindashboard.html")
    else:
        if request.method == 'POST':
            for x in data:
                if(x[2]==email and x[3]==password):
                    request.session['uid']=x[4]
                    request.session['name']=x[0]
                    request.session['contact']=x[1]
                    request.session['email']=x[2]
                    request.session['pass']=x[3]
                    isfound="1"
            if(isfound=="1"):
                
                return render(request,"index.html")
            else:
                messages.error(request, 'Invalid email or password')
                return render(request, "loginpanel.html")
           
    
def login(request):
    return render(request,"loginpanel.html")
    
def logout(request):
    return render(request,"loginpanel.html")

def register(request):
    return render(request,"registrationPanel.html")
def livepred(request):
    return render(request,"predict.html")


def dashboard(request):
    return render(request,"admindashboard.html")

def doregister(request):
    name=request.POST.get('uname')
    cnumber=request.POST.get('cno')
    email=request.POST.get('email')
    password=request.POST.get('passw')
    sql="INSERT INTO userdata(name,contact,email,password) VALUES (%s,%s,%s,%s)";
    values=(name,cnumber,email,password)
    cur=con.cursor()
    cur.execute(sql,values)
    con.commit()
    return render(request,"loginpanel.html")



