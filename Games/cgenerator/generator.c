#include <stdio.h>

int main(int argc, char *argv[])
{
  if (argc > 1) {
    printf("%s\n", argv[1]);
  } else {
    printf("%s\n", "No number of games was specified");
  }
  return 0;
}
