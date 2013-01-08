#include "Python.h"
#include <stdio.h>

int main(){
  Py_Initialize();
  unsigned long buf[10];

  PyObject* i = Py_BuildValue("i", 0xDEADBEEF);
  printf("i: %p\n", i);
  memcpy(buf, i, sizeof(i) * 3);
  printf("%p: %016lx\n", i, buf[0]); /* refcount */
  printf("%p: %016lx\n", i + 1, buf[1]); /* type */
  printf("%p: %016lx\n", i + 2, buf[2]); /* value */

  PyObject* cls = PyObject_GetAttrString(i, "__class__");
  printf("cls: %p\n", cls); /* type */

  PyObject* x = Py_BuildValue("f", (float)0x1CAFE / (float)0x10000);
  printf("x: %p\n", x);
  memcpy(buf, x, sizeof(x) * 3);
  printf("%p: %016lx\n", x, buf[0]); /* refcount */
  printf("%p: %016lx\n", x + 1, buf[1]); /* type */
  printf("%p: %016lx\n", x + 2, buf[2]); /* value */

  Py_Finalize();
  return 0;
}
