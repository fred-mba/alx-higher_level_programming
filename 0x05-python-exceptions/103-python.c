#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);

		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
		else if (PyFloat_Check(list->ob_item[i]))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_GET_SIZE(p);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	size = (size > 10) ? 10 : size;

	printf("  first %ld bytes: ", size);
	for (Py_ssize_t i = 0; i < size; i++)
		printf("%02hhx%c", bytes->ob_sval[i], (i == size - 1) ? '\n' : ' ');
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p:PyObject float object.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %s\n", PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
		Py_DTSF_ADD_DOT_0, NULL));
}

