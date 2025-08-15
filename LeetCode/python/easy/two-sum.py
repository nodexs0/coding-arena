class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Constraints:
            
            2 <= nums.length <= 104
            -109 <= nums[i] <= 109
            -109 <= target <= 109


        nums = [2, 7, 11, 15]
        target = 9

        return [i, j] where nums[i] + nums[j] == target

        output = [0, 1] # because nums[0] + nums[1] == 9

        Como seria el algoritmo?

        Solucion Fuerza Bruta:
        Para cada elemento en nums, iterar sobre el resto de los elementos y verificar si la suma es igual al target.

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        Esta solucion tiene una complejidad de tiempo O(n^2) porque estamos iterando sobre todos los pares posibles de elementos.

        Como se puede mejorar el algoritmo?

        Recorrer solo una vez la lista
        
        nums = [2, 7, 11, 15]
        target = 9

        indice 0
        elemento 2
        9 - 2 = 7

        Como el numero 7 no ha sido visto, lo guardamos en un diccionario el elemento y su indice

        dict = {2: 0}

        indice 1
        elemento 7
        9 - 7 = 2

        Como el numero 2 ya ha sido visto significa que el elemento 7 y el elemento 2 suman el target
        
        solucion = [dict[2], 1] = [0, 1]

        EL agoritmo funcionaria si el array no estuviera ordenado? 

        nums = [7, 15, 2, 11]
        target = 9

        indice 0
        elemento 7
        9 - 7 = 2

        Como el numero 2 no ha sido visto, lo guardamos en un diccionario el elemento y su indice

        dict = {7: 0}

        indice 1
        elemento 15
        9 - 15 = -6
        Como el numero -6 no ha sido visto, lo guardamos en un diccionario el elemento y su indice

        dict = {7: 0, 15: 1}

        indice 2
        elemento 2
        9 - 2 = 7
        Como el numero 7 ya ha sido visto significa que el elemento 2 y el elemento 7 suman el target
        solucion = [dict[7], 2] = [0, 2]


        """
        # Restricciones:
        # 2 <= nums.length <= 10^4
        if len(nums) < 2 or len(nums) > 10**4:
            return []
        # -10^9 <= nums[i] <= 10^9
        for num in nums:
            if num < -10**9 or num > 10**9:
                return []
        # -10^9 <= target <= 10^9
        if target < -10**9 or target > 10**9:
            return []

        diccionario_nums = {}

        for indice, elemento in enumerate(nums):

            complemento = target - elemento

            if complemento in diccionario_nums:
                return [diccionario_nums[complemento], indice]

            diccionario_nums[elemento] = indice

        return []
