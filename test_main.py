from main import *


def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(50, 2, 2) == 276
	assert simple_work_calc(60, 3, 2) == 960


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(40, 2, 2, lambda n: n) == 224
	assert work_calc(50, 2, 2, lambda n: n) == 276
	assert work_calc(60, 3, 2, lambda n: n) == 960


def test_compare_work():

	work_fn1 = lambda n: work_calc(n, 4, 2, lambda x: x) 
	work_fn2 = lambda n: work_calc(n, 4, 2, lambda x: x**2)

	sizes=[10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_work(work_fn1, work_fn2, sizes)
	print("\nComparison of work functions:")
	print_results(res)

	assert len(res) > 0

	print(res)


def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: math.log(x))

	sizes=[10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_span(span_fn1, span_fn2, sizes)
	print("\nComparison of span functions:")
	print_results(res)

	assert len(res) > 0, "Results should not be empty"
