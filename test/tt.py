import sys
sys.path.append("src/")

from transduction import tt

def is_a(x):
  return True if x=='a' else False

def testpred(*args):
  return '-'.join(args)

tt.register_pred(is_a)

print(tt.apply(([1, '*is-a', 'test', 0],
                ['1', ['testpred!', '2', '3'], '4']),
               ['z', 'a', 'a', 'a', 'test', 'x'],
               preds={'testpred':testpred}))