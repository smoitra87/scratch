#!/bin/sh
# Try to submit a ssh command otherwise forward via leo

cmd_check_leo="ssh leo hostname 2>/dev/null 1>/dev/null"
cmd_check_pdl="ssh pdl hostname 2>/dev/null 1>/dev/null"
cmd_exec_pdl="ssh pdl 'touch /tmp/a.txt' 2>/dev/null 1>/dev/null"

# Check if pdl is accesible
echo $cmd_check_pdl && $cmd_check_pdl
if [ $? -eq 0 ] 
then 
	$cmd_exec_pdl && echo "Successful ssh execution"
else 
	echo "Resorting to ssh forwarding"
	echo "ssh leo" $cmd_exec_pdl
	ssh leo $cmd_exec_pdl && echo "successful ssh execution"
fi

