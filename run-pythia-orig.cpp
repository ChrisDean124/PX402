#include "Pythia8/Pythia.h"
#include <iostream>
#include <array>
#include <fstream>
#include <cmath>

int nBins = 50;
double pTmin = 15.0;
double pTmax = 50.0;
double binWidth = (pTmax - pTmin) / nBins;

std::array<unsigned long long, nBins> nPlus{};
std::array<unsigned long long, nBins> nMinus{};

using namespace Pythia8;

int main() {

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
    if (!pythia.next()) {
        std::cerr << "Event generation failed!" << std::endl;
        return 1;
    }

    // 7. Read out the generated data (Example: loop through final state particles)
    int final_state_count = 0;
    
    for (int i = 0; i < pythia.event.size(); ++i) {
        // Only look at stable, final-state particles
        if (pythia.event[i].isFinal()) {
            final_state_count++;
        }
    }

    // Print out the statistics summary
    std::cout << "\n--- Successfully generated 1 HardQCD Event ---" << std::endl;
    std::cout << "Total stable final-state particles: " << final_state_count << std::endl;

    // 8. Print optional process statistics at the end of execution
    pythia.stat();



    return 0;
}
