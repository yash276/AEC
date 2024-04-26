```
gcc -dM -E - < /dev/null | grep "__STDC_"
gcc -Wall -save-temps hello.c -o hello   
```