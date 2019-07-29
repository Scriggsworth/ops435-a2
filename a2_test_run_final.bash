#!/bin/bash

# data file: a1_final_data
test_data=usage_data_file.txt
echo "Test data file: ${test_data}"

cat ${test_data}

./a2_ikossinov.py -h

./a2_ikossinov.py -l user ${test_data}
./a2_ikossinov.py -l host ${test_data}
./a2_ikossinov.py -u rchan -t daily ${test_data}
./a2_ikossinov.py -u rchan -t weekly ${test_data}
./a2_ikossinov.py -u rchan -t monthly ${test_data}
./a2_ikossinov.py -r 10.40.105.99 -t daily ${test_data}
./a2_ikossinov.py -r 10.40.105.99 -t weekly ${test_data}
./a2_ikossinov.py -r 10.40.105.99 -t monthly ${test_data}

./a2_ikossinov.py -l user ${test_data} -v
./a2_ikossinov.py -l host ${test_data} -v
./a2_ikossinov.py -u asmith -t daily ${test_data} -v
./a2_ikossinov.py -u asmith -t weekly ${test_data} -v
./a2_ikossinov.py -u asmith -t monthly ${test_data} -v
./a2_ikossinov.py -r 10.40.105.130 -t daily ${test_data} -v
./a2_ikossinov.py -r 10.40.105.130 -t weekly ${test_data} -v
./a2_ikossinov.py -r 10.40.105.130 -t monthly ${test_data} -v
