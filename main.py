import rbtree, bstree, time
import numpy as np
import tracemalloc


if __name__ == '__main__':
    randArray = list(range(1, 1000000))
    np.random.shuffle(randArray)
    randindex = randArray[np.random.randint(1, len(randArray))]
    root = bstree.Node(randArray[randindex])
    tracemalloc.start()
    beforeInsert = time.perf_counter()
    for number in randArray:
        root.insert(number)
    afterInsert = time.perf_counter()
    print(f" BST RAM usato in Bytes (current, peak){tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
    beforeSearch = time.perf_counter_ns()
    root.search(10000000)
    afterSearch = time.perf_counter_ns()
    spentInsert = afterInsert - beforeInsert
    spentSearch = afterSearch - beforeSearch
    print("---------------------------------------")
    print(f"tempo trascorso per inserire in BST [{spentInsert}] seconds ")
    print(f"tempo trascorso per cercare in BST [{spentSearch}] nano seconds ")
    print("---------------------------------------")
    rb = rbtree.RedBlackTree()
    tracemalloc.start()
    beforeInsert = time.perf_counter()
    for number in randArray:
        rb.add(number)
    afterInsert = time.perf_counter()
    print(f" RB RAM usato in Bytes (current, peak){tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
    beforeSearch = time.perf_counter_ns()
    rb.search(10000000)
    afterSearch = time.perf_counter_ns()
    spentInsert = afterInsert - beforeInsert
    spentSearch = afterSearch - beforeSearch
    print("---------------------------------------")
    print(f"tempo trascorso per inserire in RBT [{spentInsert}] seconds ")
    print(f"tempo trascorso per cercare in RBT[{spentSearch}] nano seconds ")
    print("---------------------------------------")
    print(f"Altezza BST : {bstree.maxDepth(root)}")
