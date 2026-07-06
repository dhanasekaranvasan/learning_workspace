# Numpy (Numerical Python)

NumPy arrays are **homogeneous**, meaning every single element in the array must be of the exact same data type (e.g., all 64-bit integers or all 32-bit floats). Because the data type is uniform, NumPy stores the data in a continuous block of memory.

The actual calculation is handed off to highly optimized, **pre-compiled C** and **Fortran** code underneath.

**Scalar**, **Vector**, **Matrix**

## Properties

**Dimention:**
- 0D: (Scalar) No Index
    - 2
    - "Hello"
    - True
    - 4.7
- 1D: Only '0' index [0]
    - [2,5]
    - (5,2,4)
- 2D: [[]] (get elements by [][])
    - [[2,4,5,6,7], [4,6,8,9,3]]
    - ((4,5,7,8,9,3), (4,5,6,7,8,3))
- 3D: [[[]]] (get elements by [][][])
    - [[[2,4,5,6,7], [4,6,8,9,3]]]
    - (((4,5,7,8,9,3), (4,5,6,7,8,3)),)
- N-dimensions: [] * n sub arrays

**shape:**
- () 0D (Scalar)
- (2,) 1D
- (3,4) 2D
- (2,5,6) 3D
- (2,4,5,...) Nth-Dimention

**SupportsIndex:**
- int
- list
- tuple

**dtype:**
- int_, int8, int16, int32, int64 (default int64)
- float16, float32, float64, float128 (default float64)
- uint8, uint16, uint32, uint64, uintp, uintc (default uint64)
- str_ or <U{len}" (len -> largest string size (default <U21>))
- bool_
- object_

**axis:**
- axis=0 (rows)
- axis=1 (columns)

## Array Creation

### 0-Dimention (Scalar)

`import numpy as np`

|        Code         |  Output  |
| ------------------- | -------- |
| `arr = np.array(5)` |          |
| `print(arr)`        | `5`      |
| `print(arr.dtype)`  | `int64`  |
| `print(arr.ndim)`   | `0`      |
| `print(arr.shape)`  | `()`     |
| `print(arr.size)`   | `1`      |

|           Code            |   Output  |
| ------------------------- | --------- |
|  `arr = np.array((2.5))`  |           |
|  `print(arr)`             | `2.5`     |
|  `print(arr.dtype)`       | `float64` |
|  `print(arr.ndim)`        | `0`       |
|  `print(arr.shape)`       | `()`      |
|  `print(arr.size)`        | `1`       |

|              Code              |   Output |
| ------------------------------ | -------- |
|  `arr = np.array("Hello")`     |          |
|  `print(arr)`                  | `Hello`  |
|  `print(arr.dtype)`            | `<U5`    |
|  `print(arr.ndim)`             | `0`      |
|  `print(arr.shape)`            | `()`     |
|  `print(arr.size)`             | `1`      |

|           Code            |   Output   |
| ------------------------- | ---------- |
|  `arr = np.array((True))` |            |
|  `print(arr)`             | ```True``` |
|  `print(arr.dtype)`       | ```bool``` |
|  `print(arr.ndim)`        | ```0```    |
|  `print(arr.shape)`       | ```()```   |
|  `print(arr.size)`        | ```1```    |

#### *`.astype()`* - change dtype

|         Code          | Before  |  After  | Output  |
| --------------------- | ------- | ------- | ------- |
| `arr = np.array(5)`   | `dtype` | `dtype` |         |
| `arr.astype(np.str_)` | `int64` | `<U21`  | `5`     |

|            Code           | Before  |  After  | Output |
| ------------------------- | ------- | ------- | ------ |
| `arr = np.array('Hello')` | `dtype` | `dtype` |        |
| `arr.astype(np.bool_)`    | `<U5`   | `bool`  | `True` |

|          Code          | Before  |  After  | Output |
| ---------------------- | ------- | ------- | ------ |
| `arr = np.array(True)` | `dtype` | `dtype` |        |
| `arr.astype(np.int64)` | `bool`  | `int64` | `1`    |

|            Code          | Before  |   After   |  Output  |
| ------------------------ | ------- | --------- | -------- |
| `arr = np.array('6.2')`  | `dtype` | `dtype`   |          |
| `arr.astype(np.float64)` | `<U3`   | `float64` | `6.2`    |

#### Arithmetic Operation (+, -, *, %, /, //)

- Supported dtypes: int, float, uint
- bool: True = 1, False = 0

|          Code         | Operation | Output |
| --------------------- | --------- | ------ |
| `arr1 = np.array(5)`  |           |        |
| `arr2 = np.array(2)`  |           |        |
| `print(arr1 + arr2)`  | `5 + 2`   | `7`    |
| `print(arr1 - arr2)`  | `5 - 2`   | `3`    |
| `print(arr1 * arr2)`  | `5 * 2`   | `10`   |
| `print(arr1 % arr2)`  | `5 % 2`   | `1`    |
| `print(arr1 / arr2)`  | `5 / 2`   | `2.5`  |
| `print(arr1 // arr2)` | `5 // 2`  | `2`    |

