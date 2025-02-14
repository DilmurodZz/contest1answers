def typeBasedTransformer(**kwargs):
    transformed = {}
    for A, B in kwargs.items():
        if isinstance(B, (int, float)):
            transformed[A] = B ** 2
        elif isinstance(B, str):
            transformed[A] = B[::-1]
        elif isinstance(B, bool):
            transformed[A] = not B
        elif isinstance(B, (list, tuple)):
            transformed[A] = B[::-1]
        elif isinstance(B, dict):
            try:
                transformed[A] = {v: k for k, v in B.items()}
            except TypeError:
                transformed[A] = B
        else:
            transformed[A] = B
    return transformed

