#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Define Methods here

static PyObject * ctensor_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}

static PyObject * say_hello(PyObject *self, PyObject *args)
{
    printf("Hello World!\n");
    return Py_None;
}

// List of Methods

static PyMethodDef CtensorMethods[] = {
    {"system",  ctensor_system, METH_VARARGS, "Execute a shell command."},
    {"hello",  say_hello, METH_VARARGS, "Says hello."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

//  Define module and the Method List

static struct PyModuleDef ctensormodule = {
    PyModuleDef_HEAD_INIT,
    "ctensor",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    CtensorMethods
};

// Initialize the module

PyMODINIT_FUNC PyInit_ctensor(void)
{
    return PyModule_Create(&ctensormodule);
}

// Entry point to the shared object

int main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("ctensor", PyInit_ctensor);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("ctensor");

    PyMem_RawFree(program);
    return 0;
}