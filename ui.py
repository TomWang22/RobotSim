import tkinter as tk
from tkinter import messagebox
from robot_simulation import SimulationWithDynamics
from ros_integration import ROSIntegration
from city_navigation import CityNavigation
import numpy as np

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Simulation")

        # Mode Selection
        tk.Label(root, text="Choose Mode:", font=("Arial", 14)).pack(pady=10)
        self.mode_var = tk.StringVar(value="grid")
        modes = [("Grid Simulation", "grid"), ("ROS Integration", "ros"), ("City Navigation", "city")]
        for text, mode in modes:
            tk.Radiobutton(root, text=text, variable=self.mode_var, value=mode, font=("Arial", 12)).pack(anchor="w")

        # Input Area
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)
        self.create_input_fields()

        # Run Button
        tk.Button(root, text="Start", font=("Arial", 14), command=self.run).pack(pady=20)

    def create_input_fields(self):
        # Grid Simulation Inputs
        self.grid_frame = tk.Frame(self.input_frame)
        tk.Label(self.grid_frame, text="Grid (comma-separated rows):", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        self.grid_entry = tk.Entry(self.grid_frame, font=("Arial", 12), width=50)
        self.grid_entry.grid(row=1, column=0, padx=5)
        self.grid_entry.insert(0, "0,1,0,0,0;0,1,0,1,0;0,0,0,1,0;1,1,0,0,0;0,0,0,0,0")
        self.grid_frame.pack()

        # City Navigation Inputs
        self.city_frame = tk.Frame(self.input_frame)
        tk.Label(self.city_frame, text="City Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        self.city_entry = tk.Entry(self.city_frame, font=("Arial", 12), width=30)
        self.city_entry.grid(row=1, column=0, padx=5)
        self.city_entry.insert(0, "New York, USA")

    def run(self):
        mode = self.mode_var.get()
        if mode == "grid":
            self.run_grid_simulation()
        elif mode == "ros":
            self.run_ros_integration()
        elif mode == "city":
            self.run_city_navigation()
        else:
            messagebox.showerror("Error", "Invalid mode selected!")

    def run_grid_simulation(self):
        try:
            grid_text = self.grid_entry.get()
            grid = np.array([list(map(int, row.split(","))) for row in grid_text.split(";")])
            start, goal = (0, 0), (4, 4)
            dynamic_obstacles = [(2, 2), (3, 3)]
            sim = SimulationWithDynamics(grid, start, goal, dynamic_obstacles)
            sim.move_robot()
        except Exception as e:
            messagebox.showerror("Error", f"Grid Simulation Failed: {e}")

    def run_ros_integration(self):
        try:
            ros = ROSIntegration()
            ros.send_velocity_command(linear_x=0.5, angular_z=0.1)
        except Exception as e:
            messagebox.showerror("Error", f"ROS Integration Failed: {e}")

    def run_city_navigation(self):
        try:
            city = self.city_entry.get()
            nav = CityNavigation(city, api_key="YOUR_GOOGLE_MAPS_API_KEY")
            nav.plot_path((40.730610, -73.935242), (40.712776, -74.005974))
        except Exception as e:
            messagebox.showerror("Error", f"City Navigation Failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
