#from __future__ import division

import re
import pprint

my_input = ''
my_list = []
listx = []
listy = []

listx1 = []
listy1 = []

finalvertexlist = []

intersectionlist = []
vertexkeylist = []
vertexvaluelist = []
street = dict()


class Point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)

    def __str__(self):
        return repr(self)


class Line():
    def __init__(self, p1, p2):
        self.src = p1
        self.dst = p2

    def __repr__(self):
        return repr(self.src) + ' --> ' + repr(self.dst)


def Segment(x1, x2, xcoor, y1, y2, ycoor):
    if min(x1, x2) <= xcoor and xcoor <= max(x1, x2) and min(y1, y2) <= ycoor and ycoor <= max(y1, y2):
        return True
    else:
        return False


def intersect(l1, l2):
    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y
    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y

    xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
    xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    xcoor = xnum / xden

    ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    ycoor = ynum / yden

    if xden != 0 and yden != 0:
        xcoor = xnum / xden
        ycoor = ynum / yden
        if Segment(x1, x2, xcoor, y1, y2, ycoor) and Segment(x3, x4, xcoor, y3, y4, ycoor):
            if xcoor == -0.0:
                xcoor = 0.0
            if ycoor == -0.0:
                ycoor = 0.0

            return Point(xcoor, ycoor)

    if xden == 0 and yden == 0:
        xden_new = (x3 - x1) * (y2 - y4) - (x2 - x4) * (y3 - y1)
        xden_new_2 = (x4 - x1) * (y3 - y2) - (x3 - x2) * (y4 - y1)

        if xden_new == 0 and xden_new_2 == 0:
            return 'parellel'
    else:
        return None

while True:

    command = raw_input()
    pattern = re.compile(r'((^([acg]\ ))\"([a-zA-Z\ ]+)\"(\ \([+-?\d\,]+\))+)$')
    pattern1 = re.compile(r'((^([r]\ ))\"([a-zA-Z\ ]+)\")')
    pattern2 = re.compile(r'((^([cg]\ ))\"([a-zA-Z\ ]+)\"(\ \([+-?\d\,]+\))+)$')
    matches = pattern.match(command)
    matches1 = pattern1.match(command)
    matches2 = pattern2.match(command)

    if matches:
        my_input = my_input + " " + command
        my_list.append(command)


    elif matches1:
        command1 = raw_input()
        if command1 == 'g':
            print "remove street"

    elif matches2:
        command2 = raw_input()
        if command2 == 'g':
            print "change street"


    elif command == "g":
        # print "execute split function"
        # print my_input
        # print my_list

        for items in my_list:
            value = re.split("\"", items)
            # print value[1]
            # streetname.append(value[1])

            value1 = re.split(" ", value[2])
            value1.pop(0)
            # print value1

            street.update({value[1]: value1})  # value1 = [listtsss] value[1] = streetname weber sheber etc

        #pprint.pprint(street)
        key = street.keys()
        # print key

        for k in range(len(key) - 1):
            vertex = street[key[k]]  # vertex = list of items
            # print vertex
            for points in vertex:
                # print points
                val = re.split("\,", points)
                coordx = re.split("\(", val[0])
                coordx.pop(0)
                coordy = re.split("\)", val[1])
                coordy.pop(1)
                listx.append(coordx[0])
                listy.append(coordy[0])
            #print listx
            #print listy
            for k1 in range(k + 1, len(key)):
                vertex1 = street[key[k1]]  # vertex = list of items
                # print vertex1
                for point1 in vertex1:
                    # print point1
                    val1 = re.split("\,", point1)
                    coordx1 = re.split("\(", val1[0])
                    coordx1.pop(0)
                    coordy1 = re.split("\)", val1[1])
                    coordy1.pop(1)
                    # print coordx1[0]
                    # print coordy1[0]
                    listx1.append(coordx1[0])
                    listy1.append(coordy1[0])
                #print listx1
                #print listy1

                for i in range(len(listx) - 1):
                    P1 = Point(listx[i], listy[i])
                    P2 = Point(listx[i + 1], listy[i + 1])
                    L1 = Line(P1, P2)
                    #print L1
                    #print len(key)

                    for j in range(len(listx1) - 1):
                        P3 = Point(listx1[j], listy1[j])
                        P4 = Point(listx1[j + 1], listy1[j + 1])
                        L2 = Line(P3, P4)
                        #print L2

                        try:
                            result = intersect(L1, L2)
                            #print result

                            if result != None:
                                intersectionlist.append(str(result))

                                finalvertexlist.append(str(result))
                                finalvertexlist.append(str(P1))
                                finalvertexlist.append(str(P2))
                                finalvertexlist.append(str(P3))
                                finalvertexlist.append(str(P4))
                                # print finalvertexlist

                        except:
                            pass
                            #print "no intersection"

                listx1 = []
                listy1 = []
            listx = []
            listy = []  # l1 = Line(Point(coordx[0], coordy[0]), Point(coordx[1],coordy[1]))
        #print finalvertexlist
        variable = set(finalvertexlist)
        # print variable
        V = dict()
        print "V - "
        w = 1
        for z in variable:
            V.update({w: z}, )
            w = w + 1
        pprint.pprint(V)

        vertexvaluelist = V.values()
        #print vertexvaluelist
        vertexkeylist = V.keys()
        #print vertexkeylist
        var = list(set(intersectionlist))
        #print var
        print "E - "
        for a in range(len(vertexkeylist) - 1):
            for b in range(a + 1, len(vertexkeylist) - 1):
                for c in range(len(var)):
                    if (var[c] == V[vertexkeylist[a]]) or (var[c] == V[vertexkeylist[b]]):
                        #print vertexkeylist[a]
                        #print vertexkeylist[b]
                        #print "condition 1 satisfied"
                        #print "           "
                        print '<',vertexkeylist[a],',',vertexkeylist[b],'>'


    else:
        print "Error: Invalid format provided"



