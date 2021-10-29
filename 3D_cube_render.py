import tkinter as tk
import numpy as np
import time


class Cube:
    def __init__(self, root, win_width=500, win_height=500, edge_size=100, color="white", bg="black", distance=3) -> None:
        self.root = root
        self.win_width = win_width
        self.win_height = win_height
        self.edge_size = edge_size
        self.color = color
        self.bg = bg

        self.distance = distance
        self.theta = 0
        self.speed = 0.01

        self.root.title("Cube 3d")
        self.canvas = tk.Canvas(
            self.root, bg=bg, height=self.win_height, width=self.win_width)
        self.canvas.pack(expand=True)

        self.cube = [
            [-1, -1, -1],
            [-1,  1, -1],
            [1,  1, -1],
            [1, -1, -1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1,  1, 1],
            [1,  1, 1]
        ]
        pass

    def projection(self, z):
        zz = 1 / (self.distance-z)
        return np.array([
            [zz, 0, 0],
            [0, zz, 0]
        ])
        pass

    def rotateX(self):
        return np.array([
            [1, 0, 0],
            [0, np.cos(self.theta), -np.sin(self.theta)],
            [0, np.sin(self.theta), np.cos(self.theta)]
        ])

    def rotateY(self):
        return np.array([
            [np.cos(self.theta), 0, np.sin(self.theta)],
            [0, 1, 0],
            [-np.sin(self.theta), 0, np.cos(self.theta)]
        ])

    def rotateZ(self):
        return np.array([
            [np.cos(self.theta), -np.sin(self.theta), 0],
            [np.sin(self.theta), np.cos(self.theta), 0],
            [0, 0, 1]
        ])

    def line(self, x1, y1, x2, y2, color='white'):
        return self.canvas.create_line(x1 + self.win_width/2, -1*y1 + self.win_height/2,
                                       x2 + self.win_width/2, -1*y2 + self.win_height/2,
                                       fill=color)
        pass

    def point(self, x, y, width=5, color='white'):
        return self.canvas.create_oval(x - width + self.win_width/2, -1*y + width + self.win_height/2,
                                       x + width + self.win_width/2, -1*y - width + self.win_height/2,
                                       fill=color)
        pass

    def show(self):
        try:
            while True:
                self.canvas.delete('all')
                edges = []
                for z in self.cube:
                    temp = self.rotateY()@z
                    temp = self.rotateX()@temp
                    temp = self.rotateZ()@temp
                    temp = self.projection(temp[2])@temp
                    temp = temp * 100
                    self.point(temp[0], temp[1])
                    edges.append(temp)

                self.line(edges[0][0], edges[0][1], edges[1][0], edges[1][1])
                self.line(edges[0][0], edges[0][1], edges[3][0], edges[3][1])
                self.line(edges[0][0], edges[0][1], edges[5][0], edges[5][1])
                self.line(edges[1][0], edges[1][1], edges[2][0], edges[2][1])

                self.line(edges[1][0], edges[1][1], edges[6][0], edges[6][1])
                self.line(edges[2][0], edges[2][1], edges[3][0], edges[3][1])
                self.line(edges[2][0], edges[2][1], edges[7][0], edges[7][1])
                self.line(edges[3][0], edges[3][1], edges[4][0], edges[4][1])

                self.line(edges[4][0], edges[4][1], edges[5][0], edges[5][1])
                self.line(edges[4][0], edges[4][1], edges[7][0], edges[7][1])
                self.line(edges[5][0], edges[5][1], edges[6][0], edges[6][1])
                self.line(edges[6][0], edges[6][1], edges[7][0], edges[7][1])

                self.theta += 0.03
                self.root.update()
                time.sleep(self.speed)
        except Exception as e:
            print(e)
    pass


def main():
    top = tk.Tk()
    cube = Cube(top)
    cube.show()


if __name__ == "__main__":
    main()
