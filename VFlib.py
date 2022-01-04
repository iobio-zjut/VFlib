
'''

'''

import os
import math
import shutil
from Bio import PDB

def out_hhr6_21():
    divided_hhm = "/iobio/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        frag_hhr = divided_hhm + lis + "/" + "frag_hhr/"
        position = []
        flag = False
        names = os.listdir(frag_hhr)
        for name in names:
            flag = False
            name = name.split('_')
            for j in position:
                if name[0] == j:
                    flag = True
            if not flag:
                position.append(name[0])
        out_hhr = divided_hhm + lis + "/" + "out_hhr" + "/"
        print(position)
        for p in position:
            position_name = out_hhr + p + ".hhr"
            f = open(position_name, 'w')
            for name in names:
                path_hhr = frag_hhr + name
                name = name.split('_')
                if name[0] == p:
                    num = ''
                    flag_frag = False
                    with open(path_hhr, 'r')as r:
                        for line in r.readlines():
                            line = line.strip()
                            line1 = line.split()
                            if len(line1) >= 2:
                                if line1[0] == 'No' and line1[1] == '1':
                                    flag_frag = False
                                    f.write(num)
                                if flag_frag:
                                    num = num + line + '\n'
                                if line1[0] == 'No' and line1[1] == 'Hit':
                                    flag_frag = True
                    r.close()
            f.close()
    pass

def out_hhr3():
    divided_hhm = "/home/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        frag_hhr = divided_hhm + lis + "/" + "frag_hhr3/"
        position = []
        flag = False
        names = os.listdir(frag_hhr)
        for name in names:
            flag = False
            name = name.split('_')
            for j in position:
                if name[0] == j:
                    flag = True
            if not flag:
                position.append(name[0])
        out_hhr = divided_hhm + lis + "/" + "out_hhr3" + "/"
        print(position)
        for p in position:
            position_name = out_hhr + p + ".hhr"
            f = open(position_name, 'w')
            for name in names:
                path_hhr = frag_hhr + name
                name = name.split('_')
                if name[0] == p:
                    num = ''
                    flag_frag = False
                    with open(path_hhr, 'r')as r:
                        for line in r.readlines():
                            line = line.strip()
                            line1 = line.split()
                            if len(line1) >= 2:
                                if line1[0] == 'No' and line1[1] == '1':
                                    flag_frag = False
                                    f.write(num)
                                if flag_frag:
                                    num = num + line + '\n'
                                if line1[0] == 'No' and line1[1] == 'Hit':
                                    flag_frag = True
                    r.close()
            f.close()
    pass

def out_frag6_21():
    divided_hhm = "/home/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        out_hhr = divided_hhm + lis + "/" + "out_hhr" + "/"
        out_frag = divided_hhm + lis + "/" + "out_frag" + "/"
        names = os.listdir(out_hhr)
        for name in names:
            in_file = out_hhr + name
            out_file = out_frag + name
            f = open(out_file, 'w')
            data = []
            name11 = []
            prob = []
            lenth = []
            start = []
            end = []
            with open(in_file, 'r') as r:
                for line in r.readlines():
                    line1 = line.split()
                    m = len(line1)
                    line2 = line1[len(line1) - 2].split('-')
                    line5 = line1[len(line1) - 3].split('-')
                    index = 0
                    index_n = 0
                    same_name = []
                    n = False
                    for i in name11:
                        if i == line1[1]:
                            n = True
                            same_name.append(index_n)
                        index_n = index_n + 1
                    if n:
                        for i in same_name:
                            index = int(i)
                            if line5[0] == "1":
                                if int(end[index]) < int(line2[0]) or int(start[index]) > int(line2[1]):
                                    flag_sss = True
                                    for j in same_name:
                                        index = int(j)
                                        if int(end[index]) > int(line2[0]) or int(start[index]) < int(line2[1]):
                                            flag_sss = False
                                    if flag_sss and float(line1[len(line1) - 4]) > 5:
                                        data.append(line)
                                        name11.append(line1[1])
                                        prob.append(line1[len(line1) - 9])
                                        lenth.append(line1[len(line1) - 4])
                                        start.append(line2[0])
                                        end.append(line2[1])
                                else:
                                    if float(prob[index]) == float(line1[len(line1) - 9]):
                                        if int(lenth[index]) > int(line1[len(line1) - 4]):
                                            data[index] = line
                                            name11[index] = line1[1]
                                            prob[index] = line1[len(line1) - 9]
                                            lenth[index] = line1[len(line1) - 4]
                                            start[index] = line2[0]
                                            end[index] = line2[1]
                                    if float(prob[index]) < float(line1[len(line1) - 9]):
                                        data[index] = line
                                        name11[index] = line1[1]
                                        prob[index] = line1[len(line1) - 9]
                                        lenth[index] = line1[len(line1) - 4]
                                        start[index] = line2[0]
                                        end[index] = line2[1]

                    else:
                        if line5[0] == "1":
                            if float(line1[len(line1) - 4]) > 5:
                                data.append(line)
                                name11.append(line1[1])
                                prob.append(line1[len(line1) - 9])
                                lenth.append(line1[len(line1) - 4])
                                start.append(line2[0])
                                end.append(line2[1])

                for frag in data:
                    f.write(frag)
    pass

