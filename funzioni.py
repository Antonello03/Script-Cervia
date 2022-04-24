#funzioni presenti in questo codice

# isPrime(n) --- Verifica se n è primo
# MCD(a,b) --- restituisce il MCD fra a e b
# mcm(a,b) --- restituisce il mcm fra a e b
# divisori(n) --- restituisce i divisori di n in una list
# divisoriMultipli(n,x) --- restituisce i divisori multipli di x di un numero n
# sommaCifre(n) --- somma le cifre di un numero
# sommaElementiList(l) --- restituisce la somma di tutti gli elementi di l
# sommaElementiListMultipli(l,x) --- restituisce la somma di tutti gli elementi di l multipli di x
# dioFanto(x,y,ris) --- restituisce una combinazione di i e j che soddisfa (a*i + b*j == ris)
# allDioFanto(x,y,ris) --- restituisce tutte le combinazioni di i e j (con i e j <= 1000) che soddisfano (a*i + b*j == ris)

#DEFINIZIONE FUNZIONI

#se n è primo restituisce True, altrimenti False
def isPrime(n):
    for i in range (2,n):
        if (n%i == 0):
            return False
    return True

#restituisce una List con i divisori di n
def divisori(n):
    div = []
    for i in range (1,n+1):
        if(n%i == 0):
            div.append(i)
    return div

#restituisce il numero di divisori multipli di x di un numero n
def divisoriMultipli(n,x = 1):
    div = []
    if (x < n):
        for i in range (x, n+1, x):
            if(n % i == 0):
                div.append(i)
        return div
    else:
        print("Valore non valido (n deve essere maggiore di x)")
        return

#somma le cifre di un numero
def sommaCifre(n):
    s = 0
    for c in str(n):
        s = s + int(c)
    return s

#restituisce la somma di tutti gli elementi di l
def sommaElementiList(l):
    s = 0
    for x in l:
        s = s + x
    return s

#restituisce la somma di tutti gli elementi di l multipli di x
def sommaElementiListMultipli(l,x):
    s = 0
    for e in l:
        if(e % x == 0):
            s = s + e
    return s

#restituisce il MCD fra a e b
def MCD(a,b):
    if (b == 0):
        return a
    else:
        return MCD(b, a % b)

#restituisce il mcm fra a e b
def mcm(a,b):
    return (a * b) / MCD (a , b)

#restituisce la combinazione più piccola di i e j che soddisfa (a*i + b*j == ris)
def dioFanto(x,y,ris):
    i=0
    j=0
    for i in range (0,1001):
        for j in range(0,1001):
            if (x*i + y*j == ris):
                return i,j

#restituisce tutte le combinazioni di i e j (con i e j < 1000) che soddisfano (a*i + b*j == ris)
def allDioFanto(x,y,ris):
    i=0
    j=0
    div = []
    for i in range (0,1001):
        for j in range(0,1001):
            if (x*i + y*j == ris):
                div.append((i,j))
    return div