#include <stdio.h>
#include <stdlib.h>

typedef int **board;

board create_board(int x, int y) {
  int** board;
  board = (int**)malloc(x*sizeof(int*));

  for (int i = 0; i < x; ++i)
    board[i] = (int*)malloc(y*sizeof(int));
  
  return board;
}

void fill_board(int x, int y, board b, int fill) {
  for (int i = 0; i < x; ++i)
    for (int j = 0; j < y; ++j)
      b[i][j] = fill;
}

void print_board(int x, int y, board b) {
  for(int i = 0 ; i < x; ++i) {
    for (int j = 0; j < y; ++j)
      printf("%d", b[i][j]);
    printf("\n");
  }
}
