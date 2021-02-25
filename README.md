# SimpleNetworkTopology

[![Documentation Status](https://readthedocs.org/projects/simplenetworktopologies/badge/?version=latest)](https://simplenetworktopologies.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/KrysEWilliams/SimpleNetworkTopologies.svg?branch=master)](https://travis-ci.com/KrysEWilliams/SimpleNetworkTopologies)

This code is used to visualize simple computer network topologies.

## Usage

This executable is for students or users new to Networking Topologies. This program will allow for users to see 6 examples of Networking Topologies that can be used to set up a network professionally. Using common layouts like Bus, Star, Ring, Mesh, FullyConnected, and Generic Topologies, the program is a great guide for learning what topology will work best in different situations(i.e Corporate Offices or Computer Labs).

## Installations

To use the program, Download the zip file off of the Github repository. Then proceed to allow the program to run using the Windows App Wizard. This will allow users to interact with the program.

## Screenshots

## Development / Contributing

Make sure you are in the top-level directory ("SimpleNetworkTopology"). 

To run the main program, type (`$` refers to command line prompt)

`$ python simplenetworktopology`

To run all unit tests, type

`$ python -m unittest -v`

(the `-v` option stands for "verbose" and lists each test that is run)

We will eventually probably use sphynx for documentation. 

### To run local server for online interface

Start the built-in Python HTTP server by

`$ python -m http.server`

The default port is 8000. To specify another port, e.g. 8080:

`$ python -m http.server 8080`

Then load http://localhost:<port>/index.html in the browser address bar. This will display the website as would be rendered online.