def out_frag3():
    divided_hhm = "/home/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        out_hhr = divided_hhm + lis + "/" + "out_hhr3" + "/"
        out_frag = divided_hhm + lis + "/" + "out_frag3" + "/"
        names = os.listdir(out_hhr)
        for name in names:
            in_file = out_hhr + name
            out_file = out_frag + name
            f = open(out_file, 'w')
            data = []
            name11 = []
            prob = []
            lenth = []
            start = []
            end = []
            with open(in_file, 'r') as r:
                for line in r.readlines():
                    line1 = line.split()
                    m = len(line1)
                    line2 = line1[len(line1) - 2].split('-')
                    line5 = line1[len(line1) - 3].split('-')
                    index = 0
                    index_n = 0
                    same_name = []
                    n = False
                    for i in name11:
                        if i == line1[1]:
                            n = True
                            same_name.append(index_n)
                        index_n = index_n + 1
                    if n:
                        for i in same_name:
                            index = int(i)
                            if line5[0] == "1":
                                if int(end[index]) < int(line2[0]) or int(start[index]) > int(line2[1]):
                                    flag_sss = True
                                    for j in same_name:
                                        index = int(j)
                                        if int(end[index]) > int(line2[0]) or int(start[index]) < int(line2[1]):
                                            flag_sss = False
                                    if flag_sss and float(line1[len(line1) - 4]) > 2:
                                        data.append(line)
                                        name11.append(line1[1])
                                        prob.append(line1[len(line1) - 9])
                                        lenth.append(line1[len(line1) - 4])
                                        start.append(line2[0])
                                        end.append(line2[1])
                                else:
                                    if float(prob[index]) == float(line1[len(line1) - 9]):
                                        if int(lenth[index]) > int(line1[len(line1) - 4]):
                                            data[index] = line
                                            name11[index] = line1[1]
                                            prob[index] = line1[len(line1) - 9]
                                            lenth[index] = line1[len(line1) - 4]
                                            start[index] = line2[0]
                                            end[index] = line2[1]
                                    if float(prob[index]) < float(line1[len(line1) - 9]):
                                        data[index] = line
                                        name11[index] = line1[1]
                                        prob[index] = line1[len(line1) - 9]
                                        lenth[index] = line1[len(line1) - 4]
                                        start[index] = line2[0]
                                        end[index] = line2[1]

                    else:
                        if line5[0] == "1":
                            if float(line1[len(line1) - 4]) > 2:
                                data.append(line)
                                name11.append(line1[1])
                                prob.append(line1[len(line1) - 9])
                                lenth.append(line1[len(line1) - 4])
                                start.append(line2[0])
                                end.append(line2[1])

                for frag in data:
                    f.write(frag)
    pass

