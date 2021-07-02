#!/bin/bash
DATE=$(date +"%Y-%b-%d-%H-%M-%S")
mkdir -p ~/old
tar -hzcf ~/old/nbgrader-$DATE.tgz ~/nbgrader