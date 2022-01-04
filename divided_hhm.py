'''
Split hhm file for segment search

'''
import os
from Bio import PDB
import shutil


def divided_hhm6_21():
    path = '/iobio/fqq/Database_3/divided_hhm/'
    pdb = '/iobio/fqq/Database_3/Test_pdb/'
    in_fasta = "/iobio/fqq/Database_3/Test_Fasta/"
    names = os.listdir(pdb)
    for name in names:
        print(name)
        name1 = name.split('.')
        fasta_line = in_fasta + name1[0] + ".fasta"
        r = open(fasta_line, 'r')
        fasta = []
        for line in r.readlines():
            line = line.strip()
            if len(line) > 20:
                for i in range(0, len(line)):
                    fasta.append(line[i])
        r.close()
        parser1 = PDB.PDBParser()
        in_pdb = pdb + name
        f = open(in_pdb, 'r')
        c = ''
        for line in f.readlines():
            line = line.strip()
            line1 = line.split()
            if line1[0] == "ATOM":
                c = line1[4]
                index = int(line1[5])
                break
        structure = parser1.get_structure(name, in_pdb)
        model = structure[0]
        chain = model[c]
        fasta_len = len(chain)

        if fasta_len > 1000:
            print("error")
        in_frag_hhm = path + name1[0] + "/frag_hhm/"
        for i in range(1, 1000):
            file_name = in_frag_hhm + "position" + str(i)

            seg = []
            flag = False
            flag_position = True
            flag_end = False
            flag_w = False
            c = 0
            count = 0

            for j in range(6, 22):
                seg.append(j)

            for j in seg:
                j_str = str(j)
                seg_len = int(j_str)
                seg_position = i
                if (seg_position + seg_len) <= fasta_len + 1:
                    filename = file_name + '_frag' + j_str + '.hhm'
                    f1 = open(filename, 'w')
                num = ''

                hhm = "/iobio/fqq/Database_3/Test_hhm/"
                in_hhm = hhm + name1[0] + ".hhm"
                with open(in_hhm, 'r')as r:
                    for line in r.readlines():
                        if flag:
                            line1 = line.split()
                            if len(line1) != 0:
                                if len(line1) != 1:
                                    if line1[1] == '1':
                                        flag_position = False
                                if (seg_position + seg_len) < fasta_len + 1:
                                    if line1[1] == str(seg_position) and line1[0] == fasta[int(seg_position) - 1]:
                                        flag_position = True
                                    if line1[1] == str(seg_position + seg_len) and line1[0] == fasta[int(seg_position + seg_len) - 1]:
                                        f1.write(num)
                                        f1.write("//")
                                        num = ''
                                        flag_position = True
                                        flag = False
                                if (seg_position + seg_len) == fasta_len + 1:
                                    if len(line1) != 1:
                                        if line1[1] == str(seg_position) and line1[0] == fasta[int(seg_position) - 1]:
                                            flag_position = True
                                    if line1[0] == "//":
                                        flag_end = True
                        if not flag:
                            line = line.strip()
                            num = num + line + '\n'
                        if flag and flag_position:
                            num = num + line
                        if line == "#":
                            flag = True
                        if flag_end:
                            f1.write(num)
                            f1.write("//")
                            num = ''
                            flag_end = False
    pass

def divided_hhm3_5():
    path = '/iobio/fqq/Database_3/divided_hhm/'
    pdb = '/iobio/fqq/Database_3/Test_pdb/'
    in_fasta = "/iobio/fqq/Database_3/Test_Fasta/"
    names = os.listdir(pdb)
    for name in names:
        print(name)
        name1 = name.split('.')
        fasta_line = in_fasta + name1[0] + ".fasta"
        r = open(fasta_line, 'r')
        fasta = []
        for line in r.readlines():
            line = line.strip()
            if len(line) > 20:
                for i in range(0, len(line)):
                    fasta.append(line[i])
        r.close()
        parser1 = PDB.PDBParser()
        in_pdb = pdb + name
        f = open(in_pdb, 'r')
        c = ''
        for line in f.readlines():
            line = line.strip()
            line1 = line.split()
            if line1[0] == "ATOM":
                c = line1[4]
                index = int(line1[5])
                break
        structure = parser1.get_structure(name, in_pdb)
        model = structure[0]
        chain = model[c]
        fasta_len = len(chain)
        if fasta_len > 1000:
            print("error")
        in_frag_hhm = path + name1[0] + "/frag_hhm3/"
        for i in range(1, 1000):
            file_name = in_frag_hhm + "position" + str(i)
            seg = []
            flag = False
            flag_position = True
            flag_end = False
            flag_w = False
            c = 0
            count = 0
            for j in range(3, 6):
                seg.append(j)
            for j in seg:
                j_str = str(j)
                seg_len = int(j_str)
                seg_position = i
                if (seg_position + seg_len) <= fasta_len + 1:
                    filename = file_name + '_frag' + j_str + '.hhm'
                    f1 = open(filename, 'w')
                num = ''
                hhm = "/iobio/fqq/Database_3/Test_hhm/"
                in_hhm = hhm + name1[0] + ".hhm"
                with open(in_hhm, 'r')as r:
                    for line in r.readlines():
                        if flag:
                            line1 = line.split()
                            if len(line1) != 0:
                                if len(line1) != 1:
                                    if line1[1] == '1':
                                        flag_position = False
                                if (seg_position + seg_len) < fasta_len + 1:
                                    if line1[1] == str(seg_position) and line1[0] == fasta[int(seg_position) - 1]:
                                        flag_position = True
                                    if line1[1] == str(seg_position + seg_len) and line1[0] == fasta[int(seg_position + seg_len) - 1]:
                                        f1.write(num)
                                        f1.write("//")
                                        num = ''
                                        flag_position = True
                                        flag = False
                                if (seg_position + seg_len) == fasta_len + 1:
                                    if len(line1) != 1:
                                        if line1[1] == str(seg_position) and line1[0] == fasta[int(seg_position) - 1]:
                                            flag_position = True
                                    if line1[0] == "//":
                                        flag_end = True
                        if not flag:
                            line = line.strip()
                            num = num + line + '\n'
                        if flag and flag_position:
                            num = num + line
                        if line == "#":
                            flag = True
                        if flag_end:
                            f1.write(num)
                            f1.write("//")
                            num = ''
                            flag_end = False
    pass


if __name__ == '__main__':

    divided_hhm6_21()
    divided_hhm3_6()

    pass
