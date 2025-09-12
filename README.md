**Python Mini-Projects Collection**

**1. Age Guesser Game**

A simple app that can guess your age with just a single question. The app uses a simple GUI built in Python using the Tkinter library and 
handles user input, and a multi-page layout.

**Key Features:**

- Simple layout
- Interactive
- Basic input validation

**2. Disneyland Wait Time Analysis**

A quick analysis from a recent trip to Disneyland that tracked the estimated wait time vs. the actual wait time experienced. The file output consists of 
four bar graphs and a table. One bar graph with the data combined from all three days, and the other three a breakdown of each individual day. Lastly, a table with a small summary of statistics calculated from the data. 

![CombinedBarGraph](https://github.com/user-attachments/assets/7e789644-2c5e-4b2e-97dc-bd216c378e8a)
_(Example of actual output)_

Here are the commands for running this project through a docker container:

```docker pull danielm52778/wait-time-analysis:latest```


macOS/Linux

```docker run --rm -v "$(pwd)/output":/app/output danielm52778/wait-time-analysis:latest```

Windows

```docker run --rm -v "%cd%/output":/app/output danielm52778/wait-time-analysis:latest```
