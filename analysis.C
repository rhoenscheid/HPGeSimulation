//ROOT Analysis Script
//Executes the analysis() function

std::unique_ptr<TFile> myFile( TFile::Open("sim_out.root") );
std::unique_ptr<TTree> myTree( myFile->Get<TTree>("g4sntuple") );

void analysis(){

	ROOT::RDataFrame rdf("myTree", "sim_out.root");
	auto h = rdf.Histo1D("Edep");
	h->Draw();

	//std::unique_ptr<TH1> hist(myFile->Get<TH1>("Edep"));
	//hist->Draw();

}

