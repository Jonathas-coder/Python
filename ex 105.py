def notas (*n,sit=False):
    dic=dict()
    c=1
    while c < len(n):
       c+=1
    maior=max(n)
    menor=min(n)
    media=list()
    for k, v in enumerate(n):
        media.append(v)
    t=sum(media) / c
    dic={'total':c,'maior':maior,'menor':menor,'media':t }
    if sit == True:
        if t <=5:
            dic["sit"]=('Média baixa')
        if t >= 5 and t <= 7:
            dic["sit"]=('Média razoavel')
        if t >=7:
            dic["sit"] = 'Média boa'
    return dic



resp= notas(5,0,0,9,sit=True)
print(resp)