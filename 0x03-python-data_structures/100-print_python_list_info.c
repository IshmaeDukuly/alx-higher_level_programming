#include <stdio.h>
#include <stdlib.h>
#include <python.h>
/**
 * print_python_list_info - thos prints
 * some neccessary info about python
 * @n: The python list
 */

void print_python_list_info(pyObject *p)
{

	pyObject *item;
	pyObject *list = (pyList(Object *)p;
	int x, size, alloc;

	size = py_size(p);
	alloc = lis->allocated;
	print("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for x = 0; x < size; x++)
	{
	item = pyList_getItem(p, i);
	printf("Element %d: %s\n", x, py_TYPE(item)->tp_name);
	}


}


