
class WindDescriptor:
    def __init__(self):
        super(WindDescriptor, self).__init__()
    
    def wind_direction(self, degrees):
        directions = [
            "North", "North-Northeast", "Northeast", "East-Northeast", "East", "East-Southeast", "Southeast", "South-Southeast",
            "South", "South-Southwest", "Southwest", "West-Southwest", "West", "West-Northwest", "Northwest", "North-Northwest"]
        calculate_index = int((degrees + 11.25)/22.5 - 0.02)
        return directions[calculate_index % len(directions)]
