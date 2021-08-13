#!/bin/bash
MYIP=`ping -c1 "${site}" | sed -nE 's/^PING[^(]+\(([^)]+)\).*/\1/p'`
