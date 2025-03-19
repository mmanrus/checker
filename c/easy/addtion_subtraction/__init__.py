import check50

@check50.check()
def exists():
     check50.exists("addition_subtraction.c")
     
@check50.check(exists)  # Mark 'compiles' as a check that depends on 'exists'
def compiles():
     check50.c.compile("addition_subtraction.c")
     
@check50.check(compiles)
def checkFunctions():
     check50.run("./addition_subtraction").stdin("12 34").stdout(46).exit(0)