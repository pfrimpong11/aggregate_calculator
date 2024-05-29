from flask import Flask, render_template, request, jsonify
from calculations import calculate_total_aggregate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def calculate_total_aggregate(compulsory_data, optional_data):
    def validate_and_convert_grade(grade):
        try:
            grade = int(grade)
            if grade < 1:
                raise ValueError("Grade must be a positive integer")
            return min(grade, 4)  # Cap the grade at 4
        except (ValueError, TypeError):
            return 4

    compulsory_grades = [validate_and_convert_grade(grade) for grade in list(compulsory_data.values())[:4]]
    optional_grades = [validate_and_convert_grade(grade) for grade in list(optional_data.values())[:4]]

    compulsory_grades.sort()
    optional_grades.sort()

    compulsory_sum = sum(compulsory_grades[:3])
    optional_sum = sum(optional_grades[:3])

    total_aggregate = compulsory_sum + optional_sum
    return total_aggregate

@app.route('/calculate-aggregate', methods=['POST'])
def calculate_aggregate():
    data = request.json
    compulsory_data = data.get('compulsory', {})
    optional_data = data.get('optional', {})

    total_aggregate = calculate_total_aggregate(compulsory_data, optional_data)

    return jsonify({'total_aggregate': total_aggregate})

if __name__ == '__main__':
    app.run(debug=True)
