from voln import count_vertices
import timeit

def test_empty_input():
    edges = []
    start = timeit.default_timer()
    count_vertices(edges)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_empty_input())
        
