import time

class User:
    # Handles user authentication
    __USER_CREDENTIALS = {"username": "gymrats", "password": "123456"}

    @staticmethod
    def login():
        # Logs the user into the system
        print("Welcome to the Real World Guys!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if (username == User.__USER_CREDENTIALS["username"] and
            password == User.__USER_CREDENTIALS["password"]):
            print("Login successful, start grinding!\n")
            return True
        else:
            print("Invalid username or password. Please try again.\n")
            return False


class WorkoutDay:
    def __init__(self, day_name, exercises):
        self.day_name = day_name
        self.exercises = exercises

    def display_and_track(self):
        # Displays available exercises and tracks the selected exercise
        print(f"\n--- {self.day_name} Exercises ---")
        for index, exercise in enumerate(self.exercises, 1):
            print(f"{index}. {exercise}")

        choice = input(f"\nSelect an exercise for {self.day_name} (1-{len(self.exercises)}): ")

        if choice.isdigit() and 1 <= int(choice) <= len(self.exercises):
            exercise_name = self.exercises[int(choice) - 1]
            self.track_exercise(exercise_name)
        else:
            print("Invalid choice, please try again.")

    def track_exercise(self, exercise_name):
        # Tracks the progress of the selected exercise
        sets = int(input(f"\nHow many sets of {exercise_name} would you like to do? "))
        reps = int(input(f"How many reps per set of {exercise_name}? "))

        print(f"\nStarting {exercise_name} workout...\n")
        total_reps = sets * reps

        for set_number in range(1, sets + 1):
            print(f"\nSet {set_number} of {sets}")
            input(f"Press Enter to start set {set_number} of {exercise_name}...")

            print(f"\nSet {set_number} of {exercise_name} complete!")

            if set_number < sets:
                rest_time = int(input("How long would you like to rest between sets (in seconds)? "))
                print(f"Resting for {rest_time} seconds...")
                time.sleep(rest_time)
                print(f"Rest time is over. Let's go to set {set_number + 1}!\n")

        print(f"\nWorkout complete! You did {total_reps} reps of {exercise_name}.\n")


class Workout(WorkoutDay):
    def __init__(self, day_name, exercises):
        super().__init__(day_name, exercises)


class ChestWorkout(Workout):
    def __init__(self):
        super().__init__("Chest Day", [
            "Bench Press",
            "Incline Dumbbell Press",
            "Dumbbell Flyes",
            "Cable Chest Fly"
        ])


class LegsWorkout(Workout):
    def __init__(self):
        super().__init__("Legs Day", [
            "Squats",
            "Romanian Deadlifts",
            "Leg Press",
            "Leg Extension"
        ])


class BackWorkout(Workout):
    def __init__(self):
        super().__init__("Back Day", [
            "Seated Cable Row",
            "Lat Pulldown",
            "Deadlift",
            "Pull-ups"
        ])


class BicepsWorkout(Workout):
    def __init__(self):
        super().__init__("Biceps Day", [
            "Cable Curl",
            "Hammer Curl",
            "Preacher Curl",
            "Dumbbell Curl"
        ])


class TricepsWorkout(Workout):
    def __init__(self):
        super().__init__("Triceps Day", [
            "Tricep Pushdown",
            "Tricep Extension",
            "Diamond Pushups",
            "Dips"
        ])


class ShouldersWorkout(Workout):
    def __init__(self):
        super().__init__("Shoulders Day", [
            "Lateral Raise",
            "Dumbbell Front Raise",
            "Dumbbell Shoulder Press",
            "Shrugs"
        ])


class FitnessTracker:
    def __init__(self):
        self.workout_days = {
            "1": ChestWorkout(),
            "2": LegsWorkout(),
            "3": BackWorkout(),
            "4": BicepsWorkout(),
            "5": TricepsWorkout(),
            "6": ShouldersWorkout()
        }

    @staticmethod
    def display_main_menu():
        print("\n--- Available Gym Exercises ---")
        print("1. Chest Day")
        print("2. Legs Day")
        print("3. Back Day")
        print("4. Biceps Day")
        print("5. Triceps Day")
        print("6. Shoulders Day")
        print("7. Cardio")
        print("8. Exit")

    def start(self):
        if not User.login():
            return  # Exit if login fails

        while True:
            self.display_main_menu()
            choice = input("\nSelect an exercise (1-8): ")

            if choice in self.workout_days:
                self.workout_days[choice].display_and_track()
            elif choice == "7":
                print("\nCardio exercises can be tracked manually.")
                # Implement Cardio tracking logic if needed
            elif choice == "8":
                print("\nWhat seems impossible today will one day become your warm-up. Well Done Champ!")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.start()