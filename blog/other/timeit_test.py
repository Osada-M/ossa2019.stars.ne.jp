import timeit

def bitCount(x):
    x -= ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x0000007f

loop = [1000, 1000]
tests = {'int.bit_count()' : f'[int.bit_count(x) for x in range({loop[0]})]',
         '自作の処理１' : f'[len([i for i in str(bin(x))[2:] if i == \'1\']) for x in range({loop[0]})]',
         '自作の処理２' : f'[len([i for i in str(bin(x))[2:] if i]) for x in range({loop[0]})]',
         '自作の処理３' : f'[bitCount(x) for x in range({loop[0]})]',
         '自作の処理４' : f'[str(bin(x))[2:].count(\'1\') for x in range({loop[0]})]'}

for t in tests.keys():
    print(f'{t}\t\t: ', timeit.timeit(tests[t], globals=globals(), number=loop[1]))

