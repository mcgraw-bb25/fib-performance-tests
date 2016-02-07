set -e

output_file=test_output

case $1 in
  "core")
    if [ -e $output_file ]
    then
        rm $output_file
    fi

    clang-3.5 -o fib_c_out.out fib.c
    ./fib_c_out.out >> $output_file

    javac fib.java
    java fib >> $output_file

    julia fib.jl >> $output_file

    go run fib.go >> $output_file

    node fib.js >> $output_file

    python3 fib.py >> $output_file

    ruby fib.rb >> $output_file;;

  "extend")
    python3 fib_cython3.py >> $output_file
    python3 fib_pyrust.py >> $output_file
    python3 fib_inverted.py >> $output_file
    ruby fib_rbrust.rb >> $output_file;;
esac
