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
     
     expected_sum = "Sum: 46"
     expected_difference = "Difference: -22"

     if result.match(expected_sum) and result.match(expected_difference) not in result:
        help = "Error Running "
        raise check50.Mismatch("ERROR: Please enter an integer", result, help=help)

@check50.check(compiles)
def checkAgain():
     result = check50.run("./addition_subtraction").stdin("20 25").stdout()
     expected_sum = "Sum: 45"
     expected_difference = "Difference: -5"
     result.match(expected_sum)
     result.match(expected_difference)
     if result.match(expected_sum) and result.match(expected_difference) not in result:
        help = "Error Running "
        raise check50.Mismatch("ERROR: Please enter an integer", result, help=help)
