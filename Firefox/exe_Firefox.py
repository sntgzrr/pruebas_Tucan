import csv
from CP001.Positivo import test_cP001P
from CP001.Negativo import test_cP001N
from CP003.Positivo import test_cP003P
from CP003.Negativo import test_cP003N
from CP007.Positivo import test_cP007P
from CP007.Negativo import test_cP007N
from CP008.Positivo import test_cP008P
from CP008.Negativo import test_cP008N
from CP009.Positivo import test_cP009P
from CP009.Negativo import test_cP009N
from CP010.Positivo import test_cP010P
from CP010.Negativo import test_cP010N
from CP011.Positivo import test_cP011P
from CP011.Negativo import test_cP011N

exe001p = test_cP001P.TestCP001P()
exe001n = test_cP001N.TestCP001N()
exe003p = test_cP003P.TestCP003P()
exe003n = test_cP003N.TestCP003N()
exe007p = test_cP007P.TestCP007P()
exe007n = test_cP007N.TestCP007N()
exe008p = test_cP008P.TestCP008P()
exe008n = test_cP008N.TestCP008N()
exe009p = test_cP009P.TestCP009P()
exe009n = test_cP009N.TestCP009N()
exe010p = test_cP010P.TestCP010P()
exe010n = test_cP010N.TestCP010N()
exe011p = test_cP011P.TestCP011P()
exe011n = test_cP011N.TestCP011N()

# CP001
exe001p.exeCP001P()
exe001n.exeCP001N()
# CP003
exe003p.exeCP003P()
exe003n.exeCP003N()
# CP007
exe007p.exeCP007P()
exe007n.exeCP007N()
# CP008
exe008p.exeCP008P()
exe008n.exeCP008N()
# CP009
exe009p.exeCP009P()
exe009n.exeCP009N()
# CP010
exe010p.exeCP010P()
exe010n.exeCP010N()
# CP010
exe011p.exeCP011P()
exe011n.exeCP011N()