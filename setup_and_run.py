import subprocess
import sys
import importlib

# List of required packages
REQUIRED_PACKAGES = ['requests']

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def check_and_install_packages():
    for package in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install(package)

def main():
    print("Checking and installing required libraries...")
    check_and_install_packages()
    
    # Now import and run the main malware detection tool
    import malware_watchdog
    malware_watchdog.main()

if __name__ == '__main__':
    main()
