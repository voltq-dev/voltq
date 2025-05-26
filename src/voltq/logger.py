from typing import Union

import logging
import sys

# Default logger for the Voltq library
logger = logging.getLogger("voltq")

# Always set the default level for the logger.
logger.setLevel(logging.INFO)

# Add a default handler ONLY if no handlers are already configured for THIS logger.
# This prevents duplicate handlers if the user configures logging globally.
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug("Default stream handler added to 'voltq' logger.") 

def set_level(level: Union[int, str]) -> None:
    """Helper function to set the logging level for the voltq logger."""
    logger.setLevel(level)