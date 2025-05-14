#!/usr/bin/python3
# Copyright (c) 2023 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import Tac

Tac.dlopen( "libPlay.so" )

# Setup a byte array for testing
play = Tac.newInstance( 'PlayNs::Play' )
playSm = Tac.newInstance( 'PlayNs::PlaySm', play )

print("adding m0")
play.newMember( "m0" )
print("removing m0" )
del play.member[ "m0" ]

print( "adding m1" )
play.newMember( "m1" )
