"""
This document will hold all of the helper functions
for the fraud_prediction notebook.
"""


def tf_binary(x):
    """
    Turns a 'T' or 'F' string into binary.

    Args:
        x: a string of 'T' or 'F'

    Returns:
        Either 1 for 'T', 0 for 'F', or None
    """
    if x == "T":
        return 1
    elif x == "F":
        return 0
    else:
        return None


def nfound_binary(x):
    """
    Turns 'Found', 'NotFound', 'New', and 'Unknown' string into numerics.

    Args:
        x: a string of 'Found', 'NotFound', 'New', or 'Unknown'

    Returns:
        Either 1 for 'Found', 0 for 'New or 'NotFound',
            -1 for 'Unknown' or None
    """
    if x == "Found":
        return 1
    elif x == "NotFound":
        return 0
    elif x == "New":
        return 0
    elif x == "Unknown":
        return -1
    else:
        return None


def devtype_binary(x):
    """
    Turns 'desktop' and 'mobile' string into numerics.

    Args:
        x: a string of 'desktop' or 'mobile'

    Returns:
        Either 1 for 'desktop', 0 for 'mobile', or None
    """
    if x == "desktop":
        return 1
    elif x == "mobile":
        return 0
    else:
        return None
