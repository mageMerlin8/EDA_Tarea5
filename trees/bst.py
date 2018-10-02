import networkx as nx
import matplotlib.pyplot as plt

class NodeB:
    def __init__(self, dato, right=None, left=None):
        self.dato = dato
        self.right = right
        self.left = left

    def __lt__(self, other):
        return self.dato <  other.dato
    def __le__(self, other):
        return self.dato <= other.dato
    def __eq__(self, other):
        return self.dato == other.dato
    def __gt__(self, other):
        return self.dato >  other.dato
    def __ge__(self, dato):
        return self.dato >= other.dato

    def getHeight(self, height = 0):
        if(self.right is None and self.left is None):
            return height
        elif(self.right is not None and self.left is not None):
            return max([self.right.getHeight(height + 1), self.left.getHeight(height + 1)])
        elif(self.right is not None):
            return self.right.getHeight(height + 1)
        else:
            return self.left.getHeight(height + 1)

    def nodeDict(self):
        if(self.left is None and self.right is None):
            return {}
        elif(self.left is None):
            return {str(self.dato):{str(self.right.dato):{}}}
        elif(self.right is None):
            return {str(self.dato):{str(self.left.dato):{}}}
        else:
            return {str(self.dato):{str(self.left.dato):{}, str(self.right.dato):{}}}

    def dataFrameMe(self):
        resp = {}
        if(self.right is not None):
            resp.update(self.right.dataFrameMe())
        if(self.left  is not None):
            resp.update(self.left.dataFrameMe())
        resp.update(self.nodeDict())
        return resp

    def __str__(self, level=0):
        resp = "\t" * level + "nivel: " + str(level) + " dato:" + str(self.dato) + "\n"

        if(self.right is not None):
            resp += "\t" * (level) + "Nodo Derecho  : \n" + self.right.__str__(level+1) + "\n"
        if(self.left is not None):
            resp += "\t" * (level) + "Nodo Izquierdo: \n" + self.left.__str__(level+1)

        return resp

class ArbolB:
    def __init__(self, root = None):
        self.root = root

    def draw(self):
        plt.clf()
        myDict = self.root.dataFrameMe()
        grafo = nx.Graph(myDict)
        profundidades = {}
        listaProf = []
        for nodo in grafo.nodes():
            nodoInfo = self.find(int(nodo))
            profundidad = len(nodoInfo['pasos'])
            listaProf.append(profundidad)
            profundidades[nodo] = profundidad
        nx.set_node_attributes(grafo, profundidades, 'depth')
        nx.draw_kamada_kawai(grafo, with_labels = True, node_size=1500,
                            node_color = listaProf,
                            cmap = plt.cm.Blues,
                            vmax = max(listaProf)+1)

    def outputTreeImage(self, file):
        if(self.root is None):
            plt.clf()
        else:
            self.draw()
        plt.savefig(file, dpi = 300)

    def find(self, dato):
        return self.__findR(dato, self.root, [])

    def __findR(self, dato, currentNode, resp=[], pastNode = None):
        if(currentNode is None): return False
        if(currentNode.dato == dato): return {'pasos':resp, 'nodo':currentNode, 'nodoAnt':pastNode}

        if(currentNode.dato < dato):
            resp.append('r')
            return self.__findR(dato, currentNode.right, resp = resp, pastNode=currentNode)
        elif(currentNode.dato > dato):
            resp.append('l')
            return self.__findR(dato, currentNode.left, resp = resp, pastNode=currentNode)

    def findPrev(self, nodo):
        if(nodo.right is None): return None
        else:
            nodo = nodo.right
            while(nodo.left is not None):
                nodo = nodo.left
        return nodo

    def insert(self, dato):
        newNode = NodeB(dato)
        if(self.root is None):
            self.root = newNode
            return True
        elif(self.root < newNode):
            if(self.root.right is not None):
                return self.insertR(newNode, self.root.right)
            else:
                self.root.right = newNode
                return True

        elif(self.root > newNode):
            if(self.root.left is not None):
                return self.insertR(newNode, self.root.left)
            else:
                self.root.left = newNode
                return True
        else:
            return False

    def insertR(self, newNode, treeNode):

        if(treeNode < newNode):
            if(treeNode.right is None):
                treeNode.right = newNode
                return True
            else:
                return self.insertR(newNode, treeNode.right)
        elif(treeNode > newNode):
            if(treeNode.left is None):
                treeNode.left = newNode
                return True
            else:
                return self.insertR(newNode, treeNode.left)
        else:
            return False

    def delete(self, dato):
        info = self.find(dato)
        if(info):#Si se encontro el dato a quitar
            if((info['nodo'].left is None) and (info['nodo'].right is None)):#El nodo a quitar no tiene hijos
                if(info['pasos']==[]): self.root = None #Es la raíz
                elif(info['pasos'][-1] == 'r'): info['nodoAnt'].right = None
                elif(info['pasos'][-1] == 'l'): info['nodoAnt'].left = None

            elif(info['nodo'].left is not None and info['nodo'].right is not None):#el nodo a quitar tiene 2 hijos
                prev = self.findPrev(info['nodo'])
                info['nodo'].dato = prev.dato      #cambias el valor del nodo que vas a quitar por el valor siguiente
                newRight = ArbolB(info['nodo'].right) #creas una nueva rama para reemplazar el lado derecho de tu nodo
                newRight.delete(prev.dato) #borras el nodo del dato que usaste para reemplazar el nodo a eliminar
                info['nodo'].right = newRight.root

            else: # solamente tiene un hijo
                if(info['pasos']==[]):
                    self.root = info['nodo'].right or info['nodo'].left #Es la raíz
                elif(info['pasos'][-1] == 'r'):
                        info['nodoAnt'].right = info['nodo'].right or info['nodo'].left
                elif(info['pasos'][-1] == 'l'):
                        info['nodoAnt'].left = info['nodo'].right or info['nodo'].left
            return True
        else:
            print('Se intentó borrar un nodo no existente')
            return False

    def __str__(self):
        return "Árbol: " + str(self.root)

    def clear(self):
        self.root = None
