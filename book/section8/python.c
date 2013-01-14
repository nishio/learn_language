#include "Python.h"
#include <stdio.h>

int main(){
  Py_Initialize();
  unsigned long buf[10];

  PyObject* i = Py_BuildValue("i", 0x1234567);
  printf("i: %p\n", i);
  memcpy(buf, i, sizeof(long) * 3);
  printf("  %016lx\n", buf[0]); /* refcount */
  printf("  %016lx\n", buf[1]); /* type */
  printf("  %016lx\n", buf[2]); /* value */

  PyObject* cls = PyObject_GetAttrString(i, "__class__");
  printf("i.__class__: %p\n", cls); /* type */

  PyObject* x = Py_BuildValue("f", (float)0x123456 / (float)0x100000);
  printf("x: %p\n", x);
  memcpy(buf, x, sizeof(long) * 3);
  printf("  %016lx\n", buf[0]); /* refcount */
  printf("  %016lx\n", buf[1]); /* type */
  printf("  %016lx\n", buf[2]); /* value */

  cls = PyObject_GetAttrString(x, "__class__");
  printf("x.__class__: %p\n", cls); /* type */

  Py_Finalize();
  return 0;
}
