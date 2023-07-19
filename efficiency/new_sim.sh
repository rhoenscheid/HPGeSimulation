#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR


#cd /unix/legend/software/ruben/sim/efficiency_qsub/

xvar=$1
yvar=$2
zvar=$3
nvar=$4

datevar=$(date +"%d-%b-%Y-%H-%M")

foldername=$1"-"$2"-"$3"-"$datevar

cp -r template $foldername

cd $foldername
bash set_pos.sh $xvar $yvar $zvar $nvar

bash use_qsub.sh

outputname=$1"-"$2"-"$3"-"$4

cd ..


cp $foldername"/final_analysis/effi_df.csv" "output/"$outputname"_df.csv"
cp $foldername"/final_analysis/parameters_deg2.csv" "output/"$outputname"_fit_parameters2.csv"
cp $foldername"/final_analysis/parameters_deg3.csv" "output/"$outputname"_fit_parameters3.csv"
cp $foldername"/final_analysis/parameters_deg4.csv" "output/"$outputname"_fit_parameters4.csv"
cp $foldername"/final_analysis/unc_deg2.csv" "output/"$outputname"_fit_parameters2_unc.csv"
cp $foldername"/final_analysis/unc_deg3.csv" "output/"$outputname"_fit_parameters3_unc.csv"
cp $foldername"/final_analysis/unc_deg4.csv" "output/"$outputname"_fit_parameters4_unc.csv"
cp $foldername"/final_analysis/Fitted_Curve_deg4.png" "output/"$outputname"_fit_deg4.png"


echo Done.
