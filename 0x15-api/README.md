# API Data Exporter

This repository contains Python scripts that interact with an API to gather data and export it into different formats.

## Scripts Overview

### 0-gather_data_from_an_API.py

This script retrieves data from an API endpoint and prints information about the employee with a specific ID.

### 1-export_to_CSV.py

This script extends the functionality of the previous one by exporting the data into a CSV file named `todo.csv`.

### 2-export_to_JSON.py

This script exports the data from the API into a JSON file named `todo_all_employees.json` in the required format.

### 3-dictionary_of_list_of_dictionaries.py

This script further extends the functionality to export data for all tasks from all employees into a JSON file named `todo_all_employees.json`, following a specific format.

## Usage

To run any of the scripts, simply execute them using Python 3:

```bash
python3 <script_name>.py
```

Replace `<script_name>` with the name of the script you want to run.

## Dependencies

All scripts require Python 3.x to be installed. Additionally, ensure you have the `requests` library installed, which can be installed via pip:

```bash
pip install requests
```

## API Endpoint

The scripts in this repository interact with the following API endpoint:

```
https://jsonplaceholder.typicode.com/todos
```

This endpoint provides dummy data about tasks assigned to various users.

## Output Files

- `todo.csv`: Contains exported data in CSV format.
- `todo_all_employees.json`: Contains exported data in JSON format, following the specified format.

## Example

After running the scripts, you can inspect the output files to see the exported data.

## Credits

These scripts were created as part of the ALX Software Engineering curriculum.

Feel free to reach out with any questions or suggestions for improvement!
