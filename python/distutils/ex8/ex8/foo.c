/* 
I am a foo C progtam 
*/

#include<Python.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"bar.c"



static PyObject*
foo_system(PyObject *self,PyObject *args) {
	const char* command;
	int sts;
	
	if(!PyArg_ParseTuple(args,"s",&command))
		return NULL;
	sts = system(command);
	return Py_BuildValue("i",sts);

}

static PyObject*
foo_hello(PyObject *self,PyObject *args){
	printf(hello_str);
	return Py_BuildValue("i",1);
}

static PyMethodDef FooMethods[] = {
	{"system",foo_system, METH_VARARGS, "Execute a shell command"},
	{"hello",foo_hello,METH_VARARGS,"Print Hello World"},
	{NULL,NULL,0,NULL}
};


PyMODINIT_FUNC
initfoo(void)
{
	(void) Py_InitModule("foo",FooMethods);
}
