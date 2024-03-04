import sys, subprocess

def check_packages(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
check_packages('pandas')