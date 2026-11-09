import numpy as np

def simulate_first_order(controller,setpoint=1.0,sim_time=10,dt=0.01):
    t=np.arange(0,sim_time,dt)
    y=0.0
    r=[]
    for _ in t:
        u=controller.update(setpoint,y,dt)
        y += ((-y+u)/1.5)*dt
        r.append(y)
    return t,np.array(r)
