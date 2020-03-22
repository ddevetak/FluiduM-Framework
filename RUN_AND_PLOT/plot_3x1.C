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

   TH1D* hist = new TH1D("hist","",100, -0.1, 3.1);
   if (scale == "log"){
     hist->SetMinimum(0.0000002);
     hist->SetMaximum(9999);
   }
	   
   hist->SetStats(0);
   hist->SetLineStyle(0);
   hist->SetLineWidth(0);

   if (check=="P1") {

      hist->GetYaxis()->SetTitle("#frac{1}{#it{N}} #frac{1}{2#pi#it{p}_{T}}#frac{d#it{N}}{d#it{p}_{T}dy} [#it{c}^{2}/GeV^{2}]");
      hist->GetXaxis()->SetTickLength(0.03);
      hist->GetYaxis()->SetTickLength(0.03);

      hist->GetYaxis()->CenterTitle(true);
      hist->GetYaxis()->SetTitleOffset(1.8);
      hist->GetYaxis()->SetTitleSize(24.5);
      hist->GetYaxis()->SetLabelSize(0.04);
      hist->GetYaxis()->SetTitleFont(43);

      hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
      hist->GetXaxis()->SetTitleFont(43);
      hist->GetXaxis()->SetTitleSize(25.5);

      hist->GetXaxis()->CenterTitle(true);
      hist->GetXaxis()->SetTitleOffset(1.24);
      hist->GetXaxis()->SetLabelOffset(0.014);

      hist->GetXaxis()->SetLabelSize(0.05);
   }

   if (check=="P2") {

      hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
      hist->GetXaxis()->SetTitleFont(45);
      hist->GetXaxis()->SetTitleSize(25.5);

      hist->GetXaxis()->CenterTitle(true);
      hist->GetXaxis()->SetTitleOffset(1.2);
      hist->GetXaxis()->SetLabelOffset(0.005);

      hist->GetXaxis()->SetLabelSize(0.06);

   }

    if (check=="P3") {

      hist->GetXaxis()->SetTitle("#it{p}_{T} [GeV/#it{c}]");
      hist->GetXaxis()->SetTitleFont(45);
      hist->GetXaxis()->SetTitleSize(25.5);

      hist->GetXaxis()->CenterTitle(true);
      hist->GetXaxis()->SetTitleOffset(1.2);
      hist->GetXaxis()->SetLabelOffset(0.005);

      hist->GetXaxis()->SetLabelSize(0.06);

   }


   return hist;

}


void DoLegend2(){


   TLegend *leg = new TLegend(0.3, 0.85, 0.68, 0.88, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.06);
   leg->SetHeader("FluiduM+FastReso","");
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);

   leg->Draw();

}

