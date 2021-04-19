#!/bin/bash
# your code goes here
awk 'BEGIN{FS=","}
{if($4<60){print $1,$2}}'|uniq|sort
