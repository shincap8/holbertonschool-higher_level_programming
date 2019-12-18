#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints info about python list
* @p: list pointer
*
* Return: void
**/
void print_python_list_info(PyObject *p)
{
	int i, length;
	Pyobject *element;

	length = Pylist_Size(p);

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < length; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
