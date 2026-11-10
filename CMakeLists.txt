cmake_minimum_required(VERSION 3.10)
project(PythiaEventGenerator CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Define the CVMFS environment base path 
set(CVMFS_PATH "/cvmfs/lhcb.cern.ch/conda/envs/default/2026-09-17_08-55/linux-64")

# Adds ROOT dependency
find_package(ROOT CONFIG REQUIRED COMPONENTS ROOTDataFrame
    HINTS "${CVMFS_PATH}"
)

# Set paths for Pythia8 headers and libraries
include_directories("${CVMFS_PATH}/include")
link_directories("${CVMFS_PATH}/lib")

# Create the executable from your top-level source file
add_executable(run-pythia run-pythia.cpp)

set_target_properties(run-pythia PROPERTIES
    CXX_STANDARD 23
    CXX_STANDARD_REQUIRED ON
)

# Link explicitly against pythia8, dl, and force-link the modern libstdc++ via RPATH
target_link_libraries(run-pythia pythia8 dl ROOT::ROOTDataFrame)

# Force the executable to load the newer Conda standard libraries at runtime
set_target_properties(run-pythia PROPERTIES 
    LINK_FLAGS "-L${CVMFS_PATH}/lib -Wl,-rpath,${CVMFS_PATH}/lib"
)
