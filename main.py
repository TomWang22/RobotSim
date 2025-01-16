from robot_simulation import SimulationWithDynamics
from ros_integration import ROSIntegration
from city_navigation import CityNavigation
import numpy as np

def run_grid_simulation():
    grid = np.array([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    start = (0, 0)
    goal = (4, 4)
    dynamic_obstacles = [(2, 2), (3, 3)]
    sim = SimulationWithDynamics(grid, start, goal, dynamic_obstacles)
    sim.move_robot()

def run_ros_integration():
    ros = ROSIntegration()
    try:
        while not rospy.is_shutdown():
            ros.send_velocity_command(linear_x=0.5, angular_z=0.1)
    except rospy.ROSInterruptException:
        pass

def run_city_navigation():
    city = "New York, USA"
    nav = CityNavigation(city, api_key="YOUR_GOOGLE_MAPS_API_KEY")
    start = (40.730610, -73.935242)
    end = (40.712776, -74.005974)
    nav.plot_path(start, end)

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Grid Simulation")
    print("2. ROS Integration")
    print("3. City Navigation")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        run_grid_simulation()
    elif choice == "2":
        run_ros_integration()
    elif choice == "3":
        run_city_navigation()
    else:
        print("Invalid choice!")
