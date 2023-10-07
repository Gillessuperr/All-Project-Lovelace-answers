# Project Lovelace easy to hard
#%%
# Scientific temperatures
def fahrenheit_to_celsius(F):
    C = 0
    C = (F - 32) * 5 / 9
    
    return C

#%% Speed of light
c = 299792458  # Speed of light [m/s]

def light_time(distance):
    t = 0
    t=distance/c

    return t

#%% Plump moose
a=2.757
b=16.793
def moose_body_mass(latitude):
    mass = 0
    mass = a*latitude+b

    return mass

#%% NAND gate
def NAND(A, B):
    nand = 0
    if A==1 and B==1:
        nand = 0
    else:
        nand = 1
    return nand

#%% Compound interest
def compound_interest(amount, rate, years):
    new_amount = 0
    new_amount = amount*(1+rate)**years
    return new_amount
#%% Wind chill
def wind_chill(T_a, v):
    T_wc = 0
    T_wc = 13.12+0.6215*T_a - 11.37*v**0.16 + 0.3965*T_a*v**0.16

    return T_wc
#%% Flight paths
import math
from math import radians, sqrt, asin, sin, cos

R  = 6372.1  # Radius of the Earth [km]

def haversine_distance(lat1, lon1, lat2, lon2):
    d = 0
    lat1=radians(lat1)
    lat2=radians(lat2)
    lon1=radians(lon1)
    lon2=radians(lon2)
    d=2*R*math.asin(math.sqrt((math.sin((lat2-lat1)/2))**2+math.cos(lat1)*math.cos(lat2)*(math.sin((lon2-lon1)/2))**2))
    return d
#%% Almost pi
def almost_pi(N):
    k=1
    pi=0
    for k in range(N):
        pi+=((-1)**k)/(2*k+1)
    return 4*pi
# %% Temperature variations
def temperature_statistics(T):
    mean = 0
    std  = 0
    mean=sum(T)/len(T)
    std=sum([(x-mean)**2 for x in T])/len(T)
    std=std**0.5
    return mean, std
#%% Blood types
def survive(blood_type, donated_blood):

    canbesaved = False
    
    if blood_type == "A-":
        compatible_bt = ["A-", "O-"]
    elif blood_type == "A+":
        compatible_bt = ["A-", "O-","A+", "O+"]
    elif blood_type == "B-":
        compatible_bt = ["B-", "O-"]
    elif blood_type == "B+":
        compatible_bt = ["B-", "O-","B+", "O+"]
    elif blood_type == "AB-":
        compatible_bt = ["A-", "O-","B-", "AB-"]
    elif blood_type == "AB+":
        compatible_bt = ["A-","O-","A+", "O+", "B-","B+","AB-","AB+"]
    elif blood_type == "O+":
        compatible_bt = ["O-", "O+"]
    elif blood_type == "O-":
        compatible_bt = ["O-"]
    
    for j in range(0,len(compatible_bt)):
        print(compatible_bt[j])
        for i in range(0,len(donated_blood)):
            print(donated_blood[i])
            if compatible_bt[j] == donated_blood[i]:
                canbesaved = True            
                break
        if canbesaved == True:
            break
    
    return canbesaved
#%% Babylonian square roots
def babylonian_sqrt(S):
    
    return 0