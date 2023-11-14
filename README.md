Clima - Weather Application by Juan Schunk
Overview
Clima is a Python-based desktop application developed by Juan Schunk, providing real-time weather information for six distinct cities. Powered by the OpenWeather API, this application enables users to effortlessly fetch and display current weather conditions and time data for their preferred cities. Each city is conveniently associated with a dedicated button, triggering the data retrieval process and updating the graphical user interface in real-time.

Features
City Selection: Choose from a carefully curated list of cities, including Amsterdam, Barcelona, Berlin, Buenos Aires, Kyiv, and Paris.

Weather Information: Retrieve detailed weather information, including temperature in Celsius and a concise description of the current weather conditions.

Real-Time Clock: Display the local time for the selected city, ensuring users are kept informed about the current time in their chosen location.

Dynamic Backgrounds: Enhance the user experience with visually appealing backgrounds associated with each city.

Dependencies
Tkinter: Used for creating the graphical user interface and managing the application's layout.

PIL (Pillow): Employed for handling and resizing images to serve as dynamic backgrounds.

Requests: Utilized for making HTTP requests to the OpenWeather API to retrieve weather data.

Usage
Installation:

Ensure Python is installed on your system.
Install the required dependencies using the requirements.txt file:
Copy code
pip install -r requirements.txt
Run the Application:

Execute the application by running the clima.py script or use the provided executable (clima.exe).
Choose a city by clicking on the corresponding button.
View real-time weather information and local time for the selected city.
Security Considerations
API Key Protection: Safeguard the confidentiality of your OpenWeather API key. Avoid exposing it directly in the codebase.
