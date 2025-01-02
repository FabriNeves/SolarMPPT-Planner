class Inverter:
    def __init__(self, model, dcInput, acOutput, efficiency, environmentLimits, general):
        self.model = model
        self.dcInput = dcInput
        self.acOutput = acOutput
        self.efficiency = efficiency
        self.environmentLimits = environmentLimits
        self.general = general

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"DC Input: {self.dcInput}")
        print(f"AC Output: {self.acOutput}")
        print(f"Efficiency: {self.efficiency}")
        print(f"Environment Limits: {self.environmentLimits}")
        print(f"General: {self.general}")
