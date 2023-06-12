#include "Python.c"
/**
 * print_python_list_info - gives information about python
 * @p: PyObject to print info about
 * 100-print_python_list.info.c
 */

void print_python_list_info(PyObject *p):
{
	Py_ssize_t x, py_list_size;
	PyObject *item;
	const char *item;
	PyListObject *list_object_cast;

	lis_object_cast = (PyListObject *)p
	py_list_size = PyList_Size(p);

	print("[*] Size of th Python List = %d\n", (int) py_list_size);
	print("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (x = 0; x < py_list_size; x++)
	{
		item = PyList_GetItem(p, x);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) x, item_type);
	}



}

