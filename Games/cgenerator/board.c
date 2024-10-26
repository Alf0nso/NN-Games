#include <stdio.h>
#include <stdlib.h>

typedef int** board;

board create_board(int x, int y) {
  int** board;
  board = (int**)malloc(x*sizeof(int*));

  for (int i = 0; i < x; ++i)
    board[i] = (int*)malloc(y*sizeof(int));
  
  return board;
}
