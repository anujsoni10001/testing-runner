import os
import platform
import sys
from datetime import datetime

def run_pipeline_test():
    print("=========================================")
    print("🚀 GITHUB ACTIONS SELF-HOSTED RUNNER TEST")
    print("=========================================")
    
    # 1. Print current execution time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Execution Time: {current_time}")
    
    # 2. Print operating system details to verify it ran on Windows
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {sys.version}")
    
    # 3. Print the directory where GitHub executed the script
    print(f"Working Directory: {os.getcwd()}")
    
    # 4. Optional: Print the GitHub user who triggered the push if available
    actor = os.getenv("GITHUB_ACTOR", "Local / Unknown")
    print(f"Triggered By GitHub User: {actor}")
    
    print("=========================================")
    print("✅ SUCCESS: Python script executed flawlessly!")
    print("=========================================")

if __name__ == "__main__":
    run_pipeline_test()
