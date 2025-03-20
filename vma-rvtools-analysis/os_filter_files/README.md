# OS Pattern Adder

This script allow users to add OS names to the file (`os_filter_patterns.txt`) located in the directory `os_filter_files` in a structured regex format. 
The OS names are cleaned before being added, ensuring that redundant information (e.g., `(32-bit)`, `(64-bit)`) is removed.

## 📌 Features
- Cleans OS names before adding them.
- Prevents duplicate entries.
- Appends OS names in regex format to `os_filter_patterns.txt`.

## 🛠️ Prerequisites
- Python 3.x installed
- `pandas` library (install using `pip install pandas`)

## 🚀 How to Use

### Run the Script
Open a terminal and execute:
```bash
python add_os_pattern.py
```

#### Example
```
python add_os_pattern.py

Enter OS name (or type 'exit' to quit): Ubuntu 24.04.2 LTS
[SUCCESS] Added pattern: ^Ubuntu\ 24\.04\.2\ LTS(?:\s*\(.*\))?$
```

and

```
python add_os_pattern.py

Enter OS name (or type 'exit' to quit): Ubuntu 24.04.2 LTS
[INFO] Pattern already exists: ^Ubuntu\ 24\.04\.2\ LTS(?:\s*\(.*\))?$
```
