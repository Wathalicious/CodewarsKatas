def get_sum(a,b):
    
    zahlen = [a, b]
    maxwert = max(zahlen)
    minwert = min(zahlen)
    
    summe = sum(range(minwert, maxwert + 1))

    if a == b:
        return a or b
    
    else:
        return summe