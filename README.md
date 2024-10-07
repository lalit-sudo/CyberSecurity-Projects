# MalwareWatchDog

**MalwareWatchDog** is a Python-based malware detection tool designed to scan files and folders for known malware signatures. This tool allows you to detect, quarantine, or remove potentially malicious files from your system. It uses a signature-based detection method, leveraging a database of MD5 hashes to identify known malware.

## Features

- **Signature-Based Detection**: Identifies malware using known MD5 hash signatures.
- **Scanning Options**: Allows scanning of specific folders, individual files, or the entire system.
- **Multithreading**: Supports multithreaded scanning for improved performance.
- **Quarantine and Removal**: Offers options to quarantine or remove detected malware files.
- **Verbose Mode**: Provides detailed output during scanning.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Requirements

- Python 3.x
- The `requests` library (automatically installed by `setup_and_run.py`)

## Installation and Usage

1. Clone the Repository
```bash
git clone https://github.com/lalit-sudo/MalwareWatchDog.git
cd MalwareWatchDog
```
2. Run the Setup and Main Tool                                                                                                                                              

The setup_and_run.py script will check for required libraries, install them if needed, and then run the main malware detection tool.
```bash
python setup_and_run.py
```
3. Choose a Scanning Option

Upon running the tool, you’ll be prompted to select a scanning option:

      1. Scan a specific folder
      2. Scan a specific file
      3. Scan the entire system
      After selecting an option, follow the on-screen instructions to start the scan.

Example Usage

To enable verbose mode and scan a specific folder
```bash
python setup_and_run.py --verbose --path /path/to/folder
```
### Interactive Prompts

- Malware Detection: When a potential malware file is detected, you’ll be asked whether you want to quarantine or delete the file.
- Verbose Mode: Displays details about each file being scanned. Enable verbose mode by entering “yes” when prompted.

### Additional Details

- Malware Signature File: The signatures.txt file contains a list of known malware MD5 hashes. You should update this file regularly to ensure accurate detection, as new malware signatures become available.
- Quarantine: Detected malware files can be moved to a designated quarantine folder for further analysis.

### Disclaimer

This tool uses a signature-based detection method, which is not foolproof. It may not detect all types of malware, especially new or unknown ones. For comprehensive security, use this tool alongside other malware detection solutions.

### Contribution

If you'd like to contribute to MalwareWatchDog, feel free to fork the repository, make your changes, and submit a pull request.

