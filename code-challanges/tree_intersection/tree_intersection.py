from hashtable.hashtable import HashTable

def tree_intersection(Bt1, Bt2):
    ht = HashTable()
    match_array = []

    def _tree_put(curr):
        
        if curr:
            ht.add(curr.data, curr.data)

            if curr.left:
                _tree_put(curr.left)
            if curr.right:
                _tree_put(curr.right)
    
    
    def _tree_check(curr):
        if curr:
            if ht.contains(curr.data):
                match_array.append(curr.data)
            if curr.left:
                _tree_check(curr.left)
            if curr.right:
                _tree_check(curr.right)
    
    _tree_put(Bt1.root)
    _tree_check(Bt2.root)
    return match_array