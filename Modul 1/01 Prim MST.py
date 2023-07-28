import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # Cetak MST yang disimpan pada list parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    # Mencari vertex dengan jarak terdekat
    # dari kumpulan vertex yang belum ada
    # dalam MST
    def minKey(self, key, mstSet):
        # Initialize nilai minimum
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Fungsi untuk mencari Prim MST dari graph saat ini
    def primMST(self):
        # Nilai key untuk menentukan weight minimum
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # List untuk menyimpan hasil MST
        key[0] = 0 # Pilih vertex pertama
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            # Ambil vertex dengan jarak minimum
            # dari vertex yang belum diproses
            u = self.minKey(key, mstSet)

            # Simpan ke dalam MST
            mstSet[u] = True

            # Update jarak dari vertex yang berdekatan
            # dengan vertex yang sedang diproses jika
            # jarak yang tersimpan saat ini lebih besar dari
            # jarak yang baru dan vertex belum ada dalam MST
            for v in range(self.V):

                # graph[u][v] bernilai tidak nol untuk vertex yang berdekatan
                # mstSet[v] bernilai False untuk vertex yang belum ada dalam MST
                # Update key jika graph[u][v] lebih kecil dari key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v] 
                    parent[v] = u

        self.printMST(parent)

if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
 
    g.primMST()