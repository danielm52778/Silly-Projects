**Python Mini-Projects Collection**

**1. Age Guesser Game**

A simple app that can guess your age with just a single question. The app uses a simple GUI built in Python using the Tkinter library and 
handles user input, and a multi-page layout.


**2. Disneyland Wait Time Analysis**

A quick analysis from a recent trip to Disneyland that tracked the estimated wait time vs. the actual wait time experienced. The file output consists of 
four bar graphs and a table. One bar graph with the data combined from all three days, and the other three a breakdown of each individual day. Lastly, a table with a small summary of statistics calculated from the data. 

_(Example of actual output)_
![CombinedBarGraph](https://github.com/user-attachments/assets/7e789644-2c5e-4b2e-97dc-bd216c378e8a)


To run this for yourself using docker: 

```docker pull danielm52778/wait-time-analysis:latest```


macOS/Linux

```docker run --rm -v "$(pwd)/output":/app/output danielm52778/wait-time-analysis:latest```

Windows

```docker run --rm -v "%cd%/output":/app/output danielm52778/wait-time-analysis:latest```

_Expected output: 4 bar charts and 1 table in a folder named 'output'_


**3. Milage Tracker (Ongoing)**

An ongoing project to track milage and gas prices when I refuel. The tracker does not take into account variables such as road conditions, driving style, city vs. highway miles, etc... The output graphs visualize the correlation between MPG and daily average temperature (if any). MPG in the data is calculated by dividing the number of miles driven by a approximation of the number of gallons used to refill the tank. 

![temp vs mpg](https://github.com/user-attachments/assets/32c263e3-3236-41df-9dd4-a2250a4efa5b)
