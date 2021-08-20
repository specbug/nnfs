a=0

while [ $a -lt 100 ]
do
	echo "Iteration" $a
	python3 -u sim.py loop 1000 &
	python3 -u sim.py vector 1000
	a=`expr $a + 1`
done
