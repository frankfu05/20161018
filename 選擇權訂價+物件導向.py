
# coding: utf-8

# In[21]:

class BS_closedform :
    def  __init__(self,S0,Sigma,K,R,T,N=10000):
        self.S0=S0
        self.Sigma=Sigma
        self.K=K
        self.R=R
        self.T=T
        self.N=N
    
    def MCS(self,N=10000):
        import numpy as np
        z= np.random.standard_normal(self.N)
        ST=self.S0*np.exp((self.R-0.5*self.Sigma**2)*self.T+self.Sigma*np.sqrt(self.T)*z)
        CT=np.maximum(ST-self.K,0)
        C0=np.sum(np.exp(-self.R*self.T)*CT)/self.N
        print(C0)
        
    def BS(self):
        from math import log, sqrt, exp
        from scipy import stats
        d1=(log(self.S0/self.K)+(self.R+0.5*self.Sigma**2)*self.T)/(self.Sigma*sqrt(self.T))
        d2=d1-self.Sigma*sqrt(self.T)
        C0=self.S0*stats.norm.cdf(d1, 0, 1)-self.K*exp(-self.R*self.T)*stats.norm.cdf(d2,0,1)
        print(C0)
    
        


# In[22]:

op = BS_closedform(100,0.3,105,0.05,0.5)


# In[13]:

op.MCS()


# In[23]:

op.BS()


# In[ ]:



