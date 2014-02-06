#!/usr/bin/env bash

make html latexpdf epub

# Deploy to Ira's account on EOS

# exec so we exit with the error code of rsync.
exec rsync \
	--verbose \
	--archive \
	--chmod=go=rX \
	--compress \
	_build/html/* \
	_build/latex/MasteringEOS.pdf \
	_build/epub/MasteringEOS.epub \
	woodriir@eos10.cis.gvsu.edu:public_html/mastering-eos

