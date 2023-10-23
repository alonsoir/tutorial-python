#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool es_primo_sieve_of_atkin(long long numero) {
  if (numero <= 1) {
    return false;
  }

  // Crea una lista de números del 2 al n.

  vector<bool> primos(numero + 1, true);

  // Elimina los múltiplos de 2.

  for (long long i = 2; i * i <= numero; i++) {
    if (primos[i]) {
      for (long long j = i * i; j <= numero; j += i) {
        primos[j] = false;
      }
    }
  }

  // Elimina los números de la forma 4n+1 para n > 1.

  for (long long i = 3; i <= numero; i += 2) {
    if (primos[i]) {
      for (long long j = i * i; j <= numero; j += 2 * i) {
        primos[j] = false;
      }
    }
  }

  // Elimina los números de la forma 8n+3 y 8n+5 para n > 1.

  for (long long i = 5; i <= numero; i += 4) {
    if (primos[i]) {
      for (long long j = i * i; j <= numero; j += 8 * i) {
        if (j % 4 == 3) {
          primos[j] = false;
        }
        if (j % 4 == 5) {
          primos[j] = false;
        }
      }
    }
  }

  // Devuelve la lista de números que no están marcados como no primo.

  return primos[numero];
}

vector<long long> calcular_primos_sieve_of_atkin(long long n) {
  vector<long long> primos;
  for (long long i = 2; i <= n; i++) {
    if (es_primo_sieve_of_atkin(i)) {
      primos.push_back(i);
    }
  }
  return primos;
}

int main() {
  auto start_time = std::chrono::steady_clock::now();
  auto how_many_primes = 10000000000;
  std::cout << "Working. Calculating " << how_many_primes << " primes using Sieve of Atkin." <<std::endl;
  auto primos = calcular_primos_sieve_of_atkin(how_many_primes);
  auto end_time = std::chrono::steady_clock::now();
  std::cout << "Tiempo de ejecución en calcular los primos: "  
            << std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time).count()
            << " segundos" << std::endl;
  // Volcar el resultado en un archivo de texto.
  start_time = std::chrono::steady_clock::now();
  ofstream archivo("primos.txt");
  for (long long primo : primos) {
    archivo << primo << endl;
  }
  archivo.close();
  end_time = std::chrono::steady_clock::now();
  std::cout << "Tiempo de ejecución en guardar en el fichero primos.txt: "  
            << std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time).count()
            << " segundos" << std::endl;
  

  std::cout << "Hecho. Se ha creado un fichero primos.txt" << std::endl;
  return 0;
}
