#!/bin/bash

#!/bin/bash

if [ "$1" == "HUMAN" ]; then
    # Run in human mode with maze size (default 15 if not provided)
    SIZE=${2:-15}
    python solve_maze.py --mode HUMAN --size $SIZE
else
    # Run in AI mode
    if [ "$#" -eq 0 ]; then
        python solve_maze.py -config_file config.yaml
    else
        python solve_maze.py -config_file config.yaml ALGORITHM.NAME $1 MAZE.SIZE $2
    fi
fi

