#implement insertion sort with custom comparison functionality.

def insertion_sort(iterable,begin: int,end: int,cmp= lambda x,y: x<y) -> None:
    """End points inclusive in sort. cmp takes comparison function (default being "<")."""
    if not (begin>=0 and end<len(iterable)):
        raise IndexError
    for i in range(begin+1,end+1):
        j=i-1
        key=iterable[i]
        while j>=begin and cmp(key,iterable[j]):
            iterable[j+1]=iterable[j]
            j-=1
        iterable[j+1]=key
