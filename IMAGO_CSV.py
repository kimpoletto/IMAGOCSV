

import os
import pandas as pd

#x = 276
for x in range(124, 126):
    workspace = 'Visconde'
    furo = f'PSO-VISD-DH{x:05d}'
    
    diretorio = f'C:\\Users\\c0624150\\OneDrive - Vale S.A\\Pictures\\IMAGO\\GIRAR\\{furo}'
    
    
    
    lista = []
    cont = 0
    
    for root, dirs, files in os.walk(diretorio):
        for arquivo in files:
         
            cont += 1
            
    #caso só tenha uma caixa na foto           
    
            if arquivo.lower().count('bx') == 1:
                
                a = arquivo.split('_')
                print(a)
                b = a[2].replace('cx','bx')
               # c = a[3].replace('cx','bx')
                d = a[3].replace('m','')
                e = d.replace(',','.')
                f = a[4].replace('m','')
                g = f.replace(',','.')
                h = a[-1].replace('wet.jpg','Wet')
                i = h.replace('dry.jpg','Dry')
                j = i.replace('molhada.JPG','Wet')
                l = j.replace('seca.JPG','Dry')
                
                lista.append([f'{root}\{arquivo}',furo,b,b,e,g,l,'Core Boxes',workspace,'Drilling'])
                
    #fotos com duas caixas
                
            else:        
                a = arquivo.split('_')
                print(a)
                b = a[2].replace('cx','bx')
                c = a[3].replace('cx','bx')
                d = a[4].replace('m','')
                e = d.replace(',','.')
                f = a[5].replace('m','')
                g = f.replace(',','.')
                h = a[-1].replace('wet.jpg','Wet')
                i = h.replace('dry.jpg','Dry')
                j = i.replace('molhada.JPG','Wet')
                l = j.replace('seca.JPG','Dry')
                
                lista.append([f'{root}\{arquivo}',furo,b,c,e,g,l,'Core Boxes',workspace,'Drilling'])
                
    print(cont)
    
    df = pd.DataFrame(data=lista)
    df.columns = ['FilePath','HOLEID','Box1','Box2','FROM','TO','ImageType','ImageryType','Workspace','Dataset']
    df.to_csv(f'C:\\Nova pasta\\Documents\\CSV IMAGO\\{furo}.csv', index=False)
