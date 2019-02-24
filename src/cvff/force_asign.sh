#!/bin/sh
data_dir=/HOME/nscc-gz_pinchen/sf_box/lammps-30Mar18/tools/msi2lmp
export MSI2LMP_LIBRARY=${data_dir}/frc_files
${data_dir}/src/msi2lmp.exe  $1 -class 1 -frc $2 -ignore
