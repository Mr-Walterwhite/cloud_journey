#!/bin/bash
echo "=============================="
echo "   SYSTEM REPORT - $(date)"
echo "=============================="
echo ""
echo "-- WHO AM I --"
whoami
echo ""
echo "-- DISK USAGE --"
df -h
echo ""
echo "-- MEMORY --"
free -h
echo ""
echo "-- MY FILES --"
ls -la ~/cloud-journey/week1
echo ""
echo "=============================="
echo "Report complete."
echo "=============================="
