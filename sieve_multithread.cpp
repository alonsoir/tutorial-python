#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <thread>

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

// Esta función calcula los primos en un rango determinado.

void calcular_primos_rango(long long inicio, long long fin, vector<long long> &primos) {
  for (long long i = inicio; i <= fin; i++) {
    if (es_primo_sieve_of_atkin(i)) {
      primos.push_back(i);
    }
  }
}

vector<long long> calcular_primos_sieve_of_atkin_multihilo(long long n, int num_hilos) {
  vector<long long> primos;

  // Crea una lista de rangos de números para cada hilo.

  vector<pair<long long, long long> > rangos(num_hilos);
  for (int i = 0; i < num_hilos; i++) {
    rangos[i] = make_pair(2 + i * (n / num_hilos), 2 + (i + 1) * (n / num_hilos));
  }

  // Crea un grupo de hilos.

  vector<thread> hilos;
  for (int i = 0; i < num_hilos; i++) {
      hilos.push_back(thread([&, i]() {
        calcular_primos_rango(rangos[i].first, rangos[i].second, primos);
      }));
  }

  // Espera a que todos los hilos terminen.

  for (int i = 0; i < num_hilos; i++) {
    hilos[i].join();
  }

  return primos;
}

int main() {
  auto start_time = std::chrono::steady_clock::now();
  long long how_many_primes = 10;
  std::cout << "Working. Calculating " << how_many_primes << " primes using Sieve of Atkin." <<std::endl;

  // Invocar la lógica que lanza los hilos para realizar el cálculo.

  auto primos = calcular_primos_sieve_of_atkin_multihilo(how_many_primes, 8);

  // Medir los tiempos.

  auto end_time = std::chrono::steady_clock::now();
  auto tiempo_calculo = std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time).count();
  std::cout << "Tiempo de ejecución en calcular los primos: " << tiempo_calculo << " segundos" << std::endl;

  // Crear el fichero de texto con los primos calculados.

  std::ofstream archivo("primos.txt");
  for (int i = 0; i < primos.size(); i++) {
    archivo << primos[i] << std::endl;
  }
  archivo.close();

  // Mostrar el tiempo necesario para volcar al fichero de texto los numeros calculados.

  auto end_time_escritura = std::chrono::steady_clock::now();
  auto tiempo_escritura = std::chrono::duration_cast<std::chrono::seconds>(end_time_escritura - end_time).count();
  std::cout << "Tiempo necesario para volcar al fichero de texto los numeros calculados: " << tiempo_escritura << " segundos" << std::endl;

  return 0;
}
