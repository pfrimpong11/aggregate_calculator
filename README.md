# Aggregate Calculator

The Aggregate Calculator is a web application that calculates the aggregate score for students based on their grades in compulsory and optional courses. This project consists of a frontend built with HTML, CSS, and JavaScript, and a backend built with Python using the Flask framework.

## Features

- Input grades for compulsory and optional courses.
- Automatically handle missing grades by assigning a default value.
- Cap grades at a maximum of 4.
- Calculate the aggregate score using the smallest three grades from each category.

## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/aggregate-calculator.git
cd aggregate-calculator
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask development server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

## Usage

1. Enter the grades for compulsory and optional courses in the input fields. The grades must be positive integers.
2. Click the "Calculate Aggregate" button.
3. The total aggregate score will be displayed on the page.

### Notes

- The application will cap any grades above 4 at 4.
- If a course grade is not provided, the application will default it to 4 for the calculation.
