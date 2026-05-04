import datetime

class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.occupied = False
        self.vehicle = None
        self.entry_time = None

    def park_vehicle(self, vehicle):
        if not self.occupied:
            self.occupied = True
            self.vehicle = vehicle
            self.entry_time = datetime.datetime.now()
            print(f"Vehicle {vehicle} parked in slot {self.slot_id} at {self.entry_time}")
            return True
        else:
            print(f"Slot {self.slot_id} is already occupied")
            return False

    def remove_vehicle(self):
        if self.occupied:
            entry_time = self.entry_time
            exit_time = datetime.datetime.now()
            duration = exit_time - entry_time
            hours = duration.total_seconds() / 3600
            fee = self.calculate_fee(hours)
            vehicle = self.vehicle
            print(f"Vehicle {vehicle} removed from slot {self.slot_id} at {exit_time}")
            print(f"Parking duration: {hours:.2f} hours")
            print(f"Fee: ${fee:.2f}")
            self.occupied = False
            self.vehicle = None
            self.entry_time = None
            return {'fee': fee, 'vehicle': vehicle, 'entry_time': entry_time, 'exit_time': exit_time}
        else:
            print(f"Slot {self.slot_id} is empty")
            return None

    def calculate_fee(self, hours):
        # Simple fee: $2 per hour
        return hours * 2

class ParkingLot:
    def __init__(self, num_slots):
        self.slots = [ParkingSlot(i) for i in range(1, num_slots + 1)]
        self.payment_roll = []  # List of payment records

    def find_available_slot(self):
        for slot in self.slots:
            if not slot.occupied:
                return slot
        return None

    def park_vehicle(self, vehicle):
        slot = self.find_available_slot()
        if slot:
            slot.park_vehicle(vehicle)
            return slot.slot_id
        else:
            print("No available slots")
            return None

    def remove_vehicle(self, slot_id):
        if 1 <= slot_id <= len(self.slots):
            slot = self.slots[slot_id - 1]
            result = slot.remove_vehicle()
            if result:
                self.payment_roll.append({
                    'slot_id': slot_id,
                    'vehicle': result['vehicle'],
                    'entry_time': result['entry_time'],
                    'exit_time': result['exit_time'],
                    'fee': result['fee']
                })
                return result['fee']
            return 0
        else:
            print("Invalid slot ID")
            return 0

    def display_payment_roll(self):
        print("\nPayment Roll:")
        for record in self.payment_roll:
            print(f"Slot {record['slot_id']}: Vehicle {record['vehicle']}, Fee: ${record['fee']:.2f}")

# Example usage
if __name__ == "__main__":
    lot = ParkingLot(5)  # 5 parking slots

    # Park some vehicles
    lot.park_vehicle("ABC123")
    lot.park_vehicle("XYZ456")

    # Simulate time passing (in real code, this would be automatic)
    import time
    time.sleep(2)  # Wait 2 seconds

    # Remove vehicles
    lot.remove_vehicle(1)
    lot.remove_vehicle(2)

    # Display payment roll
    lot.display_payment_roll()