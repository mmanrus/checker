import check50


@check50.check()
def exists():
     check50.exists('fibonacci.py')
     
@check50.check(exists)
def check_valueerror():
    actual = check50.run("python3 fibonacci.py aa").stdout()  # No .stderr(), use .stdout()
    if "ERROR: Please enter an integer" not in actual:
        help = "ValueError: Be sure to convert argv[1] to int"
        raise check50.Mismatch("ERROR: Please enter an integer", actual, help=help)

@check50.check(exists)
def check_outofbounds():
    actual = check50.run("python3 fibonacci.py 1 2").stdout()  # No .stderr(), use .stdout()
    if "USAGE: python fibonacci.py (n)" not in actual:
        help = "Ensure the script only accepts a single argument: 'python fibonacci.py <n>'"
        raise check50.Mismatch("USAGE: python fibonacci.py (n)", actual, help=help)
