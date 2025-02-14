def filterGreaterThan(threshold, **kwargs):
    filtered = {}
    for A, B in kwargs.items():
        if isinstance(B, (int, float)) and B > threshold:
            filtered[A] = B
    return filtered

