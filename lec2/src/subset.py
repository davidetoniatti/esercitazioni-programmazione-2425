#!/usr/bin/env python

def is_subset(l1,l2):
    for e1 in l1:
        matched = False
        for e2 in l2:
            if e1 == e2:
                matched = True
                """
                l'istruzione *break* interrompe il ciclo nel quale viene chiamata:
                in questo caso, se e1 = e2, l'operazione break interrompe
                il ciclo for più interno (for e2 in l2)
                """
                break 
        """
        se e1 non è uguale a nessun elemento di l2,
        allora l2 non contiene tutti gli elementi di l1
        quindi è inutile controllare gli altri elementi di l1,
        ritorna False
        """
        if not matched:
            return False
    """
    se il ciclo più esterno termina, allora tutti gli elementi di l1
    sono in l2, ritorna True
    """
    return True
