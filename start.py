import os
import subprocess
import sys

#langue = "eng"
langue = os.getenv("LANGUE", "eng")

if langue == "eng":
    subprocess.run([sys.executable, "scripts/main_eng.py"])
else:
    subprocess.run([sys.executable, "scripts/main_fr.py"])