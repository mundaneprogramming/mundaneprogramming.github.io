




generate random thing:

~~~sh
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1
~~~

~~~sh
mb="adsjflkjASDJAKVCfdas31"
echo $mb > ~/Dropbox/__hello.txt
grep "CHICKEN" ~/Dropbox/__hello.txt 
~~~
