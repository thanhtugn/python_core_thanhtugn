class Taxi:
    def __init__(self, distance, waiting_time, car_type):
        self.distance = distance
        self.waiting_time = waiting_time
        self.car_type = car_type

    def calculate_fare(self):
        if self.car_type == 4:
            base_fare = 11000
            fare_30km = 15300
            fare_above_30km = 12100
        elif self.car_type == 7:
            base_fare = 12000
            fare_30km = 16100
            fare_above_30km = 13800
        else:
            raise ValueError("Invalid car type")

        if self.distance <= 0:
            raise ValueError("Distance must be a positive number")
        elif self.distance <= 0.8:
            distance_fare = base_fare
        elif self.distance <= 30:
            distance_fare = base_fare + (self.distance - 0.8) * fare_30km
        else:
            distance_fare = base_fare + 29.2 * fare_30km + (self.distance - 30) * fare_above_30km

        if self.waiting_time < 0:
            raise ValueError("Waiting time cannot be negative")
        elif self.waiting_time <= 5:
            waiting_fare = 0
        else:
            waiting_fare = (self.waiting_time - 5) * 750

        return distance_fare + waiting_fare

def validate_positive_number(number, name):
    try:
        number = float(number)
        if number <= 0:
            raise ValueError(f"{name} must be a positive number")
        return number
    except ValueError:
        raise ValueError(f"{name} must be a number")


if __name__ == "__main__":
    try:
        distance = validate_positive_number(input("Enter the distance (km): "), "Distance")
        waiting_time = validate_positive_number(input("Enter the waiting time (min): "), "Waiting time")
        car_type = int(input("Enter the car type (4 or 7): "))
        taxi = Taxi(distance, waiting_time, car_type)
        fare = taxi.calculate_fare()
        print(f"Distance: {distance} km")
        print(f"Waiting time: {waiting_time} min")
        print(f"Car type: {car_type}")
        print(f"Total fare: {fare} VND")
    except ValueError as e:
        print(f"Error: {e}")
