#!/bin/sh
echo "** Building Flatpak **"
flatpak-builder --force-clean build-dir ./flatpak/io.github.riftr.flatpak-python-template.yml

echo "** Running Flatpak **"
flatpak-builder --run build-dir ./flatpak/io.github.riftr.flatpak-python-template.yml run.sh