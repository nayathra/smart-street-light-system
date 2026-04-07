import tkinter as tk
import threading
from detection import detect_objects

# Colors
BG = "#0D1117"
GREEN = "#3FB950"
RED = "#F85149"
WHITE = "#E6EDF3"


class SmartStreetApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AI Smart Street Light System")
        self.geometry("420x450")
        self.configure(bg=BG)

        self.running = False

        # Variables
        self.vehicle_var = tk.StringVar(value="Vehicles: —")
        self.weather_var = tk.StringVar(value="Weather: —")
        self.brightness_var = tk.StringVar(value="Brightness: —")
        self.accident_var = tk.StringVar(value="Accident: —")
        self.status_var = tk.StringVar(value="STOPPED")

        self.build_ui()

    # UI Layout
    def build_ui(self):

        tk.Label(self, text="SMART STREET LIGHT SYSTEM",
                 font=("Arial", 14, "bold"),
                 fg=WHITE, bg=BG).pack(pady=15)

        self.status_label = tk.Label(self, textvariable=self.status_var,
                                     fg=RED, bg=BG, font=("Arial", 12, "bold"))
        self.status_label.pack(pady=5)

        tk.Label(self, textvariable=self.vehicle_var, fg=WHITE, bg=BG).pack(pady=5)
        tk.Label(self, textvariable=self.weather_var, fg=WHITE, bg=BG).pack(pady=5)
        tk.Label(self, textvariable=self.brightness_var, fg=WHITE, bg=BG).pack(pady=5)

        self.accident_label = tk.Label(self, textvariable=self.accident_var,
                                      fg=WHITE, bg=BG, font=("Arial", 11, "bold"))
        self.accident_label.pack(pady=10)

        tk.Button(self, text="Start System", command=self.start_system,
                  bg=GREEN, fg="black", width=18, height=2).pack(pady=10)

        tk.Button(self, text="Stop System", command=self.stop_system,
                  bg=RED, fg="black", width=18, height=2).pack(pady=5)

    # Detection Thread
    def run_detection(self):

        def update_ui(vehicle, weather, brightness, accident):

            color = RED if accident == "DETECTED" else GREEN

            self.after(0, self.vehicle_var.set, f"Vehicles: {vehicle}")
            self.after(0, self.weather_var.set, f"Weather: {weather}")
            self.after(0, self.brightness_var.set, f"Brightness: {brightness}%")
            self.after(0, self.accident_var.set, f"Accident: {accident}")
            self.after(0, self.accident_label.config, {"fg": color})

        detect_objects(callback=update_ui)

    # Start
    def start_system(self):
        if self.running:
            return

        self.running = True
        self.status_var.set("RUNNING")
        self.status_label.config(fg=GREEN)

        threading.Thread(target=self.run_detection, daemon=True).start()

    # Stop
    def stop_system(self):
        self.running = False
        self.status_var.set("STOPPED")
        self.status_label.config(fg=RED)


if __name__ == "__main__":
    app = SmartStreetApp()
    app.mainloop()