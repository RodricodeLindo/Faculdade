#include<stdio.h>

float adicao(float x, float y){
  return x+y;
}

float subtracao(float x, float y){
  return x-y;
}

float divisao(float x, float y){
  return x/y;
}

float multriplicador(float x, float y){
  return x*y;
}

float calculo(float x, float y, char opera){
   switch(opera){
    case '+':
      return adicao(x, y);
      break;
    case '-':
      return subtracao(x, y);
      break;
    case '*':
      return multriplicador(x, y);
      break;
    case '/':
      return divisao(x, y);
      break;
    default:
      printf("\nopção inválida!\n");
  }
}

void menu(){
  float x, y, resul;
  char op;
  printf("Digite um calculo simples Ex: 1 + 1\n->");
  scanf("%f %c %f", &x, &op, &y);
  getchar();
  resul = calculo(x, y, op);
  printf("\n\t%.2f %c %.2f = %.2f\n\n", x, op, y, resul);
}

int main(){
  menu();

  printf("...");
  getchar();
  return 0;
}

