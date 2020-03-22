#include <iostream>
#include <sstream>
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TMath.h"
#include <iterator>
#include "TFile.h"
#include "TClassTable.h"
#include <vector>
#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TKey.h"
#include "TCanvas.h"
#include <math.h>
#include <fstream>
#include <string>
#include <cstdio>


using namespace std;


TH1D* DefineHist(TString check, TString scale){

   TH1D* hist;

   hist = new TH1D("hist","",100, -0.05, 3.1);
   if (scale == "log"){
     hist->SetMinimum(0.0000003);
     hist->SetMaximum(4999);
   }
   else{
     hist->SetMinimum(0.5);
     hist->SetMaximum(2.1);
   }
	   
   hist->SetStats(0);
   hist->SetLineStyle(0);
   hist->SetLineWidth(0);
   hist->SetMarkerStyle(20);
   hist->SetMarkerSize(1.0);
   hist->GetXaxis()->SetLabelOffset(0.006);
   hist->GetXaxis()->SetLabelSize(0.06);
   hist->GetXaxis()->SetTitleSize(20);
   hist->GetXaxis()->SetTitleFont(43);
   hist->GetYaxis()->SetLabelFont(43);
   hist->GetYaxis()->SetLabelSize(15);

   if (check=="P1") {

      hist->GetYaxis()->SetTitle("#frac{1}{#it{N}} #frac{1}{2#pi#it{p}_{T}}#frac{d#it{N}}{d#it{p}_{T}dy} [#it{c}^{2}/GeV^{2}]");
      hist->GetXaxis()->SetTickLength(0.03);
      hist->GetYaxis()->SetTickLength(0.03);
  
      hist->GetYaxis()->CenterTitle(true);
      hist->GetYaxis()->SetTitleOffset(2.30);
      hist->GetYaxis()->SetTitleSize(23.5);
      hist->GetYaxis()->SetTitleFont(43);

   }

   if (check=="P2") {

      hist->GetXaxis()->SetTickLength(0.03);
      hist->GetYaxis()->SetTickLength(0.04);
      hist->GetYaxis()->SetLabelSize(0);
   }

   if (check=="P3") {

      hist->GetXaxis()->SetTickLength(0.03);
      hist->GetYaxis()->SetTickLength(0.04);
      hist->GetYaxis()->SetLabelSize(0);
   }

   if (check=="P4") {

       hist->GetYaxis()->SetTitle("Data/Model");
       hist->GetXaxis()->SetTickLength(0.03);
       hist->GetYaxis()->SetTickLength(0.04);
      
       hist->GetYaxis()->CenterTitle(true);
       hist->GetYaxis()->SetTitleOffset(2.14);
       hist->GetYaxis()->SetTitleSize(25.5);
       hist->GetYaxis()->SetTitleFont(43);
       hist->GetYaxis()->SetNdivisions(505);
    
       hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
       hist->GetXaxis()->SetTitleFont(43);
       hist->GetXaxis()->SetTitleSize(25.5);
 
       hist->GetXaxis()->CenterTitle(true);
       hist->GetXaxis()->SetTitleOffset(2.14);
  
   }

   if (check=="P5") {

       hist->GetXaxis()->SetTickLength(0.03);
       hist->GetYaxis()->SetTickLength(0.05);
       hist->GetYaxis()->SetNdivisions(505);

       hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
       hist->GetXaxis()->SetTitleFont(43);
       hist->GetXaxis()->SetTitleSize(25.5);
       hist->GetXaxis()->CenterTitle(true);
       hist->GetXaxis()->SetTitleOffset(2.14);
 
       hist->GetYaxis()->SetLabelSize(0);
   }

   if (check=="P6") {

       hist->GetXaxis()->SetTickLength(0.03);
       hist->GetYaxis()->SetTickLength(0.05);
       hist->GetYaxis()->SetNdivisions(505);

       hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
       hist->GetXaxis()->SetTitleFont(43);
       hist->GetXaxis()->SetTitleSize(25.5);
 
       hist->GetXaxis()->CenterTitle(true);
       hist->GetXaxis()->SetTitleOffset(2.14);

       hist->GetYaxis()->SetLabelSize(0);
   }


   return hist;

}

void DoLegend2a(){


   TLegend *leg = new TLegend(0.05, 0.6, 0.29, 0.95, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);

   /*TLegendEntry* entry1=leg->AddEntry("", "Norm_{1} = 48.6","");
   entry1=leg->AddEntry("", "Norm_{2} = 47.8","");
   entry1=leg->AddEntry("", "Norm_{3} = 46.2","");
   entry1=leg->AddEntry("", "Norm_{4} = 43.9","");
   entry1=leg->AddEntry("", "Norm_{5} = 41.0","");*/

   TLegendEntry* entry1=leg->AddEntry("", "Norm_{1} = 54.25","");
   entry1=leg->AddEntry("", "Norm_{2} = 55.35","");
   entry1=leg->AddEntry("", "Norm_{3} = 56.19","");
   entry1=leg->AddEntry("", "Norm_{4} = 56.92","");
   entry1=leg->AddEntry("", "Norm_{5} = 56.93","");


   leg->Draw();

}

