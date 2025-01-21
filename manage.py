#!/usr/bin/env python
import os
import sys
from pathlib import Path

# Get the absolute path to your project root
BASE_DIR = Path(__file__).resolve().parent

# Add the project root directory to Python path
sys.path.insert(0, str(BASE_DIR))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()