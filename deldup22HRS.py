import os
with os.scandir('G:/HRS/LRRBAF/') as entries:
    for entry in entries:
        inputdatei=open(entry,'r',encoding='utf-8')
        b=0
        c=0
        d=0
        b1=0
        c1=0
        d1=0
        y=0
        z=0
        y1=0
        z1=0
        for j,line in enumerate(inputdatei):
            if not "非数字" in line:
                if line.split()[1]=="22":
                    a=float(line.split()[2])
                    if a>25400000:
                        if a<25580000:
                            c1=c1+1
                            b1+=float(line.split()[5])
                            d1=float(b1/c1)
                            x1=float(line.split()[4])
                            if x1<0.55:
                                if x1>0.45:
                                    y1=y1+1
                            elif x1<0.80:
                                if x1>0.57:
                                    z1=z1+1
                            elif x1<0.43:
                                if x1>0.20:
                                    z1=z1+1
                        elif a<25919400:
                            if a>25663000:
                                c=c+1
                                b+=float(line.split()[5])
                                d=float(b/c)
                                x=float(line.split()[4])
                                if x<0.55:
                                    if x>0.45:
                                        y=y+1
                                elif x<0.80:
                                    if x>0.57:
                                        z=z+1
                                elif x<0.43:
                                    if x>0.20:
                                        z=z+1
                        elif a<26500000:
                            if a>25920000:
                                c1=c1+1
                                b1+=float(line.split()[5])
                                d1=float(b1/c1)
                                x1=float(line.split()[4])
                                if x1<0.55:
                                    if x1>0.45:
                                        y1=y1+1
                                elif x1<0.80:
                                    if x1>0.57:
                                        z1=z1+1
                                elif x1<0.43:
                                    if x1>0.20:
                                        z1=z1+1

        print(entry,str(d),y,z,c,str(d1),y1,z1,c1)
    inputdatei.close()