void DoLegend2(){


   TLegend *leg = new TLegend(0.32, 0.6, 0.72, 0.95, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.06);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);

   /*TLegendEntry*entry1=leg->AddEntry("", "#eta/s = 0.22","");
   entry1=leg->AddEntry("", "(#zeta/s)_{max} = 0.05","");
   entry1=leg->AddEntry("", "T_{fo} = 136.9 MeV","");
   entry1=leg->AddEntry("", "#tau_{0} = 0.27 fm/#it{c}","");*/

   TLegendEntry*entry1=leg->AddEntry("", "#eta/s = 0.163","");
   entry1=leg->AddEntry("", "(#zeta/s)_{max} = 0.058","");
   entry1=leg->AddEntry("", "T_{fo} = 137.1 MeV","");
   entry1=leg->AddEntry("", "#tau_{0} = 0.179 fm/#it{c}","");


   leg->Draw();

}

void DoLegend3(){


   TLegend *leg = new TLegend(0.45, 0.60, 0.70, 0.95, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);
   leg->SetHeader("ALICE","C");

   TLegendEntry* entry1=leg->AddEntry("", "0-5%","p");
   entry1->SetLineWidth(4);
   entry1->SetMarkerStyle(25);
   entry1->SetMarkerSize(1.2);

   TLegendEntry* entry2=leg->AddEntry("", "5-10%   #times 10^{-1}","p");
   entry2->SetLineWidth(4);
   entry2->SetMarkerStyle(24);
   entry2->SetMarkerSize(1.2);

   TLegendEntry* entry3=leg->AddEntry("", "10-20% #times 10^{-2}","p");
   entry3->SetLineWidth(4);
   entry3->SetMarkerStyle(26);
   entry3->SetMarkerSize(1.2);

   TLegendEntry* entry4=leg->AddEntry("", "20-30% #times 10^{-3}","p");
   entry4->SetLineWidth(4);
   entry4->SetMarkerStyle(27);
   entry4->SetMarkerSize(1.2);

   TLegendEntry* entry5=leg->AddEntry("", "30-40% #times 10^{-4}","p");
   entry5->SetLineWidth(4);
   entry5->SetMarkerStyle(30);
   entry5->SetMarkerSize(1.2);
   leg->Draw();

}

void DoLegend4(){


   TLegend *leg = new TLegend(0.25, 0.78, 0.60, 0.92, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.075);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);

   TLegendEntry* entry1=leg->AddEntry("", "FluiduM+FastReso","l");
   entry1->SetLineWidth(4);
   entry1->SetMarkerStyle(25);
   entry1->SetMarkerSize(1.2);
 
   leg->Draw();
}

void DoLegend(){

   TLegend *leg = new TLegend(0.05, 0.7, 0.43, 0.85, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.06);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);


   TLegendEntry* entry=leg->AddEntry("", "MCGl+FluiduM","l");
   entry->SetLineColor(kBlack);
   entry->SetLineWidth(5);

   entry=leg->AddEntry("", "IP glasma+MUSIC+UrQMD","");
   entry->SetLineColor(kMagenta);
   entry->SetFillStyle(3001);

   entry=leg->AddEntry("", "#scale[0.8]{BulkViscosityOverEntropyAmplitude = 0.03}","l");
   entry->SetLineColor(kCyan);
   entry->SetLineWidth(5);

}

void DoLatex(double x, double y, TString text){

   TLatex *   tex = new TLatex(x, y, text);
   tex->SetNDC();
   tex->SetLineWidth(2);
   tex->SetTextFont(22);
   tex->Draw();

}

void DoText(double x, double y, TString text){

   TText *t = new TText(x, y, text);
   t->SetTextFont(43);
   t->SetTextSize(17);
   t->Draw();

}

void DoText2(double x, double y, TString text){

   TText *t = new TText(x, y, text);
   t->SetTextFont(43);
   t->SetTextSize(15);
   t->Draw();

}

void DoLine(){

   TLine *line1 = new TLine(0, 1.0, 3.1, 1.0);
   line1->SetLineColor(1);
   line1->SetLineStyle(0);
   line1->Draw();

}

void MakePad(TString plot, double x_min, double y_min, double x_max, double y_max, double LeftMargin, double RightMargin, double TopMargin, double BottomMargin, TString scale){

   TPad *p_0_0 = new TPad(plot, plot, x_min, y_min, x_max, y_max);
   p_0_0->Draw();
   p_0_0->cd();
   p_0_0->SetFillColor(0);
   p_0_0->SetBorderMode(0);
   p_0_0->SetBorderSize(2);
   p_0_0->SetTickx(1);
   p_0_0->SetTicky(1);
   p_0_0->SetLeftMargin(LeftMargin);
   p_0_0->SetRightMargin(RightMargin);
   p_0_0->SetTopMargin(TopMargin);
   p_0_0->SetBottomMargin(BottomMargin);

   TH1D* hist1=DefineHist(plot, scale);
   hist1->Draw("");

}

