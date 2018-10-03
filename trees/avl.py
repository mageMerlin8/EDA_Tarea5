from trees.bst import *

class NodeAVL(NodeB):
    def __init__(self, nodo):
        NodeB.__init__(self, nodo.dato, right=nodo.right, left=nodo.left)
        self.fe = None
        self.fe = self.getFE()

    def getFE(self):
        if(self.right):
            r = self.right.getHeight()
        else:
            r = -1
        if(self.left):
            l = self.left.getHeight()
        else:
            l = -1
        self.fe = r - l
        return self.fe


class ArbolAVL(ArbolB):
    def __init__(self, root = None):
        ArbolB.__init__(self, root)
        if(root):
            self.toAvl(self.root)

    def find2(self, node = None, parent = None):
        if(not node): return self.find2(self.root, None)
        if(node.fe > 1):
            return {'node':node, 'parent':parent}
        else:
            if(node.left and node.right):
                return self.find2(node.right, node) or self.find2(node.left, node)
            elif(node.left):
                return self.find2(node.left, node)
            elif(node.right):
                return self.find2(node.right, node)
            else: return False

    def draw(self):
        plt.clf()
        myDict = self.root.dataFrameMe()
        grafo = nx.Graph(myDict)
        profundidades = {}
        listaProf = []
        labelsDict = {}
        for nodo in grafo.nodes():
            nodoInfo = self.find(int(nodo))
            profundidad = len(nodoInfo['pasos'])
            listaProf.append(profundidad)
            profundidades[nodo] = profundidad
            labelsDict[nodo] = nodo + ', fe:' + str(nodoInfo['nodo'].fe)
        nx.set_node_attributes(grafo, profundidades, 'depth')
        nx.draw_kamada_kawai(grafo, with_labels = True, node_size=1500,
                            node_color = listaProf,
                            cmap = plt.cm.Blues,
                            vmax = max(listaProf)+1,
                            labels = labelsDict)

    def leftRotate(self, node):
        new = node.right
        if new.left:
            node.right = new.left
        else:
            node.right = None
        new.left = node
        return new

    def rightRotate(self, node):
        new = node.left
        if new.right:
            node.left = new.right
        else:
            node.left = None
        new.right = node
        return new

    def rotaLL(self):
        self.calculaFes(self.root)
        node = self.find2(self.root, None)
        if(node and node['parent']):
            node['parent'].right = self.leftRotate(node['node'])
            print('arbol rotado: ')
            print(self.root)
        else:
            print('no se puede rotar arbol')

    def insertR(self, node, dato):
        #insercion normal con modificacion de fe
        if not node:
            new = NodeAVL(NodeB(dato))
            new.fe = None
            return new

        elif dato < node.dato:
            node.left = self.insertR(node.left, dato)
            if node.left.fe is None:
                node.left.fe = 0
                node.fe -= 1
            elif node.left.fe is not 0:
                node.fe -= 1

        elif dato > node.dato:
            node.right = self.insertR(node.right, dato)
            if node.right.fe is None:
                node.right.fe = 0
                node.fe += 1
            elif node.right.fe is not 0:
                node.fe += 1
        else:
            print('se intentó insertar un nodo que ya existe')
            return None

        if(node.fe > 1):
            if(node.right.fe is 1):
                node = self.leftRotate(node)
                node.fe = 0
                node.left.fe = 0

            elif(node.right.fe is 0):
                node = self.leftRotate(node)
                node.fe = -1
                node.left.fe = 1

            elif(node.right.fe is -1):
                feY = node.right.left.fe
                node.right = self.rightRotate(node.right)
                node = self.leftRotate(node)
                node.fe = 0
                if feY is 0:
                    node.left.fe = 0
                    node.right.fe = 0
                elif feY is 1:
                    node.left.fe = -1
                    node.right.fe = 0
                elif feY is -1:
                    node.left.fe = 0
                    node.right.fe = 1

        elif node.fe < -1 :
            if(node.left.fe is -1):
                node = self.rightRotate(node)
                node.fe = 0
                node.right.fe = 0
            elif(node.left.fe is 0):
                node = self.rightRotate(node)
                node.fe = 1
                node.right.fe = -1
            elif(node.left.fe is 1):
                feY = node.left.right.fe
                node.left = self.leftRotate(node.left)
                node = self.rightRotate(node)
                node.fe = 0
                if feY is 0:
                    node.left.fe = 0
                    node.right.fe = 0
                elif feY is -1:
                    node.left.fe = 0
                    node.right.fe = 1
                elif feY is 1:
                    node.left.fe = -1
                    node.right.fe = 0
        return node

    def insert(self, dato):
        resp = self.insertR(self.root, dato)
        if(resp):
            if resp.fe is None:
                resp.fe = 0
            self.root = resp
            return True
        else:
            return False

    def calculaFes(self, node):
        node.fe = node.getFE()
        if(node.left):
            self.calculaFes(node.left)
        if(node.right):
            self.calculaFes(node.right)

    def isBalanced(self, node = None):
        if(not node):
            return self.isBalanced(self.root)
        if(node.fe < 2 and node.fe > -2):
            if(node.right and node.left):
                return self.isBalanced(node.right) and self.isBalanced(node.left)
            elif(node.right):
                 return self.isBalanced(node.right)
            elif(node.left):
                 return self.isBalanced(node.left)
            else:
                return True
        else:
            return False

    def toAvl(node):
        if(node.left):
            self.toAvl(node.left)
        if(node.right):
            self.toAvl(node.right)
        node = NodeAVL(node)
