def Torres_hanoi(n, torre_inicial, torre_auxiliar, torre_final):
    if n==1:
        print("Torre",torre_inicial+" ===> a Torre "+torre_final)
    else:
        Torres_hanoi(n-1, torre_inicial, torre_final, torre_auxiliar)
        print("Torre",torre_inicial+" ===> a Torre "+torre_final)
        Torres_hanoi(n-1, torre_auxiliar, torre_inicial, torre_final)
