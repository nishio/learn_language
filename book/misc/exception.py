# -*- coding: utf-8 -*-
"""
exception*.cのコードを雑誌に貼る形に整形するスクリプト
"""
import sys
INDENT = "  "
filename = sys.argv[1]
fi = file(filename)
for line in fi:
    if 'printf("Error' in line:
        indent = " " * line.find("printf")
        for i in range(3):
            print INDENT + indent + "/* 失敗した時の処理 */"
    else:
        print INDENT + line.rstrip()
