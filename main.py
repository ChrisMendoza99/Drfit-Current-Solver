import math
#defining some constants
q = 1.60218e-19
Nc = 2.86e19
Nv = 2.66e19
Eg = 1.12
k = 8.617e-5
T = 300
L = math.exp(-Eg/(2*k*T))
#This takes the user inputs for the voltage, Nd, Na, Nb,and adds the to get the Nb
volt = float(input("Enter Voltage: "))
print("Voltage = ", volt)
length = float(input("Enter the length: "))
print("The length is: ", length)
Nd = float(input("Enter Nd value: "))
print("The value you entered for Nd is ",Nd)
Na = float(input("Enter Na value: "))
print("The value you entered for Nd is ", Na)
Nb = Na + Nd
print("The value of Nb is: ", Nb)
N = math.sqrt(Nc*Nv)*L
print("N = ",N)
n = float(0.5 * (Nd - Na + math.sqrt(((Nd - Na)**2)+ 4*(N)**2)))
print("Our n(electrons)",n)
p = float(0.5 * (Na - Nd + math.sqrt(((Nd - Na)**2)+ 4*(N)**2)))
print("Our p(holes)",p)
#Here were taking the values and computing to determine which are the majority or minority
if Nd > Na:
  a = 8.5*10**16
  b = 0.72
  Unn = float(65 + ((1330 - 65)/(1 + (Nb/a)**b)))
  Un = Unn
  print("The value of Un", Un)
else:
  j = 8.0*10**16
  k = 0.9
  Unp = float(232 + ((1412 + 232)/(1+(Nb/j)**k)))
  Un = Unp
  print("The value of Un: ", Un)
if Na > Nd:
  z = 6.3*10**16
  x = 0.76
  Upp = float(48 + ((495 - 48)/(1 + (Nb/z)**x)))
  Up = Upp
  print("The value of Up: ", Up)
else:
  c = 8.0*10**17
  d = 1.25
  Upn = float(130 + ((500 - 130)/(1 + (Nb/c)**d)))
  Up = Upn
  print("The value of Up: ", Up)
#Right after this we can calculate the Resistivity(P), and the Drift Current
P = (1/(q*n*Un+q + q*p*Up))
print("Thus our resitivity is ", P)
DC = float((1/P)*(volt/length))
print("Therefore our Drift Current is ", DC)
