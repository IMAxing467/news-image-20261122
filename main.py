"""Entry for make.fun bounty 'Sum up 22 November's world news in one image'.

Writes the news image to /output/entry.jpg. Deterministic: it copies the
same bundled bytes every run, with no network access.
"""

import os
import shutil
from pathlib import Path

SRC = Path(__file__).with_name("entry.jpg")
DST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.jpg"


def main() -> None:
    # Fail loudly if the bundled image is missing or over the 1 MiB cap,
    # instead of silently handing the gate a broken file.
    size = SRC.stat().st_size
    if size > 1024 * 1024:
        raise SystemExit(f"entry.jpg is {size} bytes, over the 1 MiB cap")
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"entry.jpg copied to {DST} ({size} bytes)")


if __name__ == "__main__":
    main()
