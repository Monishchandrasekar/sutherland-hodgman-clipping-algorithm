from graphics import *
win=GraphWin("Sutherland-Hodgman_polygon_clipping",500,500)
win1=GraphWin("Output",500,500)
def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])

    def computeIntersection():
        dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
        dp = [s[0] - e[0], s[1] - e[1]]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0]
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3]

    outputList = subjectPolygon
    cp1 = clipPolygon[-1]

    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]

        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s = e
        cp1 = cp2
    return (outputList)
def polygon(points,prop_1,prop_2,output,wait):
    points_1=[]
    for i in range(len(points)):
        pt=Point(points[i][0],points[i][1])
        points_1.append(pt)
    poly=Polygon(*points_1)
    if prop_1==1:
        poly.setFill('Red')
    if prop_2==1:
        poly.setWidth(2)
    if output==1:
        poly.draw(win1)
    else:
        poly.draw(win)
    if wait==1:
        if output==1:
            win1.getMouse()
        else:
            win.getMouse()
def clicked(num):
    list=[]
    for i in range(num):
        pt=win.getMouse()
        q=pt.getX()
        w=pt.getY()
        e=(q,w)
        list.append(e)
        pt.draw(win)
    return list
num_subjectPolygon=int(input("Enter number of points for number of Subject Polygon : "))
subjectPolygon=clicked(num_subjectPolygon)
polygon(subjectPolygon,1,0,0,0)
num_clipPolygon=int(input("Enter number of pints for Clip Polygon : "))
clipPolygon=clicked(num_clipPolygon)
polygon(clipPolygon,0,1,0,1)
clipped=clip(subjectPolygon,clipPolygon)
polygon(clipPolygon,0,1,1,0)
polygon(clipped,1,0,1,1)