#### Comparison Operation (==, !=, <, >, >= <=)

- supported dtypes: mix types (int, float, uint, str, bool)
- 0 == 0.0 == False -> True
- 1 == 1.0 == True  -> True

|           Code             | Operation  |  Output  |
| -------------------------- | ---------- | -------- |
| `arr1 = np.array(5)`       |            |          |
| `arr2 = np.array(2)`       |            |          |
| `arr3 = np.array("hello")` |            |          |
| `arr4 = np.array('Hello')` |            |          |
| `print(arr3 == arr4)`      | `==`       | `False`  |
| `print(arr3 != arr4)`      | `!=`       | `True`   |
| `print(arr1 > arr2)`       | `5 > 2`    | `True`   |
| `print(arr1 < arr2)`       | `5 < 2`    | `Flase`  |
| `print(arr1 >= arr2)`      | `5 >= 2`   | `True`   |
| `print(arr1 <= arr2)`      | `5 <= 2`   | `False`  |

### 1-Dimention (element at [position])

|                Code               |       Output      |
| --------------------------------- | ----------------- |
| `arr = np.array([1, 2, 3, 4, 5])` |                   |
| `print(arr)`                      | `[1, 2, 3, 4, 5]` |
| `print(arr[2])`                   | `3`               |
| `print(arr.dtype)`                | `int64`           |
| `print(arr.ndim)`                 | `1`               |
| `print(arr.shape)`                | `(5, )`           |
| `print(arr.size)`                 | `5`               |

|                  Code                  |            Output            |
| -------------------------------------- | ---------------------------- |
| `arr = np.array((6.2, 7.1, 8.0, 9.5))` |                              |
| `print(arr)`                           | `[6.2, 7.1, 8.0, 9.5, 10.8]` |
| `print(arr[3])`                        | `9.5`                        |
| `print(arr.dtype)`                     | `float64`                    |
| `print(arr.ndim)`                      | `1`                          |
| `print(arr.shape)`                     | `(4, )`                      |
| `print(arr.size)`                      | `4`                          |

|                            Code                                 |                     Output                      |
| --------------------------------------------------------------- | ----------------------------------------------- |
| `arr = np.array(["John", "Allen", "Vishal", "Karan", "Sekar"])` |                                                 |
| `print(arr)`                                                    | `["John", "Allen", "Vishal", "Karan", "Sekar"]` |
| `print(arr[3])`                                                 | `Sekar`                                         |
| `print(arr.dtype)`                                              | `<U6`                                           |
| `print(arr.ndim)`                                               | `1`                                             |
| `print(arr.shape)`                                              | `(5, )`                                         |
| `print(arr.size)`                                               | `5`                                             |

|                          Code                            |                  Output                  |
| -------------------------------------------------------- | ---------------------------------------- |
| `arr = np.array([1, 0.8, "Hello", False, None, np.nan])` |                                          |
| `print(arr)`                                             | `[1, 0.8, "Hello", False, None, np.nan]` |
| `print(arr[0])`                                          | `1`                                      |
| `print(arr.dtype)`                                       | `object`                                 |
| `print(arr.ndim)`                                        | `1`                                      |
| `print(arr.shape)`                                       | `(6, )`                                  |
| `print(arr.size)`                                        | `6`                                      |

#### Arithmetic Operation (+, -, *, %, /, //)

- support dtypes: int, float, uint
- bool: False = 0, True = 1

|               Code                 |  Operation  |       Output     |
| ---------------------------------- | ----------- | ---------------- |
| `arr1 = np.array([6, False, 7])`   |             | `[6, False, 7]`  |
| `arr2 = np.array([1, 4.4, True])`  |             | `[1, 4.4, True]` |
| `print(arr1 + arr2)`               | `+`         | `[7.  4.4 8.]`   |
| `print(arr1 - arr2)`               | `- `        | `[5. -4.4  6.]`  |
| `print(arr1 * arr2)`               | `* `        | `[6. 0. 7.]`     |
| `print(arr1 % arr2)`               | `%`         | `[0. 0. 0.]`     |
| `print(arr1 / arr2)`               | `/`         | `[6. 0. 7.]`     |
| `print(arr1 // arr2)`              | `//`        | `[6. 0. 7.]`     |

|               Code              |  Operation  |            Output           |
| ------------------------------- | ----------- | --------------------------- |
| `arr1 = np.array([5, 6, 7, 8])` |             | `[5, 6, 7, 8]` |
| `arr2 = np.array([1, 2, 3, 4])` |             | `[1, 2, 3, 4]` |
| `print(arr1 + arr2)`            | `+`         | `[6  8 10 12]` |
| `print(arr1 - arr2)`            | `- `        | `[4  4  4  4]` |
| `print(arr1 * arr2)`            | `* `        | `[5 12 21 32]` |
| `print(arr1 % arr2)`            | `%`         | `[0  0  1  0]` |
| `print(arr1 / arr2)`            | `/`         | `[5. 3. 2.3 2.]` |
| `print(arr1 // arr2)`           | `//`        | `[5  3  2  2]` |

