# Robot Simulation Project

This project provides a Python-based robot simulation with dynamic obstacles, ROS integration, and city-based shortest-path finding. It also features a graphical user interface (GUI) for easier interaction.

---

## **Features**
1. **Grid Simulation**:
   - Simulates a robot navigating through a grid with dynamic obstacles.
   - Uses A* pathfinding algorithm to find the optimal path.
2. **ROS Integration**:
   - Sends velocity commands to a ROS-compatible robot for real-time control.
3. **City Navigation**:
   - Finds the shortest path between two locations in a city using OpenStreetMap data or Google Maps API.
4. **Graphical User Interface**:
   - Allows users to select modes, input configurations, and start simulations.

---

## **Requirements**

### **Python Version**
- Python 3.8 or newer

### **Dependencies**
- `numpy`: For numerical calculations.
- `matplotlib`: For visualization.
- `osmnx`: For city-based navigation and graph data.
- `networkx`: For shortest-path calculations.
- `googlemaps`: For Google Maps API integration.
- `tkinter`: Built-in Python library for the GUI.

---

## **Installation**

Follow these steps to set up the project on your system:

### **1. Clone the Repository**
Download the project files:
```bash
git clone https://github.com/yourusername/robot-simulation.git
cd robot-simulation
2. Set Up a Python Virtual Environment (Recommended)
Create and activate a virtual environment to keep dependencies isolated:

# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Required Libraries
Install the Python dependencies listed in the requirements.txt file:

pip install numpy matplotlib osmnx networkx googlemaps
If a requirements.txt file is not provided, manually install each library:

pip install numpy
pip install matplotlib
pip install osmnx
pip install networkx
pip install googlemaps
4. Set Up ROS (Optional)
For ROS integration, ensure ROS is installed on your system. Follow the official ROS installation guide.

Install additional ROS Python libraries:

pip install rospy
sudo apt-get install ros-noetic-geometry-msgs  # ROS Noetic (adjust for your ROS version)
Usage

Running the Main Program
To run the main program and select a mode:

python main.py
Running the Graphical User Interface
To start the GUI:

python ui.py
Mode Descriptions
Grid Simulation:
Simulates robot movement in a grid with dynamic obstacles.
Input grid details in the GUI or modify the default grid in robot_simulation.py.
ROS Integration:
Sends commands to a ROS-compatible robot.
Requires ROS to be installed and running on the system.
City Navigation:
Finds the shortest path between two locations using OpenStreetMap or Google Maps API.
Ensure you have an active internet connection for live traffic data.
Configuration
Google Maps API Key:
For City Navigation with live traffic, replace "YOUR_GOOGLE_MAPS_API_KEY" in city_navigation.py with your API key.
Obtain an API key from the Google Cloud Console.
Grid Simulation:
Edit the default grid, start, and goal positions in robot_simulation.py.
Examples

Grid Simulation
Default grid:
0,1,0,0,0
0,1,0,1,0
0,0,0,1,0
1,1,0,0,0
0,0,0,0,0
Start: (0, 0)
Goal: (4, 4)
Dynamic Obstacles: [(2, 2), (3, 3)]
City Navigation
Default city: New York, USA
Start: (40.730610, -73.935242)
Goal: (40.712776, -74.005974)
Troubleshooting

Missing Libraries: If you encounter ModuleNotFoundError, ensure all dependencies are installed:
pip install -r requirements.txt
ROS Connection Issues:
Ensure the ROS master node is running:
roscore
Verify the correct topic names (e.g., /cmd_vel).
Google Maps API Key:
If the live traffic feature fails, verify your API key has the correct permissions for the Directions API.
Future Enhancements

Add support for 3D robot simulation using PyBullet or Gazebo.
Implement reinforcement learning for dynamic obstacle avoidance.
Expand the GUI for more customization options.
Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.


---

### **Tips for a Detailed README**

1. **Be Explicit**:
   - Include exact commands for installation and running the program.
   - Provide examples for common use cases (e.g., grid layout, city names).

2. **Structure the Information**:
   - Use clear headings (e.g., **Requirements**, **Usage**, **Troubleshooting**).
   - Include step-by-step instructions.

3. **Highlight Examples**:
   - Add example configurations for different modes.
   - Use screenshots or diagrams to visualize outputs (optional).

4. **Make It Easy to Follow**:
   - Assume the user has minimal prior experience with Python or ROS.
   - Include links to external resources (e.g., Google API docs, ROS installation guide).

---
