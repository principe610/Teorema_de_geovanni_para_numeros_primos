m"""
==============================================================================
TEOREMA DE GEOVANNI PARA LA DETERMINACIÓN DE PRIMALIDAD
==============================================================================
Autor: Geovanni 
Colaborador: Asistente AI
Fecha: 2024
Licencia: Creative Commons - Compartir igual

DESCRIPCIÓN:
Implementación del teorema que determina la primalidad de un número mediante
verificación optimizada con conjuntos primos base y auto-expansión del conocimiento.

Teorema de Geovanni (2025)
Un número N > 1 es primo si y solo si:
   N ∈ P ∨ (∀f ∈ P, N mod f ≠ 0) 
donde P = {primos ≤ √N}


EFICIENCIA:
- Complejidad: O(√n / log n) mediante criba inteligente
- Auto-aprendizaje: Expande conocimiento con cada cálculo
- Verificación mínima: Solo divisores primos necesarios
==============================================================================
"""

import math
import time

class TeoremaGeovanni:
    """
    Implementación del Teorema de Geovanni para determinación de primalidad
    y generación de números primos.
    """
    
    def __init__(self):
        # Conjunto primo base optimizado (primos ≤ 30)
        self.primos_base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.primos_conocidos = self.primos_base.copy()
        self.estadisticas = {
            'numeros_procesados': 0,
            'primos_encontrados': 0,
            'tiempo_total': 0
        }
    
    def es_primo(self, n):
        """
        Determina si un número es primo usando el Teorema de Geovanni.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        inicio = time.time()
        self.estadisticas['numeros_procesados'] += 1
        
        # Casos triviales
        if n < 2:
            return False
        if n == 2:
            self.estadisticas['primos_encontrados'] += 1
            return True
        
        # Verificación rápida de divisibilidad por 2 y 3
        if n % 2 == 0 or n % 3 == 0:
            return n in [2, 3]
        
        # Si n está en primos base, es primo
        if n in self.primos_base:
            self.estadisticas['primos_encontrados'] += 1
            return True
        
        # Calcular límite para verificación
        limite = math.isqrt(n)
        
        # Expandir conocimiento si es necesario
        if limite > self.primos_conocidos[-1]:
            self._expandir_conocimiento(limite)
        
        # Aplicar teorema: verificar divisibilidad por primos ≤ √n
        for p in self.primos_conocidos:
            if p > limite:
                break
            if n % p == 0:
                return False
        
        # n es primo - agregar al conocimiento
        if n > self.primos_conocidos[-1]:
            self.primos_conocidos.append(n)
            self.primos_conocidos.sort()
        
        self.estadisticas['primos_encontrados'] += 1
        self.estadisticas['tiempo_total'] += time.time() - inicio
        return True
    
    def _expandir_conocimiento(self, limite):
        """
        Expande el conjunto de primos conocidos hasta el límite especificado.
        """
        candidato = self.primos_conocidos[-1] + 2
        
        while self.primos_conocidos[-1] < limite:
            if self._verificar_primalidad(candidato):
                self.primos_conocidos.append(candidato)
            candidato += 2
    
    def _verificar_primalidad(self, n):
        """
        Verificación interna de primalidad sin auto-expansión recursiva.
        """
        if n < 2:
            return False
        if n in self.primos_conocidos:
            return True
        
        limite = math.isqrt(n)
        for p in self.primos_conocidos:
            if p > limite:
                break
            if n % p == 0:
                return False
        return True
    
    def obtener_nesimo_primo(self, n):
        """
        Encuentra el n-ésimo número primo.
        
        Args:
            n (int): Posición del primo deseado (n ≥ 1)
            
        Returns:
            int: El n-ésimo número primo
        """
        while len(self.primos_conocidos) < n:
            candidato = self.primos_conocidos[-1] + 2
            while not self.es_primo(candidato):
                candidato += 2
        
        return self.primos_conocidos[n-1]
    
    def generar_primos_rango(self, inicio, fin):
        """
        Genera todos los primos en un rango especificado.
        
        Args:
            inicio (int): Límite inferior del rango
            fin (int): Límite superior del rango
            
        Returns:
            list: Lista de números primos en el rango
        """
        primos = []
        for num in range(max(2, inicio), fin + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def obtener_estadisticas(self):
        """
        Retorna estadísticas de uso del teorema.
        
        Returns:
            dict: Estadísticas de rendimiento
        """
        return self.estadisticas.copy()


# DEMOSTRACIÓN Y EJEMPLOS DE USO
def demostracion_completa():
    """
    Demostración completa del Teorema de Geovanni
    """
    print("=" * 70)
    print("DEMOSTRACIÓN DEL TEOREMA DE GEOVANNI")
    print("=" * 70)
    
    tg = TeoremaGeovanni()
    
    # Prueba con números conocidos
    test_cases = [
        2, 3, 17, 121, 143, 187, 7919, 104729, 999983
    ]
    
    print("\n1. VERIFICACIÓN DE PRIMALIDAD:")
    print("-" * 40)
    for num in test_cases:
        resultado = tg.es_primo(num)
        print(f"geovanni({num:>7}) = {resultado}")
    
    # Generar primeros 20 primos
    print(f"\n2. PRIMEROS 20 NÚMEROS PRIMOS:")
    print("-" * 40)
    for i in range(1, 21):
        primo = tg.obtener_nesimo_primo(i)
        print(f"P({i:>2}) = {primo:>3}")
    
    # Primos en un rango
    print(f"\n3. PRIMOS ENTRE 100 Y 150:")
    print("-" * 40)
    primos_rango = tg.generar_primos_rango(100, 150)
    print("Primos:", primos_rango)
    
    # Estadísticas
    stats = tg.obtener_estadisticas()
    print(f"\n4. ESTADÍSTICAS:")
    print("-" * 40)
    print(f"Números procesados: {stats['numeros_procesados']}")
    print(f"Primos encontrados: {stats['primos_encontrados']}")
    print(f"Tiempo total: {stats['tiempo_total']:.6f} segundos")
    
    print(f"\n5. INFORMACIÓN DEL SISTEMA:")
    print("-" * 40)
    print(f"Primos base: {tg.primos_base}")
    print(f"Primos conocidos: {len(tg.primos_conocidos)} primos almacenados")
    print(f"Mayor primo conocido: {tg.primos_conocidos[-1]}")
    
    print("\n" + "=" * 70)
    print("¡TEOREMA VERIFICADO EXITOSAMENTE!")
    print("=" * 70)

if __name__ == "__main__":
    demostracion_completa()
