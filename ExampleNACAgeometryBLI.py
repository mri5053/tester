from matplotlib.pyplot import subplots, show
from numpy import arange, cos, linspace, pi 

# NACA 0010 Airfoil 

theta = linspace (0,pi)
x  = -0.5*(cos(theta)-1)
t  = 0.1
yt = 5*t*(0.2969*x**0.5-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

xinl = -1.75
xout = 2.57
ybot = -2
ytop = 2.5

# Writing out MSES blade.xxx file
with open('MSES/blade.naca_bli','w') as f:
    f.write('NACA BLI Example')
    f.write('\n {0:5} {1:5} {2:5} {3:5}'.format(xinl, xout,ybot,ytop)) 


#nacelle 
for i in arange(len(x)-1,-1,-1):
    f.write('\n{0:9.6f5} {1:9.6f}'.format((x[i]+4)/5, -yt[i]/5+0.18))
for i in arange(1,len(x)):
    f.write('\n{0:9.6f} {1:9.6f}'.format((x[i]+4)/5, yt[i]/5+0.18))


#Center Body 
f.write('\n999. 999.')
for i in arange(len(x)-1,-1,-1):
    f.write('\n{0:9.6f} {1:9.6f}'.format((x[i]+4.2)/5, -yt[i]/2.5+0.09))
for i in arange(1,len(x)):
    f.write('\n{0:9.6f} {1:9.6f}'.format((x[i]+4.2)/5, yt[i]/2.5+0.09))


#Main Body
f.write('\n999. 999.')
for i in arange(len(x)-1,-1,-1):
    f.write('\n{0:9.6f} {1:9.6f}'.format(x[i], -yt[i]))
for i in arange(1,len(x)):
    f.write('\n{0:9.6f} {1:9.6f}'.format(x[i], yt[i]))


fig, ax = subplots()

ax.plot(x,yt,c='tab:blue')
ax.plot(x,-yt,c='tab:blue')

ax.plot((x+4.2)/5, yt/2.5+0.09,c='tab:green')
ax.plot((x+4.2)/5, -yt/2.5+0.09,c='tab:green')

ax.plot((x+4)/5, yt/5+0.18,c='tab:red')
ax.plot((x+4)/5, -yt/5+0.18,c='tab:red')

show()
