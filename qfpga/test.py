import sys, inspect

def main(fn):
  if inspect.stack()[1][0].f_locals.get('__name__', None) == '__main__':
    exit(fn(sys.argv))

class Variable:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __repr__(self):
    return str(self)

  def __mul__(self, other):
    return Variable('{} * {}'.format(self, other))

  def __div__(self, other):
    return Variable('{} / {}'.format(self, other))

  def __add__(self, other):
    return Variable('( {} + {} )'.format(self, other))

  def __sub__(self, other):
    return Variable('( {} - {} )'.format(self, other))
    
  def __neg__(self):
    return Variable('- {}'.format(self))


def cache(fn):
  result = None
  def new(*args):
    nonlocal result
    if result is None:
      result = fn(*args)
    return result
  return new

def cache(fn):
  cached, result = False, None
  def new(*args):
    nonlocal result, cached
    if not cached:
      cached, result = True, fn(*args)
    return result
  return new
