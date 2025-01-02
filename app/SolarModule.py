class SolarModule:
    def __init__(self, model, technology, maxPower, efficiency,
                 nominalVoltage, openCircuitVoltage, shortCircuitCurrent,
                 dimensions, weight, connector, maxTempCoeff,
                 vocTempCoeff, iscTempCoeff, manufacturer):
        self.model = model
        self.technology = technology
        self.maxPower = maxPower
        self.efficiency = efficiency
        self.nominalVoltage = nominalVoltage
        self.openCircuitVoltage = openCircuitVoltage
        self.shortCircuitCurrent = shortCircuitCurrent
        self.dimensions = dimensions  # Dictionary with length, width, height
        self.weight = weight
        self.connector = connector
        self.maxTempCoeff = maxTempCoeff
        self.vocTempCoeff = vocTempCoeff
        self.iscTempCoeff = iscTempCoeff
        self.manufacturer = manufacturer

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Technology: {self.technology}")
        print(f"Max Power: {self.maxPower}W")
        print(f"Efficiency: {self.efficiency}%")
        print(f"Nominal Voltage (Vmpp): {self.nominalVoltage}V")
        print(f"Open Circuit Voltage (Voc): {self.openCircuitVoltage}V")
        print(f"Short Circuit Current (Isc): {self.shortCircuitCurrent}A")
        print(f"Dimensions (L x W x H): {self.dimensions['length']} x {self.dimensions['width']} x {self.dimensions['height']} mm")
        print(f"Weight: {self.weight} kg")
        print(f"Connector: {self.connector}")
        print(f"Max Temperature Coefficient: {self.maxTempCoeff}%/°C")
        print(f"Voc Temperature Coefficient: {self.vocTempCoeff}%/°C")
        print(f"Isc Temperature Coefficient: {self.iscTempCoeff}%/°C")
        print(f"Manufacturer: {self.manufacturer}")