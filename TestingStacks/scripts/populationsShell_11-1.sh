#!/bin/bash

!populations -b 303 \
-P populations_temp \
-M ../scripts/PopulationMapTEST.txt \
-t 36 \
-r 0.50 \
-p 2 \
-m 5 \
--genepop \
2>> populations_out_batch303



!populations -b 230 \
-P stacks_M2 \
-M ../scripts/PopulationMapTEST.txt \
-t 36 \
-r 0.50 \
-p 2 \
-m 5 \
--genepop \
2>> populations_out_batch230


!populations -b 330 \
-P stacks_m3 \
-M ../scripts/PopulationMapTEST.txt \
-t 36 \
-r 0.50 \
-p 2 \
-m 5 \
--genepop \
2>> populations_out_batch330



!populations -b 1030 \
-P stacks_m10 \
-M ../scripts/PopulationMapTEST.txt \
-t 36 \
-r 0.50 \
-p 2 \
-m 5 \
--genepop \
2>> populations_out_batch1030


