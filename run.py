#!/usr/bin/env python3
"""
Refract - AI Video Editor Launcher

This script provides an easy way to run the Refract AI video editor
from the organized project structure.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run the main application
try:
    from main import main  # type: ignore  # Dynamic import after path manipulation
except ImportError as e:
    print(f"Error importing main module: {e}")
    print("Make sure you're running this from the project root directory")
    sys.exit(1)

if __name__ == "__main__":
    # Run the main application
    main()