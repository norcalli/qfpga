import sys, inspect

def main(fn):
  if inspect.stack()[1][0].f_locals.get('__name__', None) == '__main__':
    exit(fn(sys.argv))
