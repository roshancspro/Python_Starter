from multiprocessing.pool import ThreadPool

def foo(word, number):
    print (word * number)
    #r[(word,number)] = number
    return number

words = ['hello', 'world', 'test', 'word', 'another test']
numbers = [1,2,3,4,5]
pool = ThreadPool(5)
results = []
for i in range(0, len(words)):
    results.append(pool.apply_async(foo, args=(words[i], numbers[i])))

pool.close()
pool.join()
results = [r.get() for r in results]
print(results)