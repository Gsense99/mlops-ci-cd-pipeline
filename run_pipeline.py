import os
import shutil
import subprocess
import yaml

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def get_accuracy():
    with open("reports/report.txt", "r") as f:
        content = f.read()
    return float(content.split("=")[1].strip())

def main():
    with open("pipeline.yml", "r") as f:
        pipeline = yaml.safe_load(f)

    threshold = pipeline["threshold"]

    print("\n===== ML CI/CD PIPELINE =====\n")

    for step in pipeline["steps"]:
        name = step["name"].upper()
        command = step["command"]

        try:
            if command == "validate":
                accuracy = get_accuracy()
                if accuracy >= threshold:
                    print(f"[{name}] PASSED - Accuracy = {accuracy:.2f}")
                else:
                    raise Exception(f"Accuracy {accuracy:.2f} is below threshold {threshold}")

            elif command == "deploy":
                os.makedirs("production", exist_ok=True)
                shutil.copy("model.joblib", "production/model.joblib")
                print(f"[{name}] Model copied to production/")

            else:
                run_command(command)
                print(f"[{name}] OK")

        except Exception as e:
            print(f"[{name}] FAILED")
            print(e)
            print("\n[PIPELINE] FAILED")
            return

    print("\n[PIPELINE] SUCCESS")

if __name__ == "__main__":
    main()