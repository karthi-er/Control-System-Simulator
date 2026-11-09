from src.pid_controller import PIDController
from src.simulator import simulate_first_order
from src.response_metrics import calculate_metrics

pid=PIDController(2.0,0.5,0.1)
t,r=simulate_first_order(pid)
print(calculate_metrics(t,r))
