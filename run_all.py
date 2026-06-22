"""
Run every exercise file in warmup/, drill/, and simulation/.

    python run_all.py

Each file runs on its own and prints its own pass/fail lines. Use this
to see at a glance which exercises are still failing.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDERS = ["warmup", "drill", "simulation"]


def main():
    for folder in FOLDERS:
        path = os.path.join(HERE, folder)
        if not os.path.isdir(path):
            continue
        files = sorted(f for f in os.listdir(path)
                       if f.endswith(".py") and f != "testkit.py")
        print("=" * 50)
        print(folder.upper())
        print("=" * 50)
        for f in files:
            print(f"\n[{folder}/{f}]")
            subprocess.run([sys.executable, os.path.join(path, f)])


if __name__ == "__main__":
    main()
