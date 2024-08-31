import igraph as ig

g = ig.Graph.Read_GML('teoria-dos-grafos\karate.gml')

ig.summary(g)

lista_k = g.degree()

# número de nós
N = len(lista_k)
print('Número de nós: ', N)

# número de links
L = int( sum(lista_k) / 2)
print('Número de links: ', L)

# grau médio
k = (2 * L) / N
print('Grau médio: ', k)

# número máximo possivel de arestas
L_max = int((N * ( N - 1) ) / 2)
print('Número máximo de links possiveis: ', L_max)

# Calculo diâmetro
lista_d = g.distances()

d_max = 0
for i in range(len(lista_d)):
    if max(lista_d[i]) > d_max:
        d_max = max(lista_d[i])

print('Diâmetro: ', d_max)

