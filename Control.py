import numpy as np
import matplotlib.pyplot as plt

def TransportPhenomenaGUI(W_Liquido,W_Solido,GE):
  Cv = ( (W_Solido/GE)/(W_Solido/GE + W_Liquido) ) * 100
  Mup_Mu = 1 + (2.5*Cv) + (10.05*Cv**2) 
  return(Cv,Mup_Mu)