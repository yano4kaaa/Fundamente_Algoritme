from voln import wave_algorithm
import timeit

def test_duplicate_vertices():
    """Тест с повторяющимися вершинами в разных ребрах."""
    edges = [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3)]
    start = timeit.default_timer()
    wave_algorithm(edges, 1, 2)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_duplicate_vertices())