def out_angle6_21():
    error = 0
    divided_hhm = "/iobio/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        positions = []
        index = 0
        frag = divided_hhm + lis + "/" + "out_frag" + "/"
        in_frag = "/iobio/fqq/gernerate_frag_library/pdb_angle/"
        names = os.listdir(frag)
        size = len(names)
        for i in range(1, size + 1):
            positions.append("position" + str(i) + ".hhr")
        out_angle = divided_hhm + lis + "/" + "out_angle.txt"
        w = open(out_angle, 'w')
        for position in positions:
            index = index + 1
            po = "position : " + str(index)
            w.write(po + "\n")
            w.write("\n")
            flag1 = True
            input_frag = frag + position
            with open(input_frag, 'r') as r:
                for line in r.readlines():
                    line1 = line.strip()
                    line2 = line1.split()
                    line3 = line2[len(line2) - 2].split('-')
                    line5 = line2[len(line2) - 3].split('-')
                    flag = False
                    input_pdb = in_frag + line2[1] + ".txt"
                    with open(input_pdb, 'r')as r1:
                        for angle in r1.readlines():
                            angle = angle.strip()
                            angle1 = angle.split()
                            if (float(line3[1]) - float(line3[0]) + 1) == float(line2[len(line2) - 4]):
                                if flag:
                                    p = p + 1
                                    w.write(line2[1] + "   " + angle + "   " + str(p) + "   " + line2[
                                        len(line2) - 9] + "\n")
                                if angle1[3] == line3[0]:
                                    if flag1:
                                        flag1 = False
                                    flag = True
                                    p = index + int(line5[0]) - 1
                                    w.write(line2[1] + "   " + angle + "   " + str(p) + "   " + line2[
                                        len(line2) - 9] + "\n")
                                if angle1[3] == line3[1]:
                                    flag = False
                                    w.write("\n")
                            elif (float(line3[1]) - float(line3[0]) + 1) != float(line2[len(line2) - 4]):
                                error = error + 1
                                print(error)
                    r1.close()
            r.close()
        w.close()
    pass

def out_angle3():
    error = 0
    divided_hhm = "/home/fqq/Database_3/divided_hhm/"
    dirs = os.listdir(divided_hhm)
    for lis in dirs:
        print(lis)
        positions = []
        index = 0
        frag = divided_hhm + lis + "/" + "out_frag3" + "/"
        in_frag = "/home/fqq/Database_3/gernerate_frag_library/pdb_angle/"
        names = os.listdir(frag)
        size = len(names)
        for i in range(1, size + 1):
            positions.append("position" + str(i) + ".hhr")
        out_angle = divided_hhm + lis + "/" + "3_angle.txt"
        w = open(out_angle, 'w')
        for position in positions:
            index = index + 1
            po = "position : " + str(index)
            w.write(po + "\n")
            w.write("\n")
            flag1 = True
            input_frag = frag + position
            with open(input_frag, 'r') as r:
                for line in r.readlines():
                    line1 = line.strip()
                    line2 = line1.split()
                    line3 = line2[len(line2) - 2].split('-')
                    line5 = line2[len(line2) - 3].split('-')
                    flag = False
                    input_pdb = in_frag + line2[1] + ".txt"
                    with open(input_pdb, 'r')as r1:
                        for angle in r1.readlines():
                            angle = angle.strip()
                            angle1 = angle.split()
                            if (float(line3[1]) - float(line3[0]) + 1) == float(line2[len(line2) - 4]):
                                if flag:
                                    p = p + 1
                                    w.write(line2[1] + "   " + angle + "   " + str(p) + "   " + line2[
                                        len(line2) - 9] + "\n")
                                if angle1[3] == line3[0]:
                                    if flag1:
                                        flag1 = False
                                    flag = True
                                    p = index + int(line5[0]) - 1
                                    w.write(line2[1] + "   " + angle + "   " + str(p) + "   " + line2[
                                        len(line2) - 9] + "\n")
                                if angle1[3] == line3[1]:
                                    flag = False
                                    w.write("\n")
                            elif (float(line3[1]) - float(line3[0]) + 1) != float(line2[len(line2) - 4]):
                                error = error + 1
                                print(error)
                    r1.close()
            r.close()
        w.close()

    pass

