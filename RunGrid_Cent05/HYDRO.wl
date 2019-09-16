#!/usr/bin/env wolframscript
#
#

LaunchKernels[10]

dataC = Import["/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/grid_10bins_27_08.dat"]
SetDirectory[StringJoin["/lustre/nyx/alice/users/ddevetak/FluiduM/FluiduM-newResList", "/Package"]]

<<FluiduM`
Off[FindRoot::lstol];

LineIndex1 = ToExpression[$ScriptCommandLine[[1]]]  (*which lines are to be taken from combinations.txt*)
LineIndex2 = ToExpression[$ScriptCommandLine[[2]]]  (*which lines are to be taken from combinations.txt*)
JobFolder = ToString[$ScriptCommandLine[[3]]]

(*COMMENTS*)

(********** RUN HYDRO looping dataC COMBINATIONS ************)

Print["Combinations for lines...", LineIndex1, " ", LineIndex2]

RunHydroUntilFreezeOut[entropyXtau0_, etas_, bulk_, tch_, tau0_]:=Module[{myGrid,myFluidProperties,initialTrento,HydroSolution,myFluidFieldsOnFreezeOutSurface},
        myGrid = discretizationPoints[1/10, 50, 128];
        myFluidProperties =  setFluidPropertiesQCDParametrization["ShearViscosityOverEntropy" -> etas, "BulkViscosityOverEntropyAmplitude" -> bulk];
        initialTrento = setInitialConditionsTrento[{ {0, 5} }, entropyXtau0, tau0, myFluidProperties, myGrid][[1]];
        HydroSolution = evolveBackground[{tau0, 20}, myFluidProperties, myGrid, initialTrento, "showProgressIndicator" -> False];
        myFluidFieldsOnFreezeOutSurface =freezeOut[HydroSolution, 50, tch];
        Clear[HydroSolution,myGrid,initialTrento,myFluidProperties];
        myFluidFieldsOnFreezeOutSurface
]

pTList = Range[0.1, 3.0, 0.1];

CONF = dataC[[LineIndex1;;LineIndex2]]
Print["CONF = ", CONF]

parallelPhase = ParallelMap[RunHydroUntilFreezeOut[#[[1]],#[[2]],#[[3]],#[[4]],#[[5]]]& , CONF, DistributedContexts -> {"FluiduM`", "Global`"}, Method->"CoarsestGrained"];
myFluidProperties =  setFluidPropertiesQCDParametrization["ShearViscosityOverEntropy" -> #[[2]], "BulkViscosityOverEntropyAmplitude" -> #[[3]]]& /@ CONF;
spectraValues = spectraResonanceDecays[particleDataset, pTList, #[[1]], #[[2]], "DissipativeCorrections" -> True] & /@ Transpose[{parallelPhase, myFluidProperties}];


(***************** OUTPUT FILES & RUN MACROS ******************)

PT ="/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/fullPtRange.json"

Particles = {"pion/pi0139plu.json", "kaon/Ka0492plu.json", "proton/pr0938plu.json"}
particleFolders = {"/pion/", "/kaon/", "/proton/", "/lambda/", "/xi/", "/omega/"}


(* 1: pionPlus, 2: kaonPlus, 3: protonPlus, 4: lambdaZero, 5: xiMinus, 6: omegaMinus *)

StoringFileFolder = Table[StringJoin["/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/0-5/JOBS/", JobFolder, particleFolders[[i]]],{i,3}];


outputJsonHydro =     Table[StringJoin[StoringFileFolder[[i]], "spectra_", ToString[comb], ".json"], {i,3}, {comb, LineIndex1, LineIndex2} ];

selectedParticlePion =    Table[spectraValues[[ comb, "pi0139plu", "pTSpectra"]], {comb, 1, LineIndex2 - LineIndex1 + 1} ];
selectedParticleKaon =    Table[spectraValues[[ comb, "Ka0492plu", "pTSpectra"]], {comb, 1, LineIndex2 - LineIndex1 + 1} ];
selectedParticleProton =  Table[spectraValues[[ comb, "pr0938plu", "pTSpectra"]], {comb, 1, LineIndex2 - LineIndex1 + 1} ];

Table[Export[outputJsonHydro[[1]][[comb]], selectedParticlePion[[comb]]],   {comb, 1, LineIndex2 - LineIndex1 + 1}];   (**** 1 in json is folder for pion   ****)
Table[Export[outputJsonHydro[[2]][[comb]], selectedParticleKaon[[comb]]],   {comb, 1, LineIndex2 - LineIndex1 + 1}];   (**** 2 in json is folder for kaon   ****)
Table[Export[outputJsonHydro[[3]][[comb]], selectedParticleProton[[comb]]], {comb, 1, LineIndex2 - LineIndex1 + 1}];   (**** 3 in json is folder for proton ****)

CloseKernels[];
Quit[]

