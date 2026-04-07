import tkinter as tk

root = tk.Tk()
root.title("AI Smart Street Light Dashboard")
root.geometry("420x360")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="SMART STREET LIGHT SYSTEM",
    font=("Arial",16,"bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=15)

vehicle_label = tk.Label(root,font=("Arial",12),fg="white",bg="#1e1e2f")
vehicle_label.pack()

pedestrian_label = tk.Label(root,font=("Arial",12),fg="white",bg="#1e1e2f")
pedestrian_label.pack()

weather_label = tk.Label(root,font=("Arial",12),fg="white",bg="#1e1e2f")
weather_label.pack()

brightness_label = tk.Label(root,font=("Arial",12),fg="white",bg="#1e1e2f")
brightness_label.pack()

pole_label = tk.Label(root,font=("Arial",12),fg="white",bg="#1e1e2f")
pole_label.pack()

accident_label = tk.Label(root,font=("Arial",14,"bold"),fg="red",bg="#1e1e2f")
accident_label.pack(pady=10)


def update_dashboard(vehicle, pedestrian, weather, brightness, pole1, pole2, pole3, accident):

    vehicle_label.config(text=f"Vehicles Detected : {vehicle}")

    pedestrian_label.config(text=f"Pedestrian : {pedestrian}")

    weather_label.config(text=f"Weather : {weather}")

    brightness_label.config(text=f"AI Brightness : {brightness}%")

    pole_label.config(text=f"Pole1:{pole1}%   Pole2:{pole2}%   Pole3:{pole3}%")

    if accident:
        accident_label.config(text="🚨 ACCIDENT DETECTED")
    else:
        accident_label.config(text="")

    root.update()


# This part runs the dashboard when file is executed
if __name__ == "__main__":
    update_dashboard(2, True, "clear sky", 100, 100, 80, 60, True)
    root.mainloop()