def choose_frag():
    divided = "/iobio/fqq0/Database_3/divided_hhm/"
    dirs = os.listdir(divided)
    for dir in dirs:
        print(dir)
        number = 0
        index = 0
        in_pdb = divided + dir + "/out_angle.txt"
        out_score = divided + dir + "/frag_score.txt"
        f1 = open(in_pdb, 'r')
        w = open(out_score, 'w')
        ss1 = []
        ss2 = []
        ss3 =[]
        in_ss = "/iobio/fqq/choose_frag/sencond_structure/PSIPRED/" + dir + ".ss2"
        f3 = open(in_ss, 'r')
        for line in f3.readlines():
            line = line.strip()
            line1 = line.split()

            if len(line1) == 6:
                ss1.append(line1[2])
                ss2.append(ss1)
                ss1 = []
        flag = False
        for line in f1.readlines():
            line = line.strip()
            line1 = line.split()
            if len(line1) > 3:
                name = line1[0]
                in_pdbz = "/iobio/fqq/gernerate_frag_library/pdb_zhibiao/" + name + ".txt"
                f2 = open(in_pdbz, 'r')
                for lin in f2.readlines():
                    lin = lin.strip()
                    lin1 = lin.split()
                    if len(lin1) > 0:
                        if lin1[0] == line1[4]:
                            flag = True
                            if lin1[2] == "G" or lin1[2] == "H" or lin1[2] == "I":
                                if ss2[int(line1[5]) - 1][0] == "H":
                                    ss3.append("3")
                                if ss2[int(line1[5]) - 1][0] == "E":
                                    ss3.append("0")
                                if ss2[int(line1[5]) - 1][0] == "C":
                                    ss3.append("1")
                            if lin1[2] == "E":
                                if ss2[int(line1[5]) - 1][0] == "H":
                                    ss3.append("0")
                                if ss2[int(line1[5]) - 1][0] == "E":
                                    ss3.append("3")
                                if ss2[int(line1[5]) - 1][0] == "C":
                                    ss3.append("1")
                            if lin1[2] == "T" or lin1[2] == "B" or lin1[2] == "S" or lin1[2] == "C":
                                if ss2[int(line1[5]) - 1][0] == "H":
                                    ss3.append("1")
                                if ss2[int(line1[5]) - 1][0] == "E":
                                    ss3.append("1")
                                if ss2[int(line1[5]) - 1][0] == "C":
                                    ss3.append("3")


            if len(line1) == 3:
                flag = False
                number = 0
                index = int(line1[2])
            if len(line1) == 0 and flag:
                number = number + 1
                su = 0
                for i in range(0, len(ss3)):
                    su = float(su) + float(ss3[i])
                fs = su / len(ss3)
                w.write("position" + str(index) + "_frag" + str(number) + ".pdb" + "   " + str(fs) + "\n")
                ss3 = []

    pass

def gernerate_out_angles():
    divided = "/iobio/fqq0/Database_3/divided_hhm/"
    dirs = os.listdir(divided)
    for dir in dirs:
        print(dir)
        frag = []
        position = []
        unit = []
        position1 = []
        unit1 = []
        index = 0
        in_angle = divided + dir + "/out_angle.txt"
        out_angle = divided + dir + "/angle_20.txt"
        w = open(out_angle, 'w')
        f = open(in_angle, 'r')
        for line in f.readlines():
            line = line.strip()
            line1 = line.split()
            if len(line1) == 3 and line1[2] != "1":
                unit.append(position)
                position = []
            if len(line1) == 0 and len(frag) != 0:
                position.append(frag)
                frag = []
            if len(line1) > 5:
                frag.append(line)
        unit.append(position)
        position = []

        print(len(unit), len(unit[0][0]))
        number = 0
        po = "1"
        po1 = 0
        in_score = divided + dir + "/frag_score.txt"
        f1 = open(in_score, 'r')
        for line in f1.readlines():
            line = line.strip()
            line1 = line.split()
            line2 = line.split(".")
            line21 = line2[0].split("_")
            line11 = line1[0].split("_")
            line13 = line11[0]
            line14 = line21[1]
            line12 = line13[8:]
            line15 = line14[4:]
            if line12 != po and line12 != "1":
                unit1.append(position1)
                position1 = []

                po1 = int(line12) - int(po) - 1
                for i in range(0, po1):
                    unit1.append([])
                po = line12
            if len(line1) == 2:
                if float(line1[1]) >= 2.0:
                    index = int(line12)
                    position1.append(unit[index - 1][int(line15) - 1])
        unit1.append(position1)
        position1 = []

        for i in range(0, len(unit1)):
            w.write("position : " + str(i + 1) + "\n")
            w.write("\n")
            for j in range(0, len(unit1[i])):
                for k in range(0, len(unit1[i][j])):
                    w.write(unit1[i][j][k] + "\n")
                w.write("\n")

    pass


if __name__ == '__main__':

    out_hhr3()
    out_hhr6_21()
    out_frag3()
    out_frag6_21()
    out_angle3()
    out_angle6_21()
    choose_frag()
    gernerate_out_angles()

    pass