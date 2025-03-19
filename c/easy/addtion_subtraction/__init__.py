import check50

@check50.check()
def exists():
     check50.exists("addition_subtraction.c")
     
@check50.check(exists)  # Mark 'compiles' as a check that depends on 'exists'
def compiles():
     check50.c.compile("addition_subtraction.c")
     
@check50.check(compiles)
def checkFunctions():
     result = check50.run("./addition_subtraction").stdin("12 34").stdout()
     
     expected_output = "Sum: 46\nDifference: -22"
    

     if expected_output not in result:
        help = "Error Running: Output should be:\nSum: 46\nDifference: -22"
        raise check50.Mismatch("ERROR: Please enter an integer", result, help=help)

@check50.check(compiles)
def checkAgain():
     result = check50.run("./addition_subtraction").stdin("20 25").stdout()
     expected_output = "Sum: 45\nDifference: -5"

     if expected_output not in result:
        help = "Error Running: Output should be:\nSum: 46\nDifference: -22"
        raise check50.Mismatch("ERROR: Please enter an integer", result, help=help)