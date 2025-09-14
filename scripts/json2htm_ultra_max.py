#!/usr/bin/env python3
import sys
from pathlib import Path

# чтобы импортировать соседний файл
sys.path.insert(0, str(Path(__file__).parent))

from osint_harvester_max import main

if __name__ == "__main__":
    sys.exit(main())
