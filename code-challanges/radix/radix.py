"""
radix sort
"""

def radix_sort(list):
    queues = [Queue() for i in range(0,10)]
    max = max(list)
    iter = len(str(max))
    _pass = 1

    def _radix_sort(list):
        while _pass < iter + 1:
            output = []

            for j in range(len(list)):
                if list[j] % 10^_pass == j:
                    queues[j].enqueue(list[j])
            for q in queues:
                while q.front:
                    output.append(q.dequeue())
            _pass += 1

            return _radix_sort(output)
        return list


