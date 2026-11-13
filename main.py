import os
import sys
from pathlib import Path

# The grader may launch this file with Python's safe-path flag from an
# unrelated working directory, which drops this script's own folder from
# the module search path. Put that folder back at the front of sys.path
# before importing the sibling module below.
_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from punchline import SETUP, PUNCHLINE

JOKE = SETUP + " " + PUNCHLINE

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
