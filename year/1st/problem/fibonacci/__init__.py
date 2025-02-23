import check50


@check50.check()
def exists():
     check50.exists('fibonacci.py')
     
@check50.check(exists)
def print_fib():
     actual = check50.run("python3 fibonacci.py 5").stdout()
     if "5" not in actual and "3" in actual:
          help = "Be sure to start the sequence at 1"
          raise check50.Missing("5", actual, help=help)
@check50.check(exists)
def check_valueerror():
     actual = check50.run('python3 fibonnacci.py aa').stderr()# prints to sys.exit or ValueError
     if 'ERROR: Please enter an integer' not in actual:
          help = "ValueError: Be sure to convert argv[1] to int"
          raise check50.Mismatch('ERROR: Please enter an integer', actual, help=help)
@check50.check(exists)
def check_outofbounds():
     actual = check50.run('python3 fibonnacci.py 1 2').stderr() # prints to sys.exit or ValueError
     if 'USAGE: python fibonacci.py (n)' not in actual:
          help = "Ensure the script only accepts a single argument: 'python fibonacci.py <n>'"
          raise check50.Mismatch('USAGE: python fibonacci.py (n)', actual, help=help)
     