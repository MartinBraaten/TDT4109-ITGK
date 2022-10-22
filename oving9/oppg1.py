__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#ostevirus

cheeses = {
'cheddar':
('A235-4','A236-1','A236-2','A236-3','A236-5','C31-1','C31-2'),
'mozarella':
('Q456-9','Q456-8','A234-5','Q457-1','Q457-2'),
'gombost':
('ZLAFS55-4','ZLAFS55-9','GOMBOS-7','A236-4'),
'geitost':
('SPAZ-1','SPAZ-3','EMACS45-0'),
'port salut':
('B15-1','B15-2','B15-3','B15-4','B16-1','B16-2','B16-4'),
'camembert':
('A243-1','A234-2','A234-3','A234-4','A235-1','A235-2','A235-3'),
'ridder':
('GOMBOS-4','B16-3'),
}


# a) Finn og skriv ut alle hylleplasser til osten "port salut"

print(cheeses['port salut'])


# b) Finn og skriv ut alle typer ost som potensielt er smittet av viruset
# Hyllene A234-235, B13-15 og C31 har blitt infisert



virus = ['A234','A235','B13','B14','B15','C31']
smitte_oster = []

value=[]
realvalue=[]
for key,val in cheeses.items():
    for i in range(len(val)):
        value=str(val)
        value=value.split("-")
        if i%2==0:
            realvalue.append(value[i])
#print(cheeses)


#print(value)

            if realvalue[i] in virus:
                if key not in smitte_oster:
                    smitte_oster.append(key)

print(smitte_oster)

"""
# c) Finn alle typer ost der ingen individ er smittet av viruset
# Skriv resultatet på formen <hylleplass> <ostetype>

for key,val in cheeses.items():
    ikke_smitte_oster = {}
    for i in range (len(val)):
        if val[i] not in virus:
            if key not in ikke_smitte_oster:
                ikke_smitte_oster[key]=val

print(ikke_smitte_oster)

"""