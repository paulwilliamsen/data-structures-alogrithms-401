"""
radix sort
"""
from import Queue, Node

def radix_sort(list):
    queues = [Queue() for i in range(0,10)]
    max = max(list) if len(list) > 0 else 0
    iter = len(str(max))
    _pass = 0

    def _radix_sort(list):
        """
        
        """
        nonlocal iter
        nonlocal _pass

        while _pass < iter:
            output = []

            for j in list:
                q = j // (10 ** _pass) % 10
                queues[q].enqueue(j)

            for q in queues:
                while q.front:
                    output.append(q.dequeue())

            _pass += 1

            return _radix_sort(output)

        return list

    return _radix_sort(list)




