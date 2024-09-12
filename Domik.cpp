#include <iostream>
#include <windows.h>
using namespace std;

int col[7] = {3, 2, 11, 1, 9, 7};
int color(int c) {
  // Color of the console
  HANDLE console_color;
  console_color = GetStdHandle(STD_OUTPUT_HANDLE);
  SetConsoleTextAttribute(console_color, col[c]);
  return 0;
}
int main() {
  std::cout << "Enter size:\n";
  int a, b;
  std::cin >> a >> b;
  while (a <= 1 || b <= 1) {
    std::cout << "cannot be < 2\n";
    std::cin >> a >> b;
  }
  color(0);
  if (a % 2) {
    for (int j = 0; j < a / 2 + 2; j++) {
      std::cout << ' ';
    }
    std::cout << "*\n";
  }
  // крыша
  for (int i = 0; i < a - (a % 2); i += 2) {
    std::cout << "  ";
    for (int j = 0; j < (a - i - 2) / 2; j++) {
      std::cout << ' ';
    }
    std::cout << '/';
    for (int j = 0; j < i + (a % 2); j++) {
      std::cout << ' ';
    }
    std::cout << "\\\n";
  }
  color(2);
  // Потолок /----
  std::cout << " /";
  for (int i = 0; i < a; i++) {
    std::cout << '-';
  }
  std::cout << "\\\n";
  // Стена / |  |
  std::cout << "/ |";
  for (int i = 0; i < a - 2; i++) {
    std::cout << ' ';
  }
  std::cout << "| \\\n";
  color(4);
  // Другие стены
  for (int j = 0; j < b - 2; j++) {
    std::cout << "  |";
    for (int i = 0; i < a - 2; i++) {
      std::cout << ' ';
    }
    std::cout << "|\n";
  }
  color(1);
  // пол
  std::cout << "  |";
  for (int i = 0; i < a - 2; i++) {
    std::cout << '_';
  }
  std::cout << "|\n";
  color(5);
  return 0;
}
