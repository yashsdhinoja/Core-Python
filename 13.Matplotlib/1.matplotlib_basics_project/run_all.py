"""Run every script one after another:  python run_all.py   (add --no-show to only save images)"""
import runpy
from pathlib import Path

for script in sorted(Path(__file__).parent.glob("0*.py")):
    print(f"\n=== {script.name} ===")
    runpy.run_path(str(script), run_name="__main__")
