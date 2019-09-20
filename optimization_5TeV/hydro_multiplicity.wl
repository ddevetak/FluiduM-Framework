#!/usr/bin/env wolframscript
#
#

WORKINGFOLDER = "/lustre/nyx/alice/users/ddevetak/ProbeRun/optimization_5TeV"

SetDirectory[StringJoin["/lustre/nyx/alice/users/ddevetak/ProbeRun/FluiduM-newResList", "/Package"]]
<<FluiduM`
Off[FindRoot::lstol];

(***** Run Hydro & define output files *******)
     
(* 1: pionPlus, 2: kaonPlus, 3: protonPlus, 4: lambdaZero, 5: xiMinus, 6: omegaMinus *)

entropy05 =   ToExpression[$ScriptCommandLine[[1]]];
entropy510 =  ToExpression[$ScriptCommandLine[[2]]];
entropy1020 = ToExpression[$ScriptCommandLine[[3]]];
entropy2030 = ToExpression[$ScriptCommandLine[[4]]];
entropy3040 = ToExpression[$ScriptCommandLine[[5]]];

etas =    ToExpression[$ScriptCommandLine[[6]]];
bulk =    ToExpression[$ScriptCommandLine[[7]]];
tch =     ToExpression[$ScriptCommandLine[[8]]];
tau0 =    ToExpression[$ScriptCommandLine[[9]]];


RunFullHydro[norm05_, norm510_, norm1020_, norm2030_, norm3040_, eta_, bulk_, Tch_, tau0_] := Module[{myFluidProperties, initialTrento, HydroSolution, myFluidFieldsOnFreezeOutSurface, allParticles1Classes},

  pTList = Range[0, 4.0, 0.1];
  myGrid = discretizationPoints[1/10, 50, 128];
  myFluidProperties =  setFluidPropertiesQCDParametrization["ShearViscosityOverEntropy" -> eta, "BulkViscosityOverEntropyAmplitude" -> bulk];
  initialTrento = { setInitialConditionsTrento[{ {0, 5}}, norm05, tau0, myFluidProperties, myGrid][[1]],
                    setInitialConditionsTrento[{{5,10}}, norm510, tau0, myFluidProperties, myGrid][[1]],
                    setInitialConditionsTrento[{{10,20} }, norm1020, tau0, myFluidProperties, myGrid][[1]],
                    setInitialConditionsTrento[{ {20,30}}, norm2030, tau0, myFluidProperties, myGrid][[1]],
                    setInitialConditionsTrento[{ {30,40}}, norm3040, tau0, myFluidProperties, myGrid][[1]] 
                  };
  HydroSolution = evolveBackground[{tau0, 20}, myFluidProperties, myGrid, #, "showProgressIndicator" -> False] & /@ initialTrento;
  myFluidFieldsOnFreezeOutSurface = freezeOut[#, 50, Tch] & /@ HydroSolution ;
  allParticles1Classes = spectraResonanceDecays[particleDataset, pTList, #, myFluidProperties, "DissipativeCorrections" -> True] & /@ myFluidFieldsOnFreezeOutSurface

  ]

spectraValues = RunFullHydro[entropy05, entropy510, entropy1020, entropy2030, entropy3040, etas, bulk, tch, tau0];

(***** MACROS *****)
(*****************************************************************************************)

workingFolder = StringJoin[WORKINGFOLDER, "/mul_output_folder/"]; 
centBins = StringJoin[WORKINGFOLDER, "/cents.json"]; 

MultTotalFile = StringJoin[workingFolder, "totalMult.json"];

MultPionFile =   StringJoin[workingFolder, "totalMultPion.json"];
MultKaonFile =   StringJoin[workingFolder, "totalMultKaon.json"];
MultProtonFile = StringJoin[workingFolder, "totalMultProton.json"];

PtPionFile = StringJoin[workingFolder, "PtPion.json"];
PtKaonFile = StringJoin[workingFolder, "PtKaon.json"];
PtProtonFile =   StringJoin[workingFolder, "PtProton.json"];

(**************************** Get Data From spectraValues *********************************)

TotalYield =    Table[spectraValues[[cent]]["TotalMultiplicity"], {cent, 5}];  

PionYield =    Table[spectraValues[[ cent, "pi0139plu", "Multiplicity"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)
KaonYield =    Table[spectraValues[[ cent, "Ka0492plu", "Multiplicity"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)
ProtonYield =  Table[spectraValues[[ cent, "pr0938plu", "Multiplicity"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)

PionMeanPT =    Table[spectraValues[[ cent, "pi0139plu", "AveragepT"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)
KaonMeanPT =    Table[spectraValues[[ cent, "Ka0492plu", "AveragepT"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)
ProtonMeanPT =  Table[spectraValues[[ cent, "pr0938plu", "AveragepT"]], {cent, 5}];  (*LIST OF 5 FILES FOR EACH CENTRALITY *)

(********** Export Data ************)

Export[MultTotalFile, TotalYield];

Export[MultPionFile,   PionYield];
Export[MultKaonFile,   KaonYield];
Export[MultProtonFile, ProtonYield];

Export[PtPionFile, PionMeanPT];
Export[PtKaonFile, KaonMeanPT];
Export[PtProtonFile, ProtonMeanPT];

(***************Do Scripts*************)


graph = StringJoin["python2 ", WORKINGFOLDER, "/make_graph.py "];

GraphTotalScript = StringJoin[graph," ",     workingFolder, " ",  centBins, " ", MultTotalFile, " -b"];

Print["graph command = ", GraphTotalScript];

GraphPionScript = StringJoin[graph," ",     workingFolder, " ",  centBins, " ", MultPionFile, " -b"];
GraphKaonScript = StringJoin[graph," ",     workingFolder, " ",  centBins, " ", MultKaonFile, " -b"];
GraphProtonScript = StringJoin[graph," ",     workingFolder, " ",  centBins, " ", MultProtonFile, " -b"];

PtGraphPionScript =   StringJoin[graph," ",     workingFolder, " ",  centBins, " ", PtPionFile, " -b"];
PtGraphKaonScript =   StringJoin[graph," ",     workingFolder, " ",  centBins, " ", PtKaonFile, " -b"];
PtGraphProtonScript = StringJoin[graph," ",     workingFolder, " ",  centBins, " ", PtProtonFile, " -b"];

Run[GraphTotalScript];

Run[GraphPionScript];
Run[GraphKaonScript];
Run[GraphProtonScript];

Run[PtGraphPionScript];
Run[PtGraphKaonScript];
Run[PtGraphProtonScript];

Quit[]





