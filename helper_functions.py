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


def browser_simp(x):
    """
    Simplifies brower desciptions.

    Args:
        x: value in the id_31 column

    Returns:
        'chrome', 'safari', 'ie', 'edge',
            'firefox', 'samsung browser, and 'other'
    """
    try:
        if "chrome" in x:
            return "chrome"
        elif "safari" in x:
            return "safari"
        elif "ie " in x:
            return "ie"
        elif "edge" in x:
            return "edge"
        elif "firefox" in x:
            return "firefox"
        elif "samsung browser" in x:
            return "samsung browser"
        else:
            return "other"
    except TypeError:
        return None
