import os
from pathlib import Path


from punchline import SETUP, PUNCHLINE

JOKE = SETUP + " " + PUNCHLINE

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
