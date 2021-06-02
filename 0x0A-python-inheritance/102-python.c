#include <stdio.h>
#include <Python.h>

unsigned long powtwo(unsigned long expo);

void print_python_int(PyObject *p)
{
	PyLongObject *lng;
//	PyTypeObject *typ;
	PyVarObject *var;
	unsigned long clong;
	long i, size;
	int sign;

	if (!PyLong_Check(p))
	{
		printf("Invalid Int Object\n");
		return;
	}
	lng = (PyLongObject *) p;
//	typ = (PyTypeObject *) p;
	var = (PyVarObject *) p;
//	printf("%u\n", lng->ob_digit[0]);
//	printf("%lu\n", var->ob_size);
	clong = 0;
	size = var->ob_size;
	sign = 1;
	if (size < 0)
	{
		size *= -1;
		sign = -1;
	}
	for (i = size - 1; i >= 0; i--)
	{
		clong = (clong >> (8*sizeof(long)-PyLong_SHIFT)) | (clong << PyLong_SHIFT);
		clong += (lng->ob_digit[i]);
		if (clong < lng->ob_digit[i])
		{
			printf("C unsigned long int overflow");
			return;
		}
	}
	if (sign == -1)
		printf("-");
	printf("%lu\n", clong);
}


unsigned long powtwo(unsigned long expo)
{
	unsigned long i;
	unsigned long sum;

	i = 0;
	sum = 2;
	while (i < (expo - 1))
	{
		sum *= 2;
		i++;
	}
	return (sum);
}
