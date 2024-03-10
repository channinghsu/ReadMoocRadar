# Mooc Radar Dataset Converter

This Python script is a tool for dealing with the Mooc Radar dataset. It reads JSON data related to student problems and cognitive dimensions, and converts it into a TSV (Tab Separated Values) format.

## Requirements

- Python 3.9 or higher
- ijson
- csv
- json

## Usage

1. Ensure that your JSON data is in the correct format. The script expects JSON data where each line is a separate JSON object.

2. Run the script with the command `python main.py`.

3. The script will output a TSV file named `output_middle.tsv` in the same directory.

## Data Format

The script expects JSON data in the following format:

```json
{
  "problem_id": "Pm_2046133",
  "exercise_id": "Ex_1641736",
  "course_id": "C_674920",
  "cognitive_dimension": 4,
}
```

The output TSV file will have the following columns:

- num
- student
- skill
- right
- cognitive_level