
def yfunc(t,v0,g=9.81):
    y = v0*t-0.5*g*t**2
    dydt = v0-g*t
    return y,dydt


t_values = [0.05*i for i in range(20)]
t_values2 = [0.3*i for i in range(20)]

for t in t_values:
    pos, vel = yfunc(t,5)
    print('Erde: t=%-12g position=%12g velocity=%12g' %(t,pos,vel))

for t in t_values:
    pos, vel = yfunc(t,5,g=1.62)
    print('Erde: t=%-12g position=%12g velocity=%12g' %(t,pos,vel))

    # Keyword argumente lernen