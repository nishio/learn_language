# Make small disk on ram

init:
	sudo mkfs -q /dev/ram1 1024
	sudo mkdir -p /ramcache
	sudo mount /dev/ram1 /ramcache
	sudo chmod 777 /ramcache/
	df -H

test:
	gcc write.c
	./a.out

finish:
	sudo umount /ramcache