from datetime import datetime



class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n



class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, mtype):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.mtype = mtype

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.mtype}"



def save_fleet_to_file(vehicles, filename):
    with open(filename, "w") as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.mtype}\n")


def load_fleet_from_file(filename):
    vehicles = []

    with open(filename, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == "Car":
                vehicles.append(Car(data[1], data[2], int(data[3]), data[4], int(data[5])))

            elif data[0] == "Truck":
                vehicles.append(Truck(data[1], data[2], int(data[3]), int(data[4]), int(data[5])))

            elif data[0] == "Motorcycle":
                vehicles.append(Motorcycle(data[1], data[2], int(data[3]), int(data[4]), data[5]))

    return vehicles



def main():
    vehicles = [
        Car("V001", "Tesla Model 3", 2023, "Electric", 4),
        Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]

    filename = "fleet.txt"

    save_fleet_to_file(vehicles, filename)

    loaded = load_fleet_from_file(filename)

    print(f"{len(loaded)} vehicles loaded successfully.\n")

    print("--- All Vehicles ---")
    for v in loaded:
        print(v)

    print("\n--- Recent Vehicles (Last 4 Years) ---")
    for v in loaded:
        if v.is_new(4):
            print(v)

    print("\n--- Electric Cars Only ---")
    for v in loaded:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(v)


if __name__ == "__main__":
    main()