#!/usr/bin/python

# --------------------------------------------------------------------------------------------------
#
# Imports.
#
# --------------------------------------------------------------------------------------------------
import os
import sys
import types

# --------------------------------------------------------------------------------------------------
#
# Global variables.
#
# --------------------------------------------------------------------------------------------------
__CURRENT_SCRIPT_FOLDER_NAME = os.path.basename(
    os.path.dirname(os.path.realpath(__file__))
)

# --------------------------------------------------------------------------------------------------
#
# Backwards compatibility mapping.
#
# --------------------------------------------------------------------------------------------------
__OLD_MODULE_FILE_NAME = "OldCode"
__OLD_CODE_MAPPING_SOURCES = f"""
import os

from {__CURRENT_SCRIPT_FOLDER_NAME}.RefactoredCode import RefactoredClass

def old_function_name():
    return RefactoredClass().public_function()
"""
__OLD_MODULE_TYPE = types.ModuleType(__OLD_MODULE_FILE_NAME)

# pylint: disable-next=exec-used
exec(__OLD_CODE_MAPPING_SOURCES, __OLD_MODULE_TYPE.__dict__)
sys.modules[f"{__CURRENT_SCRIPT_FOLDER_NAME}.{__OLD_MODULE_FILE_NAME}"] = (
    __OLD_MODULE_TYPE
)
