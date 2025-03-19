import check50

@check50.check()
def exists():
    """Checks if addition_subtraction.c exists"""
    check50.exists("addition_subtraction.c")

@check50.check(exists)
def compiles():
    """Checks if addition_subtraction.c compiles successfully"""
    check50.run("gcc -o addition_subtraction addition_subtraction.c").exit(0)

@check50.check(compiles)
def checkFunctions():
    """Checks if addition and subtraction work correctly for 12 and 34"""
    result = check50.run("./addition_subtraction").stdin("12 34").stdout()

    expected_output = "Sum: 46\nDifference: -22\n"

    if expected_output not in result:
        raise check50.Mismatch(expected_output, result, help="Expected output does not match.")

@check50.check(compiles)
def checkAgain():
    """Checks if addition and subtraction work correctly for 20 and 25"""
    result = check50.run("./addition_subtraction").stdin("20 25").stdout()

    expected_output = "Sum: 45\nDifference: -5\n"

    if expected_output not in result:
        raise check50.Mismatch(expected_output, result, help="Expected output does not match.")
