import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(-100,100,300)


        
def coeff(n): #coefficient_extractor block for the given the degree
        coefff=[]
        for i in range(ord("a"),ord("a")+1+n):
         i=chr(i)
         i=float(input("enter coeff"))
         coefff.append(i)
        return coefff

def poly(coefff,x): #polynomial block
        y=np.polyval(coefff,x)
        return y


    
def roots(coefff):  # roots extractor block to filter the real ones from imaginery ones
        r=np.roots(coefff)
        mask=np.abs(r.imag)<10**-9
        r=r[mask].real
        df=pd.DataFrame({
              'roots':r
        })
        return df

def plot(x,y):  # plotting block after identifying y=f(x)
      plt.figure()
      plt.plot(x,y)
      plt.grid(True)

      plt.xlabel('x')
      plt.ylabel('f(x)')
      plt.ylim(-10,10)
      
      plt.show()
            
def trig(x): # trig functions block that can handle asympotetes of tan(x)
      ch=input("choose type")
      func_type={"sin":np.sin,
                 "cos":np.cos,
                 "tan":np.tan}
      
      func=func_type.get(ch)
      if func is None:
            print("unavailable")
            return None 
      
      para=[]
      for i in range (ord('a'),ord('a')+4):
            par=float(input('choose parameter'))
            para.append(par)

      t=para[0]*func(para[1]*x + para[2])+para[3]
      if func is np.tan:
            mask= ~np.isfinite(t)
            t[mask]=np.nan

      return t

f=input('choose a function')
if f not in ["poly","tri"]:
    while True:
            print(f"{f} is unavailable")
            f=input('choose a function')
            if f in ["poly","trig"]:
                  break
if f=='poly':
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
elif f=="trig":
      x=np.linspace(-2*np.pi,2*np.pi,1000)
      y=trig(x)
      if y is not None:
            plot(x,y)
      else:
            print('unavailable')

    
      
          
          



    
    







                          
        

    
     



              
            