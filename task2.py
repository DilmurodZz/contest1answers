def typeBasedTransformer(**zaripov):
    trans = {}
    for A, B in zaripov.items():
        if isinstance(B, (int, float)):
            trans[A] = B ** 2
        elif isinstance(B, str):
            trans[A] = B[::-1]
        elif isinstance(B, bool):
            trans[A] = not B
        elif isinstance(B, (list, tuple)):
            trans[A] = B[::-1]
        elif isinstance(B, dict):
            try:
                trans[A] = {v: k for k, v in B.items()}
            except TypeError:
                trans[A] = B
        else:
            trans[A] = B
    return trans

