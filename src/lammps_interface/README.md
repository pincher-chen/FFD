
https://github.com/peteboyd/lammps_interface
#right
$ bash -x ../command.sh CuMOF-noprous-2cavity_40ST-mixed.cif 
+ python ../lammps_interface/lammps_interface.py CuMOF-noprous-2cavity_40ST-mixed.cif -ff UFF4MOF --molecule-ff UFF

生成data/in文件

#wrong
稍微改了一下cif的结构，添加了一个苯乙烯分子，然后运行同样的脚本报错
```
$ bash -x ../command.sh CuMOF-noprous-2cavity_40ST-mixed.cif 
+ python ../lammps_interface/lammps_interface.py CuMOF-noprous-2cavity_40ST-mixed.cif -ff UFF4MOF --molecule-ff UFF

Traceback (most recent call last):
  File "../../lammps_interface/lammps_interface.py", line 25, in <module>
    sim.write_lammps_files()
  File "/WORK/nscc-gz_pinchen/project/MOFFF/lammps_interface/lammps_interface/lammps_main.py", line 748, in write_lammps_files
    self.unique_pair_terms()
  File "/WORK/nscc-gz_pinchen/project/MOFFF/lammps_interface/lammps_interface/lammps_main.py", line 239, in unique_pair_terms
    pot_names.append(data['pair_potential'].name)
AttributeError: 'NoneType' object has no attribute 'name'
```

追踪/WORK/nscc-gz_pinchen/project/MOFFF/lammps_interface/lammps_interface/lammps_main.py", line 239，添加:
```
            print(data['pair_potential']);
            pot_names.append(data['pair_potential'].name)
```
发现：
```
....
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.105000        3.430851
                      lj/cut        0.105000        3.430851
                      lj/cut        0.105000        3.430851
                      lj/cut        0.105000        3.430851
                      lj/cut        0.105000        3.430851
                      lj/cut        0.105000        3.430851
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
                      lj/cut        0.044000        2.571134
None
Traceback (most recent call last):
  File "../../lammps_interface/lammps_interface.py", line 25, in <module>
    sim.write_lammps_files()
  File "/WORK/nscc-gz_pinchen/project/MOFFF/lammps_interface/lammps_interface/lammps_main.py", line 748, in write_lammps_files
    self.unique_pair_terms()
  File "/WORK/nscc-gz_pinchen/project/MOFFF/lammps_interface/lammps_interface/lammps_main.py", line 239, in unique_pair_terms
    pot_names.append(data['pair_potential'].name)
AttributeError: 'NoneType' object has no attribute 'name'
```
里面出现了None？
