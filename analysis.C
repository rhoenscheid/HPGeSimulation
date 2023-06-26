//ROOT Analysis Script
//Executes the analysis() function

std::unique_ptr<TFile> myFile( TFile::Open("sim_out.root") );
std::unique_ptr<TTree> myTree( myFile->Get<TTree>("g4sntuple") );

void analysis(){


	auto fileName = "sim_out.root";
	//auto treeName = "g4sntuple";
	//fill_tree(treeName, fileName);
       
	ROOT::RDataFrame rdf(myTree, fileName);

	ROOT::RDF::RDisplay::Print(rdf);

        for (int i=0; i<5; i++){

		auto select1 = [](int event) {return event == 1; };
		auto entries1 = rdf.Filter(select1).Count();
		std::cout << *entries1 << " entries passed the filter." << std::endl;
        }




	//auto h = rdf.Histo1D("Edep");
	//h->Draw();

	//std::unique_ptr<TH1> hist(myFile->Get<TH1>("Edep"));
	//hist->Draw();

}

