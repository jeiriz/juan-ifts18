#ordenar lista

#extend te lo agrega al final
#insert (i,num) inserta en indice o lista[1]=3
listaNum=[3,0,1,4,9,1,0,30]
listaNumOr=[]
listaLet=["c","a","d","s"]
max=0
min=400
pos=[]
ElemListaNumOr=len(listaNumOr)
ElemListaNum=len(listaNum)
	 #saber el mayor y el menor
# for f in listaNum:
# 	if f > max:
# 		max=f
# 	elif f <min:
# 		min=f
# listaNumOr.append(min)
while ElemListaNum!=ElemListaNumOr:
	min=400
	for i in listaNum:
		if i < min:
			min=i
	listaNum.remove(min)
	listaNumOr.append(min)
	ElemListaNumOr=len(listaNumOr)

print("Lista ordenada:",listaNumOr,"\n Elementos lista: ", ElemListaNumOr, "elementos listaNum", ElemListaNum)

		# 		pos=listaNum.index(i)
		# 		listaNum.pop(pos)
		# listaNumOr.append(min)		

			# if min not in listaNumOr:
			# 	listaNumOr.append(i)

# listaNumOr.append(max)
# print(max,min)

# listaNumOr[0]=min
# listaNumOr[ElemListaNumOr-1]=max
	