void DoLegend3(TGraph* h1, TGraph* h2, TGraph* h3, TGraph* h4, TGraph* h5){


   TLegend *leg = new TLegend(0.25, 0.25, 0.50, 0.45, NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.03);
   leg->SetLineColor(1);
   leg->SetLineStyle(2);
   leg->SetLineWidth(3);

   TLegendEntry* entry1=leg->AddEntry(h1, "0-5%","l");
   entry1->SetLineWidth(4);
   entry1->SetMarkerStyle(25);
   entry1->SetMarkerSize(1.2);

   TLegendEntry* entry2=leg->AddEntry(h2, "5-10%   #times 10^{-1}","l");
   entry2->SetLineWidth(4);
   entry2->SetMarkerStyle(24);
   entry2->SetMarkerSize(1.2);

   TLegendEntry* entry3=leg->AddEntry(h3, "10-20% #times 10^{-2}","l");
   entry3->SetLineWidth(4);
   entry3->SetMarkerStyle(26);
   entry3->SetMarkerSize(1.2);

   TLegendEntry* entry4=leg->AddEntry(h4, "20-30% #times 10^{-3}","l");
   entry4->SetLineWidth(4);
   entry4->SetMarkerStyle(27);
   entry4->SetMarkerSize(1.2);

   TLegendEntry* entry5=leg->AddEntry(h5, "30-40% #times 10^{-4}","l");
   entry5->SetLineWidth(4);
   entry5->SetMarkerStyle(30);
   entry5->SetMarkerSize(1.2);
   leg->Draw();

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

void plot_3x1(){


   TCanvas *cc1 = new TCanvas("cc1", "cc1",40, 40, 1205, 500);
   gStyle->SetOptStat(0);

   //////////////////////////////////////////////////

   Double_t W  = 0.303;          // Pad Width
   Int_t    Nx = 3;              // Number of pads along X
   Double_t Xm = (1-(Nx*W))/1;   // X Margin
   double topmargin = 0.07;

   double dim[8][8] = {
                                     // Margins
                                     // Left, Right,  Top,   Botttom

    {0,      0.01,  Xm+W,    1,     0.23,    0.00,    topmargin, 0.20},
    {Xm+W,   0.01,  Xm+2*W,  1,     0.002,   0.00,    topmargin, 0.20},
    {Xm+2*W, 0.01,  Xm+3*W,  1,     0.002,   0.01,    topmargin, 0.20}

                      };
   

  //////////////////////////////////////////////////////////////////////////////////////////////
  // HEP data
  // ///////////////////////////////////////////////////////////////////////////////////////////

  ////////////  HYDRO   

  double FitScale = 1.0;
 

  ////////////////////////////////////////////////////

  TString HYDRO_DATA_PATH  = "output_folder";

  auto fPion = new TFile(HYDRO_DATA_PATH + "/0-5/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro05 = (TGraph*)fPion->Get("Graph");

  auto fPion510 = new TFile(HYDRO_DATA_PATH + "/5-10/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro510 = (TGraph*)fPion510->Get("Graph");
  for (int i=0; i<mgPionPlusHydro510->GetN(); i++) mgPionPlusHydro510->GetY()[i] *= FitScale*0.1; 

  auto fPion1020 = new TFile(HYDRO_DATA_PATH + "/10-20/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro1020 = (TGraph*)fPion1020->Get("Graph");
  for (int i=0; i<mgPionPlusHydro1020->GetN(); i++) mgPionPlusHydro1020->GetY()[i] *= FitScale*0.01; 

  auto fPion2030 = new TFile(HYDRO_DATA_PATH + "/20-30/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro2030 = (TGraph*)fPion2030->Get("Graph");
  for (int i=0; i<mgPionPlusHydro2030->GetN(); i++) mgPionPlusHydro2030->GetY()[i] *= FitScale*0.001; 

  auto fPion3040 = new TFile(HYDRO_DATA_PATH + "/30-40/pion/fit_graph_spectra_1.root", "READ");  
  TGraph* mgPionPlusHydro3040 = (TGraph*)fPion3040->Get("Graph");
  for (int i=0; i<mgPionPlusHydro3040->GetN(); i++) mgPionPlusHydro3040->GetY()[i] *= FitScale*0.0001; 
 

  ////////////////////////////////////////////////////////////////////////////////////////////////// 
  // kaon

  auto fKaon = new TFile(HYDRO_DATA_PATH + "/0-5/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro05 = (TGraph*)fKaon->Get("Graph");

  auto fKaon510 = new TFile(HYDRO_DATA_PATH + "/5-10/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro510 = (TGraph*)fKaon510->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro510->GetN(); i++) mgKaonPlusHydro510->GetY()[i] *= FitScale*0.1; 

  auto fKaon1020 = new TFile(HYDRO_DATA_PATH + "/10-20/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro1020 = (TGraph*)fKaon1020->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro1020->GetN(); i++) mgKaonPlusHydro1020->GetY()[i] *= FitScale*0.01; 

  auto fKaon2030 = new TFile(HYDRO_DATA_PATH + "/20-30/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro2030 = (TGraph*)fKaon2030->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro2030->GetN(); i++) mgKaonPlusHydro2030->GetY()[i] *= FitScale*0.001; 

  auto fKaon3040 = new TFile(HYDRO_DATA_PATH + "/30-40/kaon/fit_graph_spectra_2.root", "READ");  
  TGraph* mgKaonPlusHydro3040 = (TGraph*)fKaon3040->Get("Graph");
  for (int i=0; i<mgKaonPlusHydro3040->GetN(); i++) mgKaonPlusHydro3040->GetY()[i] *= FitScale*0.0001; 
  

  ///////////////////////////////////////////////////////////////////////////////////////////////////
  // proton

   auto fProton = new TFile(HYDRO_DATA_PATH + "/0-5/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro05 = (TGraph*)fProton->Get("Graph");

  auto fProton510 = new TFile(HYDRO_DATA_PATH + "/5-10/proton/fit_graph_spectra_3.root", "READ"); 
  TGraph* mgProtonPlusHydro510 = (TGraph*)fProton510->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro510->GetN(); i++) mgProtonPlusHydro510->GetY()[i] *= FitScale*0.1;

  auto fProton1020 = new TFile(HYDRO_DATA_PATH + "/10-20/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro1020 = (TGraph*)fProton1020->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro1020->GetN(); i++) mgProtonPlusHydro1020->GetY()[i] *= FitScale*0.01;

  auto fProton2030 = new TFile(HYDRO_DATA_PATH + "/20-30/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro2030 = (TGraph*)fProton2030->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro2030->GetN(); i++) mgProtonPlusHydro2030->GetY()[i] *= 0.5*0.001;

  auto fProton3040 = new TFile(HYDRO_DATA_PATH + "/30-40/proton/fit_graph_spectra_3.root", "READ");  
  TGraph* mgProtonPlusHydro3040 = (TGraph*)fProton3040->Get("Graph");
  for (int i=0; i<mgProtonPlusHydro3040->GetN(); i++) mgProtonPlusHydro3040->GetY()[i] *= FitScale*0.0001;   

  /////////////////////////////////////////////////////////////////////////////////////////////////
  // HYDRO data
  /////////////////////////////////////////////////////////////////////////////////////////////////


  TString plot; 
  TAxis *axis;

  for(int cent=0; cent<3; cent++) {

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

	DoLatex(0.7, 0.75, "#scale[2.0]{#pi^{+}}");  

        mgPionPlusHydro05->SetLineWidth(3);
        mgPionPlusHydro05->SetMarkerStyle(25);
        mgPionPlusHydro05->SetLineColor(kBlack);
        mgPionPlusHydro05->SetLineStyle(1);
        mgPionPlusHydro05->Draw("l");

        mgPionPlusHydro510->SetLineWidth(3);
        mgPionPlusHydro510->SetMarkerStyle(25);
        mgPionPlusHydro510->SetLineColor(kRed);
        mgPionPlusHydro510->SetLineStyle(1);
        mgPionPlusHydro510->Draw("l");

        mgPionPlusHydro1020->SetLineWidth(3);
        mgPionPlusHydro1020->SetMarkerStyle(25);
        mgPionPlusHydro1020->SetLineColor(kBlue);
        mgPionPlusHydro1020->SetLineStyle(1);
        mgPionPlusHydro1020->Draw("l");

        mgPionPlusHydro2030->SetLineWidth(3);
        mgPionPlusHydro2030->SetMarkerStyle(25);
        mgPionPlusHydro2030->SetLineColor(kGreen+3);
        mgPionPlusHydro2030->SetLineStyle(1);
        mgPionPlusHydro2030->Draw("l");

        mgPionPlusHydro3040->SetLineWidth(3);
        mgPionPlusHydro3040->SetMarkerStyle(25);
        mgPionPlusHydro3040->SetLineColor(kMagenta);
        mgPionPlusHydro3040->SetLineStyle(1);
        mgPionPlusHydro3040->Draw("l");

 
        DoLegend3(mgPionPlusHydro05, mgPionPlusHydro510, mgPionPlusHydro1020, mgPionPlusHydro2030, mgPionPlusHydro3040);

      }

      if (cent == 1) { 
  
	DoLatex(0.7,0.75, "#scale[2.0]{K^{+}}");
        //DoLatex(0.23, 0.80, "#scale[1.3]{Pb-Pb, #sqrt{s_{NN}} = 5.02 TeV}");  
        DoLegend2();

        mgKaonPlusHydro05->SetLineWidth(3);
        mgKaonPlusHydro05->SetMarkerStyle(25);
        mgKaonPlusHydro05->SetLineColor(kBlack);
        mgKaonPlusHydro05->SetLineStyle(1);
        mgKaonPlusHydro05->Draw("l");

        mgKaonPlusHydro510->SetLineWidth(3);
        mgKaonPlusHydro510->SetMarkerStyle(25);
        mgKaonPlusHydro510->SetMarkerColor(2);
        mgKaonPlusHydro510->SetLineColor(kRed);
        mgKaonPlusHydro510->SetLineStyle(1);
        mgKaonPlusHydro510->Draw("l");

        mgKaonPlusHydro1020->SetLineWidth(3);
        mgKaonPlusHydro1020->SetMarkerStyle(25);
        mgKaonPlusHydro1020->SetMarkerColor(2);
        mgKaonPlusHydro1020->SetLineColor(kBlue);
        mgKaonPlusHydro1020->SetLineStyle(1);
        mgKaonPlusHydro1020->Draw("l");

        mgKaonPlusHydro2030->SetLineWidth(3);
        mgKaonPlusHydro2030->SetMarkerStyle(25);
        mgKaonPlusHydro2030->SetMarkerColor(2);
        mgKaonPlusHydro2030->SetLineColor(kGreen +3);
        mgKaonPlusHydro2030->SetLineStyle(1);
        mgKaonPlusHydro2030->Draw("l");

        mgKaonPlusHydro3040->SetLineWidth(3);
        mgKaonPlusHydro3040->SetMarkerStyle(25);
        mgKaonPlusHydro3040->SetMarkerColor(2);
        mgKaonPlusHydro3040->SetLineColor(kMagenta);
        mgKaonPlusHydro3040->SetLineStyle(1);
        mgKaonPlusHydro3040->Draw("l");


      }	

      if (cent == 2) { 
  
	DoLatex(0.7,0.75, "#scale[2.0]{p}");  
        DoLatex(0.23, 0.85, "#scale[1.2]{Pb-Pb}");  
        //DoLatex(0.23, 0.85, "#scale[1.2]{Pb-Pb, #sqrt{s_{NN}} = 5.02 TeV}");  
	//DoLatex(0.13, 0.85, "#scale[1.2]{Pb-Pb 5.02 TeV FluiduM+FastReso}");  

        mgProtonPlusHydro05->SetLineWidth(3);
        mgProtonPlusHydro05->SetMarkerStyle(25);
        mgProtonPlusHydro05->SetLineColor(kBlack);
        mgProtonPlusHydro05->SetLineStyle(1);
        mgProtonPlusHydro05->Draw("l");

        mgProtonPlusHydro510->SetLineWidth(3);
        mgProtonPlusHydro510->SetMarkerStyle(25);
        mgProtonPlusHydro510->SetLineColor(kRed);
        mgProtonPlusHydro510->SetLineStyle(1);
        mgProtonPlusHydro510->Draw("l");

        mgProtonPlusHydro1020->SetLineWidth(3);
        mgProtonPlusHydro1020->SetMarkerStyle(25);
        mgProtonPlusHydro1020->SetLineColor(kBlue);
        mgProtonPlusHydro1020->SetLineStyle(1);
        mgProtonPlusHydro1020->Draw("l");

        mgProtonPlusHydro2030->SetLineWidth(3);
        mgProtonPlusHydro2030->SetMarkerStyle(25);
        mgProtonPlusHydro2030->SetMarkerColor(2);
        mgProtonPlusHydro2030->SetLineColor(kGreen+3);
        mgProtonPlusHydro2030->SetLineStyle(1);
        mgProtonPlusHydro2030->Draw("l");

        mgProtonPlusHydro3040->SetLineWidth(3);
        mgProtonPlusHydro3040->SetMarkerStyle(25);
        mgProtonPlusHydro3040->SetLineColor(kMagenta);
        mgProtonPlusHydro3040->SetLineStyle(1);
        mgProtonPlusHydro3040->Draw("l");


      }

      cc1->cd();

   }

   cc1->SaveAs("Figure_3x1.pdf");
   ////////////////////////////////////////////////

   
}
