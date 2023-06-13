#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - gives information about python
 * @p: PyObject to print info about
 * print_python_list.info.c
 */

void print_python_list_info(PyObject *p)
{

	int elem;

	print("[*] Size of the python List = %lu\n", Py_SIZE(p));
	print("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		print("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