#### Comparison Operation (==, !=, <, >, >= <=)

- supported dtypes: mix types (int, float, uint, str, bool)
- 0 == 0.0 == False -> True
- 1 == 1.0 == True  -> True

|                  Code             |  Operation  |                  Output                 |
| --------------------------------- | ----------- | --------------------------------------- |
| `arr1 = np.array([1,2,3,4,7,6])`  |             | `[1,    2,     3,     4,     7,     6]` |
| `arr2 = np.array([1,2,4,5,5,6])`  |             | `[1,    2,     4,     5,     5,     6]` |
| `print(arr1 == arr2)`             | `==`        | `[ True  True False False  True  True]` |
| `print(arr1 != arr2)`             | `!=`        | `[False False  True  True False False]` |
| `print(arr1 > arr2)`              | `>`         | `[False False False False  True False]` |
| `print(arr1 < arr2)`              | `<`         | `[False False  True  True False False]` |
| `print(arr1 >= arr2)`             | `>=`        | `[ True  True False False  True  True]` |
| `print(arr1 <= arr2)`             | `<=`        | `[ True  True  True  True  True  True]` |

|                  Code                             |  Operation  |                  Output               |
| ------------------------------------------------- | ----------- | ------------------------------------- |
| `arr1 = np.array(["string",{1,3,4},1.7,False,1)`  |             | `["string", {1,3,4}, 1.7, False,  1]` |
| `arr2 = np.array(["string",{1,3,4},1.6,0,True])`  |             | `["string", {1,3,4}, 1.6,  0,  True]` |
| `print(arr1 == arr2)`                             | `==`        | `[ True   True  False   True   True]` |
| `print(arr1 != arr2)`                             | `!=`        | `[False  False   True  False  False]` |
| `print(arr1 > arr2)`                              | `>`         | `[False  False   True  False  False]` |
| `print(arr1 < arr2)`                              | `<`         | `[False  False  False  False  False]` |
| `print(arr1 >= arr2)`                             | `>=`        | `[ True   True   True   True   True]` |
| `print(arr1 <= arr2)`                             | `<=`        | `[ True   True  False   True   True]` |


### 2-Dimention (element at [position][position])

|                     Code                     |       Output       |
| -------------------------------------------- | ------------------ |
| `arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])` |                    |
| `print(arr)`                                 | `[[ 1  2  3  4  5]`<br>`[ 6  7  8  9 10]]` |
| `print(arr[1])`                              | `[ 6  7  8  9 10]` |
| `print(arr[1][2])`                           | `8`                |
| `print(arr.dtype)`                           | `int64`            |
| `print(arr.ndim)`                            | `2`                |
| `print(arr.shape)`                           | `(2, 5)`           |
| `print(arr.size)`                            | `10`               |

|                         Code                         |       Output       |
| ---------------------------------------------------- | ------------------ |
| `arr = np.array([[4.5, 6.7],[8.9, 1.2],[2.3, 3.4]])` |                    |
| `print(arr)`                                         | `[[4.5 6.7]`<br>`[8.9 1.2]`<br>`[2.3 3.4]]` |
| `print(arr[2])`                                      | `[2.3 3.4]`        |
| `print(arr[2][1])`                                   | `3.4`              |
| `print(arr.dtype)`                                   | `float64`          |
| `print(arr.ndim)`                                    | `2`                |
| `print(arr.shape)`                                   | `(3, 2)`           |
| `print(arr.size)`                                    | `6`                |

#### Arithmetic Operation (+, -, *, %, /, //)

- support dtypes: int, float, uint
- bool: False = 0, True = 1

|                        Code                       |  Operation  |              Output             |
| ------------------------------------------------- | ----------- | ------------------------------- |
| `arr1 = np.array([[1,2,False,4,5],[6,7,8,9,10]])` |             | `[[1 2 False 4 5][6 7 8 9 10]]` |
| `arr2 = np.array([[10,5,9,4,8],[3,7,2,6,True]])`  |             | `[[10 5 9 4 8][3 7 2 6 True]]`  |
| `print(arr1 + arr2)`                              | `+`         | `[[11  7  9  8 13][ 9 14 10 15 11]` |
| `print(arr1 - arr2)`                              | `- `        | `[[-9 -3 -9  0 -3][ 3  0  6  3  9]]` |
| `print(arr1 * arr2)`                              | `* `        | `[[10 10  0 16 40][18 49 16 54 10]]` |
| `print(arr1 % arr2)`                              | `%`         | `[[1 2 0 0 5][0 0 0 3 0]]` |
| `print(arr1 / arr2)`                              | `/`         | `[[0.1 0.4 0. 1. 0.625][2. 1. 4. 1.5 10.]]` |
| `print(arr1 // arr2)`                             | `//`        | `[[ 0  0  0  1  0][ 2  1  4  1 10]]` |