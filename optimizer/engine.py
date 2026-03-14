import random
import json

class NeuralOptimizer:
    """
    Simplified Neural-Network-based Inventory Optimizer for Relief Operations.
    Inspired by MATLAB/Simulink research at VIT.
    """
    def __init__(self, relief_center_id="RC-101"):
        self.center_id = relief_center_id
        self.stock_levels = {"Medical": 85, "Food": 40, "Water": 25, "Shelter": 10}

    def predict_demand(self, disaster_severity_index=0.85):
        """
        Simulates demand prediction using a weighting logic (Neural Mock).
        severity_index: float (0 to 1)
        """
        print(f"[{self.center_id}] Running Neural Demand Analysis (Severity: {disaster_severity_index*100}%)...")
        # Simplified weights representing neural activation
        demand = {item: round(level * (1 + disaster_severity_index)) for item, level in self.stock_levels.items()}
        return demand

class StrategicCoordinator:
    """
    GenAI Strategy Layer: Converts neural demand outputs into logistical commands.
    Reflects the 'Strategic Product Lead' role.
    """
    def __init__(self, optimizer):
        self.optimizer = optimizer

    def generate_strategy(self, severity=0.85):
        demand = self.optimizer.predict_demand(severity)
        strategy = []
        
        for item, required in demand.items():
            current = self.optimizer.stock_levels[item]
            shortfall = max(0, required - current)
            if shortfall > 0:
                strategy.append(f"CRITICAL: Dispatch {shortfall} units of {item} to {self.optimizer.center_id}")
            else:
                strategy.append(f"STABLE: {item} stock is sufficient for predicted demand.")
        
        return {
            "predicted_demand": demand,
            "logistical_commands": strategy,
            "priority": "HIGH" if severity > 0.7 else "MEDIUM"
        }

if __name__ == "__main__":
    # Test simulation
    optimizer = NeuralOptimizer()
    coordinator = StrategicCoordinator(optimizer)
    
    report = coordinator.generate_strategy(severity=0.9)
    print("--- Humanitarian AI Strategy Report ---")
    print(json.dumps(report, indent=2))