void plot_3x2(){


   TCanvas *cc1 = new TCanvas("cc1", "cc1",40,40,1020,648);
   gStyle->SetOptStat(0);

   //////////////////////////////////////////////////
   
   Double_t W  = 0.303;          // Pad Width
   Int_t    Nx = 3;              // Number of pads along X
   Double_t Xm = (1-(Nx*W))/1;   // X Margin
   double topmargin = 0.07;

   double dim[8][8] = {
                                  // Margins  
  // xmin,  ymin, xmax,  ymax     // Left, Right,  Top,   Botttom

    {0,      0.512,  Xm+W,    1,     0.23,    0.00,    topmargin, 0},
    {Xm+W,   0.512,  Xm+2*W,  1,     0.002,   0.00,    topmargin, 0},
    {Xm+2*W, 0.512,  Xm+3*W,  1,     0.002,   0.01,    topmargin, 0},
    {0,      0.02,   Xm+W,    0.512, 0.23,    0.00,    0,         0.35},  // bottom  1 
    {Xm+W,   0.02,   Xm+2*W,  0.512, 0.002,   0.00,    0,         0.35},  // bottom  2
    {Xm+2*W, 0.02,   Xm+3*W,  0.512, 0.002,   0.01,    0,         0.35}   // bottom  3

                      };

  //////////////////////////////////////////////////////////////////////////////////////////////
  // HEP data
  // ///////////////////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////////////////////
  //  pion

  TString HYDRO_DATA_PATH = "output_folder";
  //TString HYDRO_DATA_PATH = "BEST-FIT-p0";

  auto f = new TFile("./ALICE-DATA/HEPData-ins1222333-v1-root.root", "READ");

  TDirectory* dir05 = f->GetDirectory("Table 1");
  TGraphAsymmErrors* mgPionPlus05;
  dir05->GetObject("Graph1D_y1", mgPionPlus05);

  TDirectory* dir510 = f->GetDirectory("Table 2");
  TGraphAsymmErrors* mgPionPlus510;
  dir510->GetObject("Graph1D_y1", mgPionPlus510);

  TDirectory* dir1020 = f->GetDirectory("Table 3");
  TGraphAsymmErrors* mgPionPlus1020;
  dir1020->GetObject("Graph1D_y1", mgPionPlus1020);

  TDirectory* dir2030 = f->GetDirectory("Table 4");
  TGraphAsymmErrors* mgPionPlus2030;
  dir2030->GetObject("Graph1D_y1", mgPionPlus2030);

  TDirectory* dir3040 = f->GetDirectory("Table 5");
  TGraphAsymmErrors* mgPionPlus3040;
  dir3040->GetObject("Graph1D_y1", mgPionPlus3040);

  double scaleFit = 1;

  for (int i=0; i<mgPionPlus510->GetN(); i++) mgPionPlus510->GetY()[i] *= scaleFit*0.1; 
  for (int i=0; i<mgPionPlus510->GetN(); i++) mgPionPlus510->SetPointEYhigh(i, mgPionPlus510->GetErrorYhigh(i) * scaleFit*0.1); 
  for (int i=0; i<mgPionPlus510->GetN(); i++) mgPionPlus510->SetPointEYlow(i, mgPionPlus510->GetErrorYlow(i) * scaleFit*0.1); 

  for (int i=0; i<mgPionPlus1020->GetN(); i++) mgPionPlus1020->GetY()[i] *= scaleFit*0.01; 
  for (int i=0; i<mgPionPlus1020->GetN(); i++) mgPionPlus1020->SetPointEYhigh(i, mgPionPlus1020->GetErrorYhigh(i) * scaleFit*0.01); 
  for (int i=0; i<mgPionPlus1020->GetN(); i++) mgPionPlus1020->SetPointEYlow(i, mgPionPlus1020->GetErrorYlow(i) * scaleFit*0.01); 

  for (int i=0; i<mgPionPlus2030->GetN(); i++) mgPionPlus2030->GetY()[i] *= scaleFit*0.001; 
  for (int i=0; i<mgPionPlus2030->GetN(); i++) mgPionPlus2030->SetPointEYhigh(i, mgPionPlus2030->GetErrorYhigh(i) * scaleFit*0.001); 
  for (int i=0; i<mgPionPlus2030->GetN(); i++) mgPionPlus2030->SetPointEYlow(i, mgPionPlus2030->GetErrorYlow(i) * scaleFit*0.001); 

  for (int i=0; i<mgPionPlus3040->GetN(); i++) mgPionPlus3040->GetY()[i] *= scaleFit*0.0001; 
  for (int i=0; i<mgPionPlus3040->GetN(); i++) mgPionPlus3040->SetPointEYhigh(i, mgPionPlus3040->GetErrorYhigh(i) * scaleFit*0.0001); 
  for (int i=0; i<mgPionPlus3040->GetN(); i++) mgPionPlus3040->SetPointEYlow(i, mgPionPlus3040->GetErrorYlow(i) * scaleFit*0.0001); 

  auto fPion = new TFile(HYDRO_DATA_PATH + "/0-5/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro05 = (TGraph*)fPion->Get("Graph");

  auto fPion510 = new TFile( HYDRO_DATA_PATH + "/5-10/pion/fit_graph_spectra_1.root", "READ"); 
  TGraph* mgPionPlusHydro510 = (TGraph*)fPion510->Get("Graph");
  for (int i=0; i<mgPionPlusHydro510->GetN(); i++) mgPionPlusHydro510->GetY()[i] *= scaleFit*0.1; 

  auto fPion1020 = new TFile(HYDRO_DATA_PATH + "/10-20/pion/fit_graph_spectra_1.root", "READ"); 
  TGraph* mgPionPlusHydro1020 = (TGraph*)fPion1020->Get("Graph");
  for (int i=0; i<mgPionPlusHydro1020->GetN(); i++) mgPionPlusHydro1020->GetY()[i] *= scaleFit*0.01; 

  auto fPion2030 = new TFile(HYDRO_DATA_PATH + "/20-30/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro2030 = (TGraph*)fPion2030->Get("Graph");
  for (int i=0; i<mgPionPlusHydro2030->GetN(); i++) mgPionPlusHydro2030->GetY()[i] *= scaleFit*0.001; 

  auto fPion3040 = new TFile(HYDRO_DATA_PATH + "/30-40/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro3040 = (TGraph*)fPion3040->Get("Graph");
  for (int i=0; i<mgPionPlusHydro3040->GetN(); i++) mgPionPlusHydro3040->GetY()[i] *= scaleFit*0.0001; 
 
  // ratio
 
  auto fPion05Ratio = new TFile(HYDRO_DATA_PATH + "/0-5/pion/ratio_eval_fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro05Ratio = (TGraph*)fPion05Ratio->Get("Graph");
  
  auto fPion510Ratio = new TFile(HYDRO_DATA_PATH + "/5-10/pion/ratio_eval_fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro510Ratio = (TGraph*)fPion510Ratio->Get("Graph");
  
  auto fPion1020Ratio = new TFile(HYDRO_DATA_PATH + "/10-20/pion/ratio_eval_fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro1020Ratio = (TGraph*)fPion1020Ratio->Get("Graph");
  
  auto fPion2030Ratio = new TFile(HYDRO_DATA_PATH + "/20-30/pion/ratio_eval_fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro2030Ratio = (TGraph*)fPion2030Ratio->Get("Graph");
  
  auto fPion3040Ratio = new TFile(HYDRO_DATA_PATH + "/30-40/pion/ratio_eval_fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro3040Ratio = (TGraph*)fPion3040Ratio->Get("Graph");
  
  

  ////////////////////////////////////////////////////////////////////////////////////////////////// 
  // kaon

  TDirectory* kdir05 = f->GetDirectory("Table 11");
  TGraphAsymmErrors* mgKaonPlus05;
  kdir05->GetObject("Graph1D_y1", mgKaonPlus05);

  TDirectory* kdir510 = f->GetDirectory("Table 12");
  TGraphAsymmErrors* mgKaonPlus510;
  kdir510->GetObject("Graph1D_y1", mgKaonPlus510);

  TDirectory* kdir1020 = f->GetDirectory("Table 13");
  TGraphAsymmErrors* mgKaonPlus1020;
  kdir1020->GetObject("Graph1D_y1", mgKaonPlus1020);

  TDirectory* kdir2030 = f->GetDirectory("Table 14");
  TGraphAsymmErrors* mgKaonPlus2030;
  kdir2030->GetObject("Graph1D_y1", mgKaonPlus2030);

  TDirectory* kdir3040 = f->GetDirectory("Table 15");
  TGraphAsymmErrors* mgKaonPlus3040;
  kdir3040->GetObject("Graph1D_y1", mgKaonPlus3040);


  for (int i=0; i<mgKaonPlus510->GetN(); i++) mgKaonPlus510->GetY()[i] *= scaleFit*0.1;
  for (int i=0; i<mgKaonPlus510->GetN(); i++) mgKaonPlus510->SetPointEYhigh(i, mgKaonPlus510->GetErrorYhigh(i) * scaleFit*0.1);
  for (int i=0; i<mgKaonPlus510->GetN(); i++) mgKaonPlus510->SetPointEYlow(i, mgKaonPlus510->GetErrorYlow(i) * scaleFit*0.1);

  for (int i=0; i<mgKaonPlus1020->GetN(); i++) mgKaonPlus1020->GetY()[i] *= scaleFit*0.01;
  for (int i=0; i<mgKaonPlus1020->GetN(); i++) mgKaonPlus1020->SetPointEYhigh(i, mgKaonPlus1020->GetErrorYhigh(i) * scaleFit*0.01);
  for (int i=0; i<mgKaonPlus1020->GetN(); i++) mgKaonPlus1020->SetPointEYlow(i, mgKaonPlus1020->GetErrorYlow(i) * scaleFit*0.01);

  for (int i=0; i<mgKaonPlus2030->GetN(); i++) mgKaonPlus2030->GetY()[i] *= scaleFit*0.001;
  for (int i=0; i<mgKaonPlus2030->GetN(); i++) mgKaonPlus2030->SetPointEYhigh(i, mgKaonPlus2030->GetErrorYhigh(i) * scaleFit*0.001);
  for (int i=0; i<mgKaonPlus2030->GetN(); i++) mgKaonPlus2030->SetPointEYlow(i, mgKaonPlus2030->GetErrorYlow(i) * scaleFit*0.001);

  for (int i=0; i<mgKaonPlus3040->GetN(); i++) mgKaonPlus3040->GetY()[i] *= scaleFit*0.0001;
  for (int i=0; i<mgKaonPlus3040->GetN(); i++) mgKaonPlus3040->SetPointEYhigh(i, mgKaonPlus3040->GetErrorYhigh(i) * scaleFit*0.0001);
  for (int i=0; i<mgKaonPlus3040->GetN(); i++) mgKaonPlus3040->SetPointEYlow(i, mgKaonPlus3040->GetErrorYlow(i) * scaleFit*0.0001);

  auto fKaon = new TFile(HYDRO_DATA_PATH + "/0-5/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro05 = (TGraph*)fKaon->Get("Graph");

  auto fKaon510 = new TFile(HYDRO_DATA_PATH + "/5-10/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro510 = (TGraph*)fKaon510->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro510->GetN(); i++) mgKaonPlusHydro510->GetY()[i] *= scaleFit*0.1; 

  auto fKaon1020 = new TFile(HYDRO_DATA_PATH + "/10-20/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro1020 = (TGraph*)fKaon1020->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro1020->GetN(); i++) mgKaonPlusHydro1020->GetY()[i] *= scaleFit*0.01; 

  auto fKaon2030 = new TFile(HYDRO_DATA_PATH + "/20-30/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro2030 = (TGraph*)fKaon2030->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro2030->GetN(); i++) mgKaonPlusHydro2030->GetY()[i] *= scaleFit*0.001; 

  auto fKaon3040 = new TFile(HYDRO_DATA_PATH + "/30-40/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro3040 = (TGraph*)fKaon3040->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro3040->GetN(); i++) mgKaonPlusHydro3040->GetY()[i] *= scaleFit*0.0001; 
  
  auto fKaon05Ratio = new TFile(HYDRO_DATA_PATH + "/0-5/kaon/ratio_eval_fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro05Ratio = (TGraph*)fKaon05Ratio->Get("Graph");
  
  auto fKaon510Ratio = new TFile(HYDRO_DATA_PATH + "/5-10/kaon/ratio_eval_fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro510Ratio = (TGraph*)fKaon510Ratio->Get("Graph");
  
  auto fKaon1020Ratio = new TFile(HYDRO_DATA_PATH + "/10-20/kaon/ratio_eval_fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro1020Ratio = (TGraph*)fKaon1020Ratio->Get("Graph");
  
  auto fKaon2030Ratio = new TFile(HYDRO_DATA_PATH + "/20-30/kaon/ratio_eval_fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro2030Ratio = (TGraph*)fKaon2030Ratio->Get("Graph");
  
  auto fKaon3040Ratio = new TFile(HYDRO_DATA_PATH + "/30-40/kaon/ratio_eval_fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro3040Ratio = (TGraph*)fKaon3040Ratio->Get("Graph");
  
 
  ///////////////////////////////////////////////////////////////////////////////////////////////////
  // proton

  TDirectory* prdir05 = f->GetDirectory("Table 21");
  TGraphAsymmErrors* mgProtonPlus05;
  prdir05->GetObject("Graph1D_y1", mgProtonPlus05);

  TDirectory* prdir510 = f->GetDirectory("Table 22");
  TGraphAsymmErrors* mgProtonPlus510;
  prdir510->GetObject("Graph1D_y1", mgProtonPlus510);

  TDirectory* prdir1020 = f->GetDirectory("Table 23");
  TGraphAsymmErrors* mgProtonPlus1020;
  prdir1020->GetObject("Graph1D_y1", mgProtonPlus1020);

  TDirectory* prdir2030 = f->GetDirectory("Table 24");
  TGraphAsymmErrors* mgProtonPlus2030;
  prdir2030->GetObject("Graph1D_y1", mgProtonPlus2030);

  TDirectory* prdir3040 = f->GetDirectory("Table 25");
  TGraphAsymmErrors* mgProtonPlus3040;
  prdir3040->GetObject("Graph1D_y1", mgProtonPlus3040);


  for (int i=0; i<mgProtonPlus510->GetN(); i++) mgProtonPlus510->GetY()[i] *= scaleFit*0.1;
  for (int i=0; i<mgProtonPlus510->GetN(); i++) mgProtonPlus510->SetPointEYhigh(i, mgKaonPlus510->GetErrorYhigh(i) * scaleFit*0.1);
  for (int i=0; i<mgProtonPlus510->GetN(); i++) mgProtonPlus510->SetPointEYlow(i, mgKaonPlus510->GetErrorYlow(i) * scaleFit*0.1);

  for (int i=0; i<mgProtonPlus1020->GetN(); i++) mgProtonPlus1020->GetY()[i] *= scaleFit*0.01;
  for (int i=0; i<mgProtonPlus1020->GetN(); i++) mgProtonPlus1020->SetPointEYhigh(i, mgKaonPlus1020->GetErrorYhigh(i) *scaleFit*0.01);   //
  for (int i=0; i<mgProtonPlus1020->GetN(); i++) mgProtonPlus1020->SetPointEYlow(i, mgKaonPlus1020->GetErrorYlow(i) *scaleFit*0.01);

  for (int i=0; i<mgProtonPlus2030->GetN(); i++) mgProtonPlus2030->GetY()[i] *= scaleFit*0.001;
  for (int i=0; i<mgProtonPlus2030->GetN(); i++) mgProtonPlus2030->SetPointEYhigh(i, mgKaonPlus2030->GetErrorYhigh(i) *scaleFit*0.001);
  for (int i=0; i<mgProtonPlus2030->GetN(); i++) mgProtonPlus2030->SetPointEYlow(i, mgKaonPlus2030->GetErrorYlow(i) *scaleFit*0.001);

  for (int i=0; i<mgProtonPlus3040->GetN(); i++) mgProtonPlus3040->GetY()[i] *= scaleFit*0.0001;
  for (int i=0; i<mgProtonPlus3040->GetN(); i++) mgProtonPlus3040->SetPointEYhigh(i, mgKaonPlus3040->GetErrorYhigh(i) * scaleFit*0.0001);
  for (int i=0; i<mgProtonPlus3040->GetN(); i++) mgProtonPlus3040->SetPointEYlow(i, mgKaonPlus3040->GetErrorYlow(i) * scaleFit*0.0001);
 
  auto fProton = new TFile(HYDRO_DATA_PATH + "/0-5/proton/fit_graph_spectra_3.root", "READ"); 
  TGraph* mgProtonPlusHydro05 = (TGraph*)fProton->Get("Graph");

  auto fProton510 = new TFile(HYDRO_DATA_PATH + "/5-10/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro510 = (TGraph*)fProton510->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro510->GetN(); i++) mgProtonPlusHydro510->GetY()[i] *= scaleFit*0.1; 

  auto fProton1020 = new TFile(HYDRO_DATA_PATH + "/10-20/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro1020 = (TGraph*)fProton1020->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro1020->GetN(); i++) mgProtonPlusHydro1020->GetY()[i] *= scaleFit*0.01; 

  auto fProton2030 = new TFile(HYDRO_DATA_PATH + "/20-30/proton/fit_graph_spectra_3.root", "READ"); 
  TGraph* mgProtonPlusHydro2030 = (TGraph*)fProton2030->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro2030->GetN(); i++) mgProtonPlusHydro2030->GetY()[i] *= scaleFit*0.001; 

  auto fProton3040 = new TFile(HYDRO_DATA_PATH + "/30-40/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro3040 = (TGraph*)fProton3040->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro3040->GetN(); i++) mgProtonPlusHydro3040->GetY()[i] *= scaleFit*0.0001; 
  
  auto fProton05Ratio = new TFile(HYDRO_DATA_PATH + "/0-5/proton/ratio_eval_fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro05Ratio = (TGraph*)fProton05Ratio->Get("Graph");
  
  auto fProton510Ratio = new TFile(HYDRO_DATA_PATH + "/5-10/proton/ratio_eval_fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro510Ratio = (TGraph*)fProton510Ratio->Get("Graph");
  
  auto fProton1020Ratio = new TFile(HYDRO_DATA_PATH + "/10-20/proton/ratio_eval_fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro1020Ratio = (TGraph*)fProton1020Ratio->Get("Graph");
  
  auto fProton2030Ratio = new TFile(HYDRO_DATA_PATH + "/20-30/proton/ratio_eval_fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro2030Ratio = (TGraph*)fProton2030Ratio->Get("Graph");
  
  auto fProton3040Ratio = new TFile(HYDRO_DATA_PATH + "/30-40/proton/ratio_eval_fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro3040Ratio = (TGraph*)fProton3040Ratio->Get("Graph");

  mgProtonPlus05->RemovePoint(34);
  mgProtonPlus510->RemovePoint(34);
  mgProtonPlus1020->RemovePoint(34);
  mgProtonPlus2030->RemovePoint(34);
  mgProtonPlus3040->RemovePoint(34);

  /////////////////////////////////////////////////////////////////////////////////////////////////
  // PLOTTING
  /////////////////////////////////////////////////////////////////////////////////////////////////


  TString plot; 
  TAxis *axis;

  for(int cent=0; cent<6; cent++) {

      plot.Form("%d", cent+1);
      
      if (cent==0 || cent==1 || cent==2) {
              MakePad("P"+plot,dim[cent][0], dim[cent][1], dim[cent][2], dim[cent][3], dim[cent][4], dim[cent][5], dim[cent][6], dim[cent][7], "log");
      }

      if (cent==3 || cent==4 || cent==5) {
	      MakePad("P"+plot,dim[cent][0], dim[cent][1], dim[cent][2], dim[cent][3], dim[cent][4], dim[cent][5], dim[cent][6], dim[cent][7], "non-log"); 
              DoLine();
      }	      

      if (cent==0 || cent==1 || cent==2) gPad->SetLogy();
      if (cent == 0) {

	DoLatex(0.7, 0.7, "#scale[2.0]{#pi^{+}}");  


        mgPionPlus05->SetMarkerColor(kRed);
        mgPionPlus05->SetMarkerStyle(25);
	mgPionPlus05->Draw("p");

        mgPionPlus510->SetMarkerColor(kRed);
        mgPionPlus510->SetMarkerStyle(24);
	mgPionPlus510->Draw("p");

        mgPionPlus1020->SetMarkerColor(kRed);
        mgPionPlus1020->SetMarkerStyle(26);
        mgPionPlus1020->SetMarkerSize(1.4);
	mgPionPlus1020->Draw("p");

        mgPionPlus2030->SetMarkerColor(kRed);
        mgPionPlus2030->SetMarkerStyle(27);
        mgPionPlus2030->SetMarkerSize(1.5);
	mgPionPlus2030->Draw("p");

        mgPionPlus3040->SetMarkerColor(kRed);
        mgPionPlus3040->SetMarkerStyle(30);
        mgPionPlus3040->SetMarkerSize(1.5);
	mgPionPlus3040->Draw("p");

        mgPionPlusHydro05->SetLineWidth(2);
        mgPionPlusHydro05->Draw("l");

        mgPionPlusHydro510->SetLineWidth(2);
        mgPionPlusHydro510->Draw("l");
 
        mgPionPlusHydro1020->SetLineWidth(2);
        mgPionPlusHydro1020->Draw("l");
 
        mgPionPlusHydro2030->SetLineWidth(2);
        mgPionPlusHydro2030->Draw("l");
 
        mgPionPlusHydro3040->SetLineWidth(2);
        mgPionPlusHydro3040->Draw("l");
 
      }

      if (cent == 1) { 
  
	DoLatex(0.7,0.7, "#scale[2.0]{K^{+}}");  
        DoLegend4();

        mgKaonPlus05->SetMarkerColor(kGreen + 2);
        mgKaonPlus05->SetMarkerStyle(25);
	mgKaonPlus05->Draw("p");

        mgKaonPlus510->SetMarkerColor(kGreen + 2);
        mgKaonPlus510->SetMarkerStyle(24);
	mgKaonPlus510->Draw("p");

        mgKaonPlus1020->SetMarkerColor(kGreen + 2);
        mgKaonPlus1020->SetMarkerStyle(26);
        mgKaonPlus1020->SetMarkerSize(1.4);
	mgKaonPlus1020->Draw("p");

        mgKaonPlus2030->SetMarkerColor(kGreen + 2);
        mgKaonPlus2030->SetMarkerStyle(27);
        mgKaonPlus2030->SetMarkerSize(1.5);
	mgKaonPlus2030->Draw("p");

        mgKaonPlus3040->SetMarkerColor(kGreen + 2);
        mgKaonPlus3040->SetMarkerStyle(30);
        mgKaonPlus3040->SetMarkerSize(1.5);
	mgKaonPlus3040->Draw("p");

        mgKaonPlusHydro05->SetLineWidth(2);
        mgKaonPlusHydro05->Draw("l");

        mgKaonPlusHydro510->SetLineWidth(2);
        mgKaonPlusHydro510->Draw("l");
 
        mgKaonPlusHydro1020->SetLineWidth(2);
        mgKaonPlusHydro1020->Draw("l");
 
        mgKaonPlusHydro2030->SetLineWidth(2);
        mgKaonPlusHydro2030->Draw("l");
 
        mgKaonPlusHydro3040->SetLineWidth(2);
        mgKaonPlusHydro3040->Draw("l");

      }	

      if (cent == 2) { 
  
	DoLatex(0.7,0.7, "#scale[2.0]{p}");  
	DoLatex(0.23, 0.80, "#scale[1.3]{Pb-Pb, #sqrt{s_{NN}} = 2.76 TeV}");  

        mgProtonPlus05->SetMarkerColor(kBlue);
        mgProtonPlus05->SetMarkerStyle(25);
	mgProtonPlus05->Draw("p");

        mgProtonPlus510->SetMarkerColor(kBlue) ;
        mgProtonPlus510->SetMarkerStyle(24);
	mgProtonPlus510->Draw("p");

        mgProtonPlus1020->SetMarkerColor(kBlue);
        mgProtonPlus1020->SetMarkerStyle(26);
        mgProtonPlus1020->SetMarkerSize(1.4);
	mgProtonPlus1020->Draw("p");

        mgProtonPlus2030->SetMarkerColor(kBlue);
        mgProtonPlus2030->SetMarkerStyle(27);
        mgProtonPlus2030->SetMarkerSize(1.5);
	mgProtonPlus2030->Draw("p");

        mgProtonPlus3040->SetMarkerColor(kBlue);
        mgProtonPlus3040->SetMarkerStyle(30);
        mgProtonPlus3040->SetMarkerSize(1.5);
	mgProtonPlus3040->Draw("p");

        mgProtonPlusHydro05->SetLineWidth(2);
        mgProtonPlusHydro05->Draw("l");

        mgProtonPlusHydro510->SetLineWidth(2);
        mgProtonPlusHydro510->Draw("l");
 
        mgProtonPlusHydro1020->SetLineWidth(2);
        mgProtonPlusHydro1020->Draw("l");
 
        mgProtonPlusHydro2030->SetLineWidth(2);
        mgProtonPlusHydro2030->Draw("l");
 
        mgProtonPlusHydro3040->SetLineWidth(2);
        mgProtonPlusHydro3040->Draw("l");
 

      }

      if (cent == 3) {
	      

        DoLegend3();
        mgPionPlusHydro05Ratio->SetFillColor(kRed-7);
        mgPionPlusHydro05Ratio->SetFillStyle(3001);
        mgPionPlusHydro05Ratio->Draw(" 4 c"); 

        //mgPionPlusHydro510Ratio->SetFillColor(kRed -4);
        mgPionPlusHydro510Ratio->SetFillColor(kRed-7);
        mgPionPlusHydro510Ratio->SetFillStyle(3001);
        mgPionPlusHydro510Ratio->Draw("4 c"); 
   
        //mgPionPlusHydro1020Ratio->SetFillColor(kRed - 7);
        mgPionPlusHydro1020Ratio->SetFillColor(kRed-7);
        mgPionPlusHydro1020Ratio->SetFillStyle(3001);
        mgPionPlusHydro1020Ratio->Draw("4 c"); 

        //mgPionPlusHydro2030Ratio->SetFillColor(kRed - 9);
        mgPionPlusHydro2030Ratio->SetFillColor(kRed-7);
        mgPionPlusHydro2030Ratio->SetFillStyle(3001);
        mgPionPlusHydro2030Ratio->Draw("4 c"); 

        //mgPionPlusHydro3040Ratio->SetFillColor(kRed - 10);
        mgPionPlusHydro3040Ratio->SetFillColor(kRed-7);
        mgPionPlusHydro3040Ratio->SetFillStyle(3001);
        mgPionPlusHydro3040Ratio->Draw("4 c"); 

      }	

      if (cent == 4) {


        DoLegend2();

        mgKaonPlusHydro05Ratio->SetFillColor(kGreen-7);
        mgKaonPlusHydro05Ratio->SetFillStyle(3001);
        mgKaonPlusHydro05Ratio->Draw(" 4 c"); 

        //mgKaonPlusHydro510Ratio->SetFillColor(kGreen -4);
        mgKaonPlusHydro510Ratio->SetFillColor(kGreen-7);
        mgKaonPlusHydro510Ratio->SetFillStyle(3001);
        mgKaonPlusHydro510Ratio->Draw("4 c"); 
   
        //mgKaonPlusHydro1020Ratio->SetFillColor(kGreen - 7);
        mgKaonPlusHydro1020Ratio->SetFillColor(kGreen-7);
        mgKaonPlusHydro1020Ratio->SetFillStyle(3001);
        mgKaonPlusHydro1020Ratio->Draw("4 c"); 

        //mgKaonPlusHydro2030Ratio->SetFillColor(kGreen - 9);
        mgKaonPlusHydro2030Ratio->SetFillColor(kGreen-7);
        mgKaonPlusHydro2030Ratio->SetFillStyle(3001);
        mgKaonPlusHydro2030Ratio->Draw("4 c"); 

        //mgKaonPlusHydro3040Ratio->SetFillColor(kGreen - 10);
        mgKaonPlusHydro3040Ratio->SetFillColor(kGreen-7);
        mgKaonPlusHydro3040Ratio->SetFillStyle(3001);
        mgKaonPlusHydro3040Ratio->Draw("4 c"); 
 
      }


      if (cent == 5) {

        
        DoLegend2a();
	DoLatex(0.6, 0.9, "#scale[1.0]{#chi^{2}/N_{dof} = 1.37}");  

        mgProtonPlusHydro05Ratio->SetFillColor(kBlue-7);
        mgProtonPlusHydro05Ratio->SetFillStyle(3001);
        mgProtonPlusHydro05Ratio->Draw(" 4 c"); 

        //mgProtonPlusHydro510Ratio->SetFillColor(kBlue -4);
        mgProtonPlusHydro510Ratio->SetFillColor(kBlue-7);
        mgProtonPlusHydro510Ratio->SetFillStyle(3001);
        mgProtonPlusHydro510Ratio->Draw("4 c"); 
   
        //mgProtonPlusHydro1020Ratio->SetFillColor(kBlue - 7);
        mgProtonPlusHydro1020Ratio->SetFillColor(kBlue-7);
        mgProtonPlusHydro1020Ratio->SetFillStyle(3001);
        mgProtonPlusHydro1020Ratio->Draw("4 c"); 

        //mgProtonPlusHydro2030Ratio->SetFillColor(kBlue - 9);
        mgProtonPlusHydro2030Ratio->SetFillColor(kBlue-7);
        mgProtonPlusHydro2030Ratio->SetFillStyle(3001);
        mgProtonPlusHydro2030Ratio->Draw("4 c"); 

        //mgProtonPlusHydro3040Ratio->SetFillColor(kBlue - 10);
        mgProtonPlusHydro3040Ratio->SetFillColor(kBlue-7);
        mgProtonPlusHydro3040Ratio->SetFillStyle(3001);
        mgProtonPlusHydro3040Ratio->Draw("4 c"); 
 
        gPad->SetBorderSize(0);

      }

      cc1->cd();

   }

   cc1->SaveAs("Figure_3x2.pdf");
   ////////////////////////////////////////////////

   
}
