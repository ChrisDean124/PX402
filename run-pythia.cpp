#include "Pythia8/Pythia.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <ROOT/RDataFrame.hxx>

using namespace Pythia8;


  int main() {

    int nEvents = 1000;

    std::vector<double> pT(nEvents) ;
    std::vector<double> charge(nEvents) ;


    // 1. Instantiate the Pythia generator object
    Pythia pythia;

    // 2. Configure the collision beam details (Proton-Proton at LHC Run 3 energy)
    pythia.readString("Beams:idA = 2212"); // Proton
    pythia.readString("Beams:idB = 2212"); // Proton
    pythia.readString("Beams:eCM = 13600."); // Center-of-mass energy in GeV

    // 3. Enable Hard QCD processes
    pythia.readString("HardQCD:all = on");

    // 4. Set a minimum pT hat cut to avoid divergences in the perturbative cross-section
    pythia.readString("PhaseSpace:pTHatMin = 20.0");

    // 5. Initialize the generator
    if (!pythia.init()) {
        std::cerr << "Pythia initialization failed!" << std::endl;
        return 1;
    }

    // 6. Generate a single event
    
    for (int j = 0; j < nEvents ; j++) {
	    if (!pythia.next()) {
		std::cerr << "Event generation failed!" << std::endl;
		return 1;
	    }

	    // 7. Read out the generated data (Example: loop through final state particles)
	   double pTmax = 0; 
	   double target_charge = 0; 

	    for (int i = 0; i < pythia.event.size(); ++i) {
		// Only look at stable, final-state particles
		if (pythia.event[i].isFinal() && pythia.event[i].pT() > pTmax) {
			pTmax = pythia.event[i].pT();
			target_charge = pythia.event[i].charge();	
		}
	    }
	    
	    pT[j] = pTmax;
	    charge[j] = target_charge;

    }

    ROOT::RDataFrame rdf(nEvents);
    
    auto events = rdf.Define("pT_GeV", [&pT](ULong64_t i) {return pT[i]; }, {"rdfentry_"} )
	    	     .Define("charge", [&charge](ULong64_t i) {return charge[i]; }, {"rdfentry_"} ) ;

    events.Snapshot("Events", "transient/event_data.root", {"pT_GeV", "charge"});
    

    return 0;
}
