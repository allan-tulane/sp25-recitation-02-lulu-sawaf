# CMPS 2200  Recitation 02

**Name (Team Member 1):**_Lulu Sawaf_______________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [x] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [x] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [x] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [x] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

f(n)=1
  $W(n) = aW(n/b) + 1$
  if a > 1 then it isleaf-dominated therefore $W(n) = O(n^{\log_b a})$
  if a=1 then it is balanced therefore $W(n)= O(\log n)

f(n)=logn
  $W(n) = aW(n/b) + \log n$
  if $f(n) = \log n$ then it is balanced therefore $W(n) = O(n\log n)$

f(n) = n
  $W(n) = aW(n/b) + n$
  if a>b then it is root dominated therefore $W(n) = O(n)$
  if a<b then it is leaf dominated therefore $W(n) = O(n^{\log_b a})$
  if a = b then it is balanced therefore $W(n) = O(n\log (n))$ 

Comparison of work functions:
f(n) = 1, f(n) = logn
|     n |   W_1 |       W_2 |
|-------|-------|-----------|
|    10 |    15 |    16.294 |
|    20 |    31 |    35.584 |
|    50 |    63 |    84.201 |
|   100 |   127 |   173.008 |
|  1000 |  1023 |  1471.608 |
|  5000 |  8191 |  9919.326 |
| 10000 | 16383 | 19847.862 |

Comparison of work functions:
f(n) = 1, f(n) = n
|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |    15 |     36 |
|    20 |    31 |     92 |
|    50 |    63 |    276 |
|   100 |   127 |    652 |
|  1000 |  1023 |   9120 |
|  5000 |  8191 |  61728 |
| 10000 | 16383 | 133456 |
       

- [x] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

$W(n) = W(n) = aW(n / b) + n^c
Case 1: c < log_base b_a (leaf-dominated)
Complexity of the leaf dominated function: W(n) = 0(n^log_base b_a)
Comparison of work functions:
work_fn1 = lambda n: work_calc(n, 4, 2, lambda x: x)
work_fn2 = lambda n: work_calc(n, 4, 2, lambda x: x**0.5)
work_fn2 ~~ O(n) = n^2

|     n |       W_1 |           W_2 |
|-------|-----------|---------------|
|    10 |       126 |        98.734 |
|    20 |       524 |       399.408 |
|    50 |      2518 |      1706.669 |
|   100 |     10172 |      6836.676 |
|  1000 |    697496 |    443674.137 |
|  5000 |  34237688 |  26036347.356 |
| 10000 | 136960752 | 104145489.424 |

Case 2: c > log_base b_a) (root-dominated)
Complexity of root dominated: W(n) = 0(n^c)
Comparison of work functions:
work_fn1 = lambda n: work_calc(n, 4, 2, lambda x: x)
work_fn2 = lambda n: work_calc(n, 4, 2, lambda x: x**2)
work_fn2 ~~ O(n) = n^2

|     n |       W_1 |        W_2 |
|-------|-----------|------------|
|    10 |       126 |        328 |
|    20 |       524 |       1712 |
|    50 |      2518 |      12936 |
|   100 |     10172 |      61744 |
|  1000 |    697496 |    8544512 |
|  5000 |  34237688 |  294904064 |
| 10000 | 136960752 | 1279616256 |

Case 3: c = log,a (balanced)
work is even between leaf and root. therefore complexity of O(n^c logn)
Comparison of work functions:
work_fn1 = lambda n: work_calc(n, 4, 2, lambda x: x)
work_fn2 = lambda n: work_calc(n, 4, 2, lambda X: x**2*math.log(x))
work_fn2 ~~ O(n) = n^2logn

|     n |       W_1 |            W_2 |
|-------|-----------|----------------|
|    10 |       126 |        499.564 |
|    20 |       524 |       3196.548 |
|    50 |      2518 |      31235.889 |
|   100 |     10172 |     170995.256 |
|  1000 |    697496 |   35880844.351 |
|  5000 |  34237688 | 1384552219.544 |
| 10000 | 136960752 | 6459242915.374 |

- [x] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

S(n) = S(n / b) + f(n) is work but not multiplied by a (because we consider one path at a time)
Case 1: f(n) = 1    S(n) = S(n /b) + 1
O(1) is constant- complexity of O(logn)

Case 2: f(n) = n    S(n) = S(n /b) + n
f(n) = n asymptotically dominates- complexity of O(n)

Case 3: f(n) = logn,    S(n) = S(n / b) + logn
both terms are O(logn), complexity of O(log'n)

f(n) = 1 increases slowest (about rate of logn). f(n) = n increases linearly
f(n) = logn grows slowly (faster than f(n) = 1, slower than linear)

Comparison of span functions:
span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: x)

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |    18 |
|    20 |     5 |    38 |
|    50 |     6 |    97 |
|   100 |     7 |   197 |
|  1000 |    10 |  1994 |
|  5000 |    13 |  9995 |
| 10000 |    14 | 19995 |

Comparison of span functions:
span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: math.log (x))

|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |     4 |  5.605 |
|    20 |     5 |  8.601 |
|    50 |     6 | 13.506 |
|   100 |     7 | 18.111 |
|  1000 |    10 | 37.786 |
|  5000 |    13 | 56.944 |
| 10000 |    14 | 66.154 |