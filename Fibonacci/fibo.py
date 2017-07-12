import timeit

def fibo(n):
    '''function that returns the nth fibo number'''
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def time_execution(function, inputs):
    start = timeit.default_timer()
    result = function(inputs)
    run_time = timeit.default_timer() - start
    return result, run_time

def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]
    
def cached_fibo(n):
    '''function that returns the nth fibo number'''
    if n == 0 or n == 1:
        return n
    else:
        return (cached_execution(cache, cached_fibo, (n-1)) + cached_execution(cache, cached_fibo, (n-2)))


cache = {}
memo = [0, 1]
def list_cached_fibo(n):
    '''function returns the nth fibo number and stores wach in a dictionary'''
    if len(memo) <= n:
        memo.append(list_cached_fibo(n-1) + list_cached_fibo(n-2))
    return memo[n]

def write_to_file(txt_file, num_list):
    with open(txt_file, 'w') as f:
        for number in num_list:
            f.write('%s\n' % number)

def write_cache_to_file(cache, filename):
    with open(filename, 'w') as f:
        for entry in cache:
            f.write('%d\n' % cache[entry])
			
