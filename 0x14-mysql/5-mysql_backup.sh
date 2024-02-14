#!/bin/bash

# Generate MySQL dump
mysqldump -uroot -pPASSWORD --all-databases > backup.sql

# Create tar.gz archive
timestamp=$(date +%d-%m-%Y)
tar -czf $timestamp.tar.gz backup.sql

# Remove dump file
rm backup.sql
