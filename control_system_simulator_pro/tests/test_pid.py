from src.pid_controller import PIDController

def test_pid():
 p=PIDController(1,1,1); assert p.kp==1
