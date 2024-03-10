# Mooc Radar Dataset Converter

This Python script is a tool for dealing with the [Mooc Radar dataset](https://github.com/THU-KEG/MOOC-Radar/). It reads JSON data related to student problems and cognitive dimensions, and converts it into a TSV (Tab Separated Values) format.

## Requirements

- Python 3.9 or higher
- ijson
- csv
- json
## Data Access
There are multi-level data to be used, including:

| Dataset          | Description                                           | Download Link                                                |
| ---------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| MoocRadar_Raw    | The raw data from MOOCCubeX (after data filtering).   | [Raw link](https://cloud.tsinghua.edu.cn/d/adc2d43d154944ffb75f/) |
| MoocRadar_Coarse | Exercises and behaviors with coarse-grained concepts. | [Coarse link](https://cloud.tsinghua.edu.cn/d/5443ee05152344c79419/) |
| MoocRadar_Middle | Exercises and behaviors with middle-grained concepts. | [Middle link](https://cloud.tsinghua.edu.cn/d/adf72390e3234143aec0/) |
| MoocRadar_Fine   | Exercises and behaviors with fine-grained concepts.   | [Fine link](https://cloud.tsinghua.edu.cn/d/308c17eeb99e4ebf98e2/) |
| External_Data    | Other additional data of MoocRadar.                   | [External link](https://cloud.tsinghua.edu.cn/d/000fddd19a434765872a/) |

## 
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
