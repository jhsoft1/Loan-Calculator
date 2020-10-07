import math
from sys import exit
from argparse import ArgumentParser


def print_no_cr(*arg, sep='', end='', file=None, flush=False):
    print(*arg, sep=sep, end=end, file=file, flush=flush)


parser = ArgumentParser()
parser.add_argument("-t", "--type", dest="type")
parser.add_argument("-pr", "--principal", dest="principal")
parser.add_argument("-pe", "--periods", dest="periods")
parser.add_argument("-i", "--interest", dest="interest")
parser.add_argument("-pa", "--payment", dest="payment")
args = parser.parse_args()
v = vars(args)
n_args = sum([1 for a in v.values() if a])
typ = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
# print(typ, principal, periods, interest, payment, n_args)
if typ != "annuity" and typ != "diff":
    print("Incorrect parameters")
    exit(1)
if typ == "diff" and payment is not None:
    print("Incorrect parameters")
    exit(1)
if interest is None:
    print("Incorrect parameters")
    exit(1)
else:
    interest = float(interest)
    if interest < 0:
        print("Incorrect parameters")
        exit(1)
i = interest / 12 / 100
if n_args != 4:
    print("Incorrect parameters")
    exit(1)
if typ == "annuity":
    if periods is None:
        P = float(principal)
        A = float(payment)
        if P < 0 or A < 0:
            print("Incorrect parameters")
            exit(1)
        n = math.ceil(math.log(A / (A - i * P), 1 + i))
        years = n // 12
        months = n % 12
        print_no_cr("It will take ")
        if years != 0:
            print_no_cr(str(years)),
            print_no_cr(" year" if years == 1 else " years"),
        if years != 0 and months != 0:
            print_no_cr(" and "),
        if months != 0:
            print_no_cr(str(months)),
            print_no_cr(" month" if months == 1 else " months"),
        print(" to repay this loan!")
    elif payment is None:
        P = float(principal)
        n = float(periods)
        if P < 0 or n < 0:
            print("Incorrect parameters")
            exit(1)
        A = math.ceil(P * i * (1 + i) ** n / ((1 + i) ** n - 1))
        print("Your annuity payment = " + str(A) + "!")
    elif principal is None:
        A = float(payment)
        n = float(periods)
        if A < 0 or n < 0:
            print("Incorrect parameters")
            exit(1)
        P = math.floor(A / (i * (1 + i) ** n / ((1 + i) ** n - 1)))
        print("Your loan principal = " + str(P) + "!")
    print("Overpayment = " + str(math.ceil(A * n - P)))
elif typ == "diff":
    P = float(principal)
    n = int(periods)
    total = 0
    if P < 0 or n < 0:
        print("Incorrect parameters")
        exit(1)
    for m in range(n):
        payment = math.ceil(P / n + i * (P - P * m / n))
        total += payment
        print_no_cr("Month ", str(m + 1))
        print(": payment is ", str(payment))
    print()
    print("Overpayment = " + str(math.ceil(total - P)))
