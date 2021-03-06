# MSD:均方根位移

## 使用方法
文件内时间步长，原子个数可任意
```
(venv1) C:\Users\Yan\Downloads\FFD\src\msd>python msd.py -h
usage: msd.py [-h] [-o OUTPUT] input1 input2

positional arguments:
  input1                the name of input file 1
  input2                the name of input file 2

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the name of output file

(venv1) C:\Users\Yan\Downloads\FFD\src\msd>python msd.py ./4-db-msd-cu.lammpstrj ./4-db-msd-db.lammpstrj
result has been successfully written to msd.txt
```

## 测试结果

小样例测试：
File1
```
ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
2
ITEM: BOX BOUNDS pp pp pp
-5.23605 54.2864
1.40777 51.0098
0.00696182 49.609
ITEM: ATOMS id type xu yu zu
 1 1 1 2 3
 2 1 4 5 6
ITEM: TIMESTEP
1
ITEM: NUMBER OF ATOMS
2
ITEM: BOX BOUNDS pp pp pp
-5.23605 54.2864
1.40777 51.0098
0.00696182 49.609
ITEM: ATOMS id type xu yu zu
 1 1 7 8 9
 2 1 10 11 12
```
 
File2
```
ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
2
ITEM: BOX BOUNDS pp pp pp
-5.23605 54.2864
1.40777 51.0098
0.00696182 49.609
ITEM: ATOMS id type xu yu zu
 1 1 13 14 15
 2 1 16 17 18
ITEM: TIMESTEP
1
ITEM: NUMBER OF ATOMS
2
ITEM: BOX BOUNDS pp pp pp
-5.23605 54.2864
1.40777 51.0098
0.00696182 49.609
ITEM: ATOMS id type xu yu zu
 1 1 19 20 21
 2 1 22 23 24
 ```
 
计算结果msd.txt与预期相符
```
timestep distance_A_B
1 20.784609690826528
2 20.784609690826528
```


在timestep = 1的时候验算结果同样符合预期
```
python msd.py ./4-db-msd-cu.lammpstrj ./4-db-msd-db.lammpstrj
文件1的(x_min, y_min, z_min) = (20.5647 24.2907 24.4791)
文件1的(x_max, y_max, z_max) = (28.4857 28.1269 25.1369)
中心1=[24.5252 26.2088 24.808 ]
文件2的(x_min, y_min, z_min) = (34.2643  10.3227   5.26964)
文件2的(x_max, y_max, z_max) = (41.1058  14.7752   8.29968)
中心2=[37.68505 12.54895  6.78466]
距离为26.165128297040702
```

## 输入文件
```
ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
2
ITEM: BOX BOUNDS pp pp pp
-5.23605 54.2864
1.40777 51.0098
0.00696182 49.609
ITEM: ATOMS id type xu yu zu
 1 1 20.5647 24.2907 25.1369
 2 1 28.4857 28.1269 24.4791
 ...
```
上述文件总共有5000个时间步，每步中包含TIMESTEP/NUMBER OF ATOMS/BOX BOUNDSATOMS四个部分，要求计算每个时间步中两个Cu原子的中心Ax


4-db-msd-db.lammpstrj
```
ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
18
ITEM: BOX BOUNDS pp pp pp
7.92383 67.4463
-12.2521 37.35
-18.0164 31.5857
ITEM: ATOMS id type xu yu zu
 1 1 36.2453 12.5799 6.45944
 2 1 36.9204 11.3168 6.65631
 3 1 38.3361 11.2864 6.93642
 4 1 39.0869 12.5187 7.02178
 5 1 38.4125 13.7813 6.82308
 6 1 36.9966 13.812 6.54283
 7 2 34.7641 12.6357 6.19075
 8 2 40.5603 12.5104 7.33631
 9 3 34.3304 11.6367 6.07746
 10 3 34.5786 13.1985 5.26964
 11 3 34.2643 13.14 7.02406
 12 3 41.1058 13.0544 6.55771
 13 3 40.9617 11.4929 7.39167
 14 3 40.7276 13.0031 8.29968
 15 3 36.3627 10.3757 6.60428
 16 3 38.8323 10.3227 7.09326
 17 3 38.9701 14.7215 6.89346
 18 3 36.4943 14.7752 6.40295
 ....
```
与上述Cu原子的格式类似，要求计算该原子团的几何中心Bx，计算方法为(1/2(x_max + x_min),1/2(y_max + y_min),1/2(z_max + z_mic))。但是不能将原子个数固定，该算例有十八个原子，另外还有其他文件包含的原子数范围12~18.


然后计算Ax与Bx之间的距离，做出与时间对应关系，输出如下：
```
timestep distance_A_B
0   xx
1   xx
2   xx
....
```

伪代码
```
读入4-db-msd-cu.lammpstrj;
遍历每个timestep的原子，获得原子中心A的xyz坐标;
读入4-db-msd-db.lammpstrj;
遍历每个timestep的原子，获得原子团的几何中心B的xyz坐标;
根据timestep,计算A与B的距离[（Ax - Bx）^2 + (Ay - By) + (Az - Bz)]开根号;
将结果写入文本msd.txt;

```
