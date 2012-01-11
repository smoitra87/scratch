/* Reads in a file and builds a Python DS from it */

#include<Python.h>

static PyObject*
parser_parseList(PyObject* self, PyObject *args);

static PyObject*
parser_parseDict(PyObject* self, PyObject *args);

static PyMethodDef ParserMethods[] = {
	{"parse_list",parser_parseList,METH_VARARGS,
	"Parse a file and return a Python List"},
	{"parse_dict",parser_parseDict,METH_VARARGS,
	"Parse and file and return a Python Dictionary"},
	{NULL,NULL,0,NULL}	
};

PyMODINIT_FUNC
initcparser(void) {

	(void) Py_InitModule("cparser",ParserMethods);
}

static PyObject*
parser_parseList(PyObject* self, PyObject *args){

	int vals[] = {1,2,3};
	int i;
	PyObject *pystr,*pyint,*pylist;
	
	pylist = PyList_New(0);

	int len_array = (int)sizeof(vals)/(sizeof(vals[0]));
	printf("Length of list array is %d\n",len_array);

	for(i  = 0 ; i < len_array ; i++) {
		pystr = PyString_FromFormat("%d",vals[i]);
		pyint = PyFloat_FromString(pystr,NULL);
		PyList_Append(pylist,pyint);
	}
	return pylist;
}

static PyObject*
parser_parseDict(PyObject* self, PyObject *args){

	int vals[] = {1,2,3};
	char keys[][10] = {"a","ab","abc"};
	int i;
	PyObject *pystr,*pyint,*pydict,*val;
	const char* key;	
	
	pydict = PyDict_New();

	int len_array = (int)sizeof(vals)/(sizeof(vals[0]));
	printf("Length of array is %d\n",len_array);

	for(i  = 0 ; i < len_array ; i++) {
		//Build The Val
		pystr = PyString_FromFormat("%d",vals[i]);
		pyint = PyFloat_FromString(pystr,NULL);
		val = pyint;

		// Build the Key
		key = keys[i];
		//pystr = PyString_FromFormat("%s",keys[i]);
		// Add element to dict
		PyDict_SetItemString(pydict,key,val);
	}
	return pydict;
}



