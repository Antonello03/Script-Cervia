def divisori(n):
    div = []
    for i in range (1,n+1):
        if n % i == 0:
            div.append(i)
    return div

print(len(divisori(144)) + len(divisori(1820)) + len(divisori(1485)))