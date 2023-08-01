#!/usr/bin/python3
# Copyright (c) 2023 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import Tac

# Setup a byte array for testing
ary = bytearray( 256 )
for i in range( 256 ):
   ary[i] = 255 - i

Tac.dlopen( "libPlay.so" )
Play = Tac.Type( "Play" )
play = Play()
play.pa1 = 10
assert play.pa1 == 10

