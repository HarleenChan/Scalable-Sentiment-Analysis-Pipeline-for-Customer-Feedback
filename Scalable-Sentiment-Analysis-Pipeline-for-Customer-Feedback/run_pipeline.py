# run_pipeline.py

import subprocess

def run_script(script_name):
    print(f"\n Running {script_name}...\n")
    result = subprocess.run(['python', f'src/{script_name}'], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:\n", result.stderr)

if __name__ == "__main__":
    print("Launching Full Feedback Pipeline")

    scripts = ['ingest.py', 'clean.py', 'sentiment.py']

    for script in scripts:
        run_script(script)

    print("\n All steps completed successfully!")

