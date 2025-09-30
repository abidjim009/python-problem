# Profile a simple function
import cProfile

def sum():
    print(1,3)
cProfile.run('sum()')