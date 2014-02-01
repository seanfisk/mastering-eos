#!/usr/bin/env bash

# Deploy to Ira's account on EOS

# exec so we exit with the error code of rsync.
exec rsync \
	--verbose \
	--archive \
	--chmod=go=rX \
	--compress \
	_build/html/* \
	woodriir@eos10.cis.gvsu.edu:public_html/mastering-eos
