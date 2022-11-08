import networkx as nx
import matplotlib.pyplot as plt


def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)


if __name__ == '__main__':

    
    G = nx.DiGraph()
    
    # Agrega nodos/edge pairs
    agregar_arista(G, "0", "3", 11.3)
    agregar_arista(G, "0", "2", 15.2)
    agregar_arista(G, "0", "6",17.4)

    agregar_arista(G, "1", "2", 14.1)
    agregar_arista(G, "1", "6", 15.3)
    
    
    agregar_arista(G, "2", "6", 2.3)
    agregar_arista(G, "2", "3", 3.3)
    
    agregar_arista(G, "3", "7", 8)
    agregar_arista(G, "3", "5", 13)
    
    agregar_arista(G, "4", "5", 8.6)
    agregar_arista(G, "4", "9", 15)
  
    agregar_arista(G, "5", "7", 7.2) 
     
    agregar_arista(G, "7", "9", 16)
    agregar_arista(G, "7", "8", 17.7) 
     
    agregar_arista(G, "8", "9", 24.8) 
   
 

    # dibuja el networ
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo con Distritos del Peru")
    plt.show()
