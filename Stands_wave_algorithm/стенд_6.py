from voln import wave_algorithm
import timeit

def test_mixed_type_vertices():
    """Тест с вершинами разных типов."""
    edges = [(1, 'A'), ('A', 2.5), (2.5, 1)]
    start = timeit.default_timer()
    wave_algorithm(edges, 0, 1)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_mixed_type_vertices())