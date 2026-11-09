class PIDController:
    def __init__(self,kp,ki,kd):
        self.kp=kp; self.ki=ki; self.kd=kd
        self.i=0; self.prev=0
    def update(self,setpoint,y,dt):
        e=setpoint-y
        self.i+=e*dt
        d=(e-self.prev)/dt if dt else 0
        self.prev=e
        return self.kp*e+self.ki*self.i+self.kd*d
