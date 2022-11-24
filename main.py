# process_yaml.py file
import numpy as numpy
import yaml
with open("ya.yaml",encoding="utf-8") as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
masOb=read_data['Objects']
a=False
while (a==False):
    print("\nОбъекты:")
    for i in range(len(masOb)):
        print(i+1," ",masOb[i])
    no =int(input("\nВведите номер объекта: "))-1

    masCn=read_data['Connection']

    Cn=[]

    for i in range(len(masCn)):
        if (masOb[no]==((masCn[i])['src']) or masOb[no]==((masCn[i])['dst'])):
            if (masCn[i])['type'] not in Cn:
                Cn.append((masCn[i])['type'])
    print("\nСвязи обьекта:")
    for i in range(len(Cn)):
        print(i+1," ",Cn[i])
    ns =int(input("\nВведите номер типа связи: "))-1

    for i in range(len(masCn)):
        if ((masOb[no]==((masCn[i])['src']) or masOb[no]==((masCn[i])['dst'])) and ( Cn[ns]==((masCn[i])['type']))  ):
            print('\n',masCn[i])
    f=input('\nВведите +, если хотите продолжить: ')
    if (f!="+"):
        a=True
print("\nКонец")


