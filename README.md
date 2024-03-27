# flatpak-python-template
A template for packaging Python-based apps with Flatpak.


## This template is a work in progress 


### Instructions

You need to adjust ***my_sample_app*** in the various files to match the directory which your Python
application lives. Then you need to update ***run.sh*** to match the entry point for your app.

Included is an example of copying a resource directory into the Flatpak if needed.

To generate your Python dependency list of sources for the YML file, use flatpak-getreq.sh. This will 
generate a python3-requirements.yaml file which you can copy the sources: from into the YML file. Don't 
forget to rename this file to match your application.

To build it use flatpak-build.sh
