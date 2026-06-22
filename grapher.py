import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x=np.linspace(-100,100,300)



        
def coeff(n):
        coefff=[]
        for i in range(ord("a"),ord("a")+1+n):
         i=chr(i)
         i=float(input("enter coeff"))
         coefff.append(i)
        return coefff

def poly(coefff,x):
        y=np.polyval(coefff,x)
        return y


    
def roots(coefff):
        r=np.roots(coefff)
        mask=np.abs(r.imag)<10**-9
        r=r[mask].real
        df=pd.DataFrame({
              'roots':r
        })
        return df

def plot(x,y):
      plt.figure()
      plt.plot(x,y)
      plt.grid(True)
    
      plt.show()
            
f=input('choose function')  
if f=='polynomial':
    while True:
          try:
                n=int(input("choose degree"))
                if n>0:
                      break
                print("degree must be positive")
          except ValueError:
                print("Please enter an integer for degree.")

    
    coefff=coeff(n)
    
    y=poly(coefff,x)
   
    plot(x,y)   
    print(roots(coefff))    

else:
      print(f ,"is uanavailable") 

   



    
    







                          
        

    
     



              
            