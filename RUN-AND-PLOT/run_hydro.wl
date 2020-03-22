#!/usr/bin/env wolframscript
#
#
(*LaunchKernels[5]*)


MainFolder = "/Users/damirdevetak/FluiduM-21-01-2020/RUN_AND_PLOT"

SetDirectory[StringJoin[MainFolder, "/FluiduM-newResList/Package"]]
<<FluiduM`
Off[FindRoot::lstol];

(***** Run Hydro & define output files *******)
     
(* 1: pionPlus, 2: kaonPlus, 3: protonPlus, 4: lambdaZero, 5: xiMinus, 6: omegaMinus *)

entropyC1 =  ToExpression[$ScriptCommandLine[[1]]];
entropyC2 =  ToExpression[$ScriptCommandLine[[2]]];
entropyC3 =  ToExpression[$ScriptCommandLine[[3]]];
entropyC4 =  ToExpression[$ScriptCommandLine[[4]]];
entropyC5 =  ToExpression[$ScriptCommandLine[[5]]];

etas =    ToExpression[$ScriptCommandLine[[6]]];
bulk =    ToExpression[$ScriptCommandLine[[7]]];
tch =     ToExpression[$ScriptCommandLine[[8]]];
tau0 =    ToExpression[$ScriptCommandLine[[9]]];


(***********load initial conditions **************)

rprofile = Import["./InitialCondition-p0/LHCPbPb2760GeV/WeightFunction.txt", "Table"][[All, 1]];
wprofile = Transpose[Import["./InitialCondition-p0/LHCPbPb2760GeV/WeightFunction.txt", "Table"][[All, 2 ;; All]]];
averageMultiplicity = Flatten[Import["./InitialCondition-p0/LHCPbPb2760GeV/AverageMultiplicity.txt", "Table"]];


(*************************************************)


RunFullHydro[normC1_, normC2_, normC3_, normC4_, normC5_, eta_, bulk_, Tch_, tau0_] := Module[{myFluidProperties, initialTrento, HydroSolution, myFluidFieldsOnFreezeOutSurface, allParticles1Classes},

  pTList = Range[0.1, 3.0, 0.1];
  myGrid = discretizationPoints[1/10, 50, 128];
  myFluidProperties =  setFluidPropertiesQCDParametrization["ShearViscosityOverEntropy" -> eta, "BulkViscosityOverEntropyAmplitude" -> bulk];
  initialTrento = { setInitialConditionsCentrality[{ {0, 5}   }, normC1, tau0, myFluidProperties, myGrid, rprofile, wprofile, averageMultiplicity][[1]],
                    setInitialConditionsCentrality[{ {5, 10}  }, normC2, tau0, myFluidProperties, myGrid, rprofile, wprofile, averageMultiplicity][[1]],
                    setInitialConditionsCentrality[{ {10, 20} }, normC3, tau0, myFluidProperties, myGrid, rprofile, wprofile, averageMultiplicity][[1]],
                    setInitialConditionsCentrality[{ {20, 30} }, normC4, tau0, myFluidProperties, myGrid, rprofile, wprofile, averageMultiplicity][[1]],
                    setInitialConditionsCentrality[{ {30, 40} }, normC5, tau0, myFluidProperties, myGrid, rprofile, wprofile, averageMultiplicity][[1]] 
                  };
  HydroSolution = evolveBackground[{tau0, 20}, myFluidProperties, myGrid, #, "showProgressIndicator" -> False] & /@ initialTrento;
  myFluidFieldsOnFreezeOutSurface = freezeOut[#, 128, Tch] & /@ HydroSolution ;
  allParticles1Classes = spectraResonanceDecays[particleDataset, pTList, #, myFluidProperties, "DissipativeCorrections" -> True,  
  "PartialChemicalEquilibrium" -> False] & /@ myFluidFieldsOnFreezeOutSurface

  ]

spectraValues = RunFullHydro[entropyC1, entropyC2, entropyC3, entropyC4, entropyC5, etas, bulk, tch, tau0];

(***** MACROS *****)

graph = StringJoin["python ", MainFolder, "/MACROS/graph/make_graph.py "]
fit = StringJoin["python ", MainFolder, "/MACROS/fit/make_fit.py "]
makeRatio = StringJoin["python ", MainFolder, "/MACROS/ratio/make_ratio.py "]
egraph = StringJoin["python ", MainFolder, "/MACROS/graph/make_graph_with_error.py "]

(***** DATA ******)

PT = StringJoin[MainFolder, "/ALICE-DATA/fullPtRange.json"]

NumberOfCent = 5

CENTS = {"0-5/", "5-10/", "10-20/", "20-30/", "30-40/"}
Particles = {"pion/pi0139plu.json", "kaon/Ka0492plu.json", "proton/pr0938plu.json"}
particleFolders = {"pion/", "kaon/", "proton/", "lambda/", "xi/", "omega/"}

DataAliceFolder = Table[ StringJoin[ MainFolder, "/ALICE-DATA/", cent, part ],  {cent, CENTS}, {part, Particles} ]

PtData =   {
            StringJoin[MainFolder, "/ALICE-DATA/0-5/pion/pt_pi0139plu.json"],
            StringJoin[MainFolder, "/ALICE-DATA/0-5/kaon/pt_Ka0492plu.json"],
            StringJoin[MainFolder, "/ALICE-DATA/0-5/proton/pt_pr0938plu.json"]
           }

(***** Define output files *******)
     
(* 1: pionPlus, 2: kaonPlus, 3: protonPlus, 4: lambdaZero, 5: xiMinus, 6: omegaMinus *)


workingFolder = Table[StringJoin[MainFolder, "/output_folder/", cent, particleFolders[[i]]], {cent, CENTS}, {i, 3}]; 

outputJsonHydro =    Table[ StringJoin[workingFolder[[cent]][[iPart]], "spectra_", ToString[iPart], ".json"], {cent, NumberOfCent}, {iPart, 3}];   
outputFitJsonHydro = Table[ StringJoin[workingFolder[[cent]][[iPart]], "eval_fit_graph_spectra_", ToString[iPart], ".json"],  {cent, NumberOfCent}, {iPart, 3}];
outputGraphHydro =   Table[ StringJoin[workingFolder[[cent]][[iPart]], "graph_spectra_", ToString[iPart], ".root"], {cent, NumberOfCent},  {iPart, 3}];
outputFitRatio =     Table[ StringJoin[workingFolder[[cent]][[iPart]], "ratio_eval_fit_graph_spectra_", ToString[iPart], ".json"],  {cent, NumberOfCent}, {iPart, 3}];

(*************)

(***** Get Data From spectraValues *****)

selectedParticlePion =    Table[spectraValues[[ cent, "pi0139plu", "pTSpectra"]], {cent, NumberOfCent}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *) 
selectedParticleKaon =    Table[spectraValues[[ cent, "Ka0492plu", "pTSpectra"]], {cent, NumberOfCent}];
selectedParticleProton =  Table[spectraValues[[ cent, "pr0938plu", "pTSpectra"]], {cent, NumberOfCent}];

Table[Export[outputJsonHydro[[cent]][[1]], selectedParticlePion[[cent]]],   {cent, NumberOfCent}];
Table[Export[outputJsonHydro[[cent]][[2]], selectedParticleKaon[[cent]]],   {cent, NumberOfCent}];
Table[Export[outputJsonHydro[[cent]][[3]], selectedParticleProton[[cent]]], {cent, NumberOfCent}];


(****** Define scripts and run them *******)

script1 = Table[StringJoin[graph," ",     workingFolder[[cent]][[i]], " ",  PT," ", outputJsonHydro[[cent]][[i]], " -b"], {cent, NumberOfCent}, {i, 3} ]; 
script2 = Table[StringJoin[fit, " ",      workingFolder[[cent]][[i]], " ",  outputGraphHydro[[cent]][[i]], " ", PtData[[i]], " -b"], {cent, NumberOfCent}, {i, 3} ];
script3 = Table[StringJoin[makeRatio," ", workingFolder[[cent]][[i]], " ",  DataAliceFolder[[cent]][[i]], " ", outputFitJsonHydro[[cent]][[i]], " -b"], {cent, NumberOfCent}, {i, 3} ];
script4 = Table[StringJoin[egraph, " ",   workingFolder[[cent]][[i]], " ",  PtData[[i]], " ", outputFitRatio[[cent]][[i]], " -b"], {cent, NumberOfCent}, {i, 3} ];

Do[ Run[script1[[cent]][[part]]],{cent, NumberOfCent}, {part, 3} ];
Do[ Run[script2[[cent]][[part]]],{cent, NumberOfCent}, {part, 3} ];
Do[ Run[script3[[cent]][[part]]],{cent, NumberOfCent}, {part, 3} ];
Do[ Run[script4[[cent]][[part]]],{cent, NumberOfCent}, {part, 3} ];

(*CloseKernels[5]*)

Quit[]

