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

```
import numpy as np

def output(arr):
    print(arr)
    print(arr.ndim)
    print(arr.dtype)
    print(arr.shape)
    print(arr.size)
```
|                Code                |     Output    |
| ---------------------------------- | ------------- |
| ```arr = np.array(5)```            |               |
| ```print(arr)```                   | ```5```       |
| ```print(arr.dtype)```             | ```int64```   |
| ```print(arr.ndim)```              | ```0```       |
| ```print(arr.shape)```             | ```()```      |
| ```print(arr.size)```              | ```1```       |

|                Code                |     Output    |
| ---------------------------------- | ------------- |
|  ```arr = np.array((2.5))```       |               |
|  ```print(arr)```                  | ```2.5```     |
|  ```print(arr.dtype)```            | ```float64``` |
|  ```print(arr.ndim)```             | ```0```       |
|  ```print(arr.shape)```            | ```()```      |
|  ```print(arr.size)```             | ```1```       |

|                Code                |     Output    |
| ---------------------------------- | ------------- |
|  ```arr = np.array("Hello")```     |               |
|  ```print(arr)```                  | ```Hello```   |
|  ```print(arr.dtype)```            | ```<U5```     |
|  ```print(arr.ndim)```             | ```0```       |
|  ```print(arr.shape)```            | ```()```      |
|  ```print(arr.size)```             | ```1```       |

|                Code                |     Output    |
| ---------------------------------- | ------------- |
|  ```arr = np.array((True))```      |               |
|  ```print(arr)```                  | ```True```    |
|  ```print(arr.dtype)```            | ```bool```    |
|  ```print(arr.ndim)```             | ```0```       |
|  ```print(arr.shape)```            | ```()```      |
|  ```print(arr.size)```             | ```1```       |

#### *`.astype()`* - change dtype

|                Code                |     Before    |     After     |     Output    |
| ---------------------------------- | ------------- | ------------- | ------------- |
| ```arr = np.array(5)```            | ```dtype```   | ```dtype```   |               |
| ```arr.astype(np.str_)```          | ```int64```   | ```<U21```    | ```5```       |

|                Code                |     Before    |     After     |     Output    |
| ---------------------------------- | ------------- | ------------- | ------------- |
| ```arr = np.array('Hello')```      | ```dtype```   | ```dtype```   |               |
| ```arr.astype(np.str_)```          | ```<U5```     | ```bool```    | ```True```    |

|                Code                |     Before    |     After     |     Output    |
| ---------------------------------- | ------------- | ------------- | ------------- |
| ```arr = np.array(True)```         | ```dtype```   | ```dtype```   |               |
| ```arr.astype(np.int64)```          | ```bool```   | ```int64```   | ```1```       |

|                Code                |     Before    |     After     |     Output    |
| ---------------------------------- | ------------- | ------------- | ------------- |
| ```arr = np.array('6.2')```        | ```dtype```   | ```dtype```   |               |
| ```arr.astype(np.float64)```       | ```<U3```     | ```float64``` | ```6.2```     |

#### Arithmetic Operation (+, -, *, %, /, //)

- Supported dtypes: int, float, uint

|            Code           |  Operation   |   Output  |
| ------------------------- | ------------ | --------- |
| ```arr1 = np.array(5)```  |              |           |
| ```arr2 = np.array(2)```  |              |           |
| ```print(arr1 + arr2)```  | ```5 + 2```  | ```7```   |
| ```print(arr1 - arr2)```  | ```5 - 2```  | ```3```   |
| ```print(arr1 * arr2)```  | ```5 * 2```  | ```10```  |
| ```print(arr1 % arr2)```  | ```5 % 2```  | ```1```   |
| ```print(arr1 / arr2)```  | ```5 / 2```  | ```2.5``` |
| ```print(arr1 // arr2)``` | ```5 // 2``` | ```2```   |

#### Comparison Operation (==, !=, <, >, >= <=)

- supported dtypes: mix types (int, float, uint, str, bool)
- 0 == 0.0 == False -> True
- 1 == 1.0 == True  -> True

|               Code             |   Operation  |    Output   |
| ------------------------------ | ------------ | ------------|
| ```arr1 = np.array(5)```       |              |             |
| ```arr2 = np.array(2)```       |              |             |
| ```arr3 = np.array("hello")``` |              |             |
| ```arr4 = np.array('Hello')``` |              |             |
| ```print(arr3 == arr4)```      | ```5 == 2``` | ```False``` |
| ```print(arr3 != arr4)```      | ```5 != 2``` | ```True```  |
| ```print(arr1 > arr2)```       | ```5 > 2```  | ```True```  |
| ```print(arr1 < arr2)```       | ```5 < 2```  | ```Flase``` |
| ```print(arr1 >= arr2)```      | ```5 >= 2``` | ```True```  |
| ```print(arr1 <= arr2)```      | ```5 <= 2``` | ```False